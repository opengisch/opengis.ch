#!/usr/bin/env python3
"""Audit sitemap pages against local Hugo output and generate a JSON report.

The audit can also suggest (or apply) Hugo aliases when the same page text exists
under a different local URL.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import re
import subprocess
import sys
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from difflib import SequenceMatcher
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable
from urllib.parse import unquote, urlparse
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET

try:
    from scripts.sitemap_audit_viewer import derive_html_output_path, write_html_report
except ModuleNotFoundError:
    from sitemap_audit_viewer import derive_html_output_path, write_html_report

DEFAULT_HEADERS = {
    "User-Agent": "opengis-sitemap-audit/1.0 (+https://www.opengis.ch)",
    "Accept": "application/xml,text/xml,text/html;q=0.9,*/*;q=0.8",
}

LANG_SEGMENTS = {"de", "fr", "it", "en"}
DATE_SEGMENT_RE = re.compile(r"^\d{4}$")
MONTH_SEGMENT_RE = re.compile(r"^(0[1-9]|1[0-2])$")
DAY_SEGMENT_RE = re.compile(r"^(0[1-9]|[12][0-9]|3[01])$")
TOP_LEVEL_MEDIA_SLUG_RE = re.compile(
    r"^[^/]+-(mp4|m4v|mov|webm|avi|wmv|png|jpg|jpeg|gif|webp|svg|pdf)(-[0-9]+)?$",
    re.IGNORECASE,
)
TOP_LEVEL_NUMERIC_ATTACHMENT_RE = re.compile(r"^\d[\da-z_-]*$", re.IGNORECASE)


class VisibleTextParser(HTMLParser):
    """Collect visible text while ignoring scripts/styles and selected tags."""

    IGNORE_TAGS = {
        "script",
        "style",
        "noscript",
        "svg",
        "canvas",
        "iframe",
    }

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self._ignored_depth = 0
        self._parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in self.IGNORE_TAGS:
            self._ignored_depth += 1

    def handle_endtag(self, tag: str) -> None:
        if tag in self.IGNORE_TAGS and self._ignored_depth > 0:
            self._ignored_depth -= 1

    def handle_data(self, data: str) -> None:
        if self._ignored_depth == 0:
            self._parts.append(data)

    def text(self) -> str:
        raw = " ".join(self._parts)
        return re.sub(r"\s+", " ", raw).strip()


@dataclass
class LocalPageEntry:
    url: str
    html_file: str
    text: str
    text_sha256: str


@dataclass
class ContentEntry:
    url: str
    content_file: str
    source_path: str | None


@dataclass
class PageAuditResult:
    url: str
    path: str
    local_file: str | None
    local_exists: bool
    source_type: str | None
    source_file: str | None
    source_fetch_ok: bool
    local_read_ok: bool
    text_exact_match: bool
    text_similarity: float | None
    source_text_chars: int | None
    local_text_chars: int | None
    source_text_sha256: str | None
    local_text_sha256: str | None
    matched_local_url: str | None
    matched_local_file: str | None
    alias_content_file: str | None
    alias_applied: bool
    issues: list[str]


def fetch_url_text(url: str, timeout: int = 20) -> str:
    request = Request(url, headers=DEFAULT_HEADERS)
    with urlopen(request, timeout=timeout) as response:
        content_type = response.headers.get("Content-Type", "")
        charset = "utf-8"
        if "charset=" in content_type:
            charset = content_type.split("charset=", 1)[1].split(";", 1)[0].strip()
        raw = response.read()
    return raw.decode(charset, errors="replace")


def parse_sitemap_xml(xml_text: str) -> tuple[list[str], list[str]]:
    """Return (page_urls, nested_sitemap_urls)."""
    root = ET.fromstring(xml_text)
    ns_match = re.match(r"\{(.+)}", root.tag)
    ns = {"sm": ns_match.group(1)} if ns_match else {}

    def findall(path: str) -> list[ET.Element]:
        return root.findall(path, ns) if ns else root.findall(path.replace("sm:", ""))

    tag_name = root.tag.split("}")[-1].lower()
    urls: list[str] = []
    nested: list[str] = []

    if tag_name == "urlset":
        loc_path = ".//sm:url/sm:loc" if ns else ".//url/loc"
        for loc in findall(loc_path):
            if loc.text:
                urls.append(loc.text.strip())
    elif tag_name == "sitemapindex":
        loc_path = ".//sm:sitemap/sm:loc" if ns else ".//sitemap/loc"
        for loc in findall(loc_path):
            if loc.text:
                nested.append(loc.text.strip())
    else:
        raise ValueError(f"Unsupported sitemap root tag: {root.tag}")

    return urls, nested


def collect_sitemap_urls(sitemap_url: str, timeout: int = 20) -> list[str]:
    pending = [sitemap_url]
    visited: set[str] = set()
    page_urls: list[str] = []

    while pending:
        current = pending.pop()
        if current in visited:
            continue
        visited.add(current)

        xml_text = fetch_url_text(current, timeout=timeout)
        urls, nested = parse_sitemap_xml(xml_text)

        for nested_url in nested:
            if nested_url not in visited:
                pending.append(nested_url)

        page_urls.extend(urls)

    deduped: list[str] = []
    seen: set[str] = set()
    for url in page_urls:
        if url not in seen:
            seen.add(url)
            deduped.append(url)

    return deduped


def is_allowed_domain(url: str, allowed_domains: set[str]) -> bool:
    host = (urlparse(url).hostname or "").lower()
    return host in allowed_domains


def is_html_page_url(url: str) -> bool:
    path = (urlparse(url).path or "").lower()
    excluded_suffixes = {
        ".jpg",
        ".jpeg",
        ".png",
        ".gif",
        ".webp",
        ".svg",
        ".pdf",
        ".xml",
        ".txt",
        ".json",
        ".rss",
        ".js",
        ".css",
        ".ico",
        ".zip",
    }
    if any(path.endswith(suffix) for suffix in excluded_suffixes):
        return False
    return not is_probable_wordpress_attachment_path(path)


def normalize_route_path(path: str) -> str:
    if not path:
        return "/"

    if not path.startswith("/"):
        path = f"/{path}"

    if path != "/" and not path.endswith("/"):
        tail = path.rsplit("/", 1)[-1]
        if "." not in tail:
            path = f"{path}/"

    return path


def url_path(url: str) -> str:
    parsed = urlparse(url)
    path = unquote(parsed.path or "/")
    return normalize_route_path(path)


def split_route_segments(path: str) -> list[str]:
    return [segment for segment in path.strip("/").split("/") if segment]


def is_dated_blog_path(path: str) -> bool:
    segments = split_route_segments(path)
    if not segments:
        return False

    if segments[0] in LANG_SEGMENTS:
        segments = segments[1:]

    if segments and segments[0] == "blog":
        segments = segments[1:]

    if len(segments) < 4:
        return False

    return bool(
        DATE_SEGMENT_RE.match(segments[0])
        and MONTH_SEGMENT_RE.match(segments[1])
        and DAY_SEGMENT_RE.match(segments[2])
    )


def is_probable_wordpress_attachment_path(path: str) -> bool:
    normalized = normalize_route_path(path)
    segments = split_route_segments(normalized)
    if not segments:
        return False

    if segments[0].startswith("_"):
        return True

    if len(segments) == 1 and TOP_LEVEL_MEDIA_SLUG_RE.match(segments[0]):
        return True

    if len(segments) == 1 and TOP_LEVEL_NUMERIC_ATTACHMENT_RE.match(segments[0]):
        return True

    if not is_dated_blog_path(normalized):
        return False

    if segments[0] in LANG_SEGMENTS:
        segments = segments[1:]
    if segments and segments[0] == "blog":
        segments = segments[1:]

    return len(segments) > 4


def equivalent_blog_paths(path: str) -> list[str]:
    normalized = normalize_route_path(path)
    candidates = [normalized]

    if not is_dated_blog_path(normalized):
        return candidates

    segments = split_route_segments(normalized)
    prefix: list[str] = []
    remainder = segments

    if remainder and remainder[0] in LANG_SEGMENTS:
        prefix = [remainder[0]]
        remainder = remainder[1:]

    if remainder and remainder[0] == "blog":
        alternate = prefix + remainder[1:]
        if alternate:
            candidates.append(normalize_route_path("/" + "/".join(alternate) + "/"))
    else:
        candidates.append(normalize_route_path("/" + "/".join(prefix + ["blog"] + remainder) + "/"))

    deduped: list[str] = []
    seen: set[str] = set()
    for candidate in candidates:
        if candidate not in seen:
            seen.add(candidate)
            deduped.append(candidate)
    return deduped


def path_to_local_candidates(path: str, public_dir: Path) -> list[Path]:
    cleaned = path.lstrip("/")
    candidates: list[Path] = []

    if cleaned.endswith("/"):
        candidates.append(public_dir / cleaned / "index.html")
    elif cleaned.endswith(".html"):
        candidates.append(public_dir / cleaned)
        candidates.append(public_dir / cleaned.removesuffix(".html") / "index.html")
    else:
        candidates.append(public_dir / cleaned / "index.html")
        candidates.append(public_dir / cleaned)

    deduped: list[Path] = []
    seen: set[Path] = set()
    for candidate in candidates:
        norm = candidate.resolve(strict=False)
        if norm not in seen:
            seen.add(norm)
            deduped.append(candidate)

    return deduped


def local_candidates_for_url(url: str, public_dir: Path) -> list[Path]:
    candidates: list[Path] = []

    for path in equivalent_blog_paths(url_path(url)):
        if path == "/":
            candidates.append(public_dir / "index.html")
            continue
        candidates.extend(path_to_local_candidates(path, public_dir))

    deduped: list[Path] = []
    seen: set[Path] = set()
    for candidate in candidates:
        norm = candidate.resolve(strict=False)
        if norm not in seen:
            seen.add(norm)
            deduped.append(candidate)

    return deduped


def public_file_to_url(public_dir: Path, html_file: Path) -> str:
    relative = html_file.relative_to(public_dir).as_posix()
    if relative == "index.html":
        return "/"
    if relative.endswith("/index.html"):
        return normalize_route_path(f"/{relative[: -len('/index.html')]}/")
    return normalize_route_path(f"/{relative}")


def extract_primary_html_region(html: str) -> str:
    lowered = html.lower()

    main_start = lowered.find("<main")
    if main_start != -1:
        main_open_end = lowered.find(">", main_start)
        main_close = lowered.find("</main>", main_open_end + 1)
        if main_open_end != -1 and main_close != -1:
            return html[main_open_end + 1 : main_close]

    body_start = lowered.find("<body")
    if body_start != -1:
        body_open_end = lowered.find(">", body_start)
        body_close = lowered.find("</body>", body_open_end + 1)
        if body_open_end != -1 and body_close != -1:
            return html[body_open_end + 1 : body_close]

    return html


def normalize_visible_text(html: str) -> str:
    parser = VisibleTextParser()
    parser.feed(extract_primary_html_region(html))
    parser.close()
    return parser.text()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def compare_texts(source_html: str, local_html: str) -> tuple[bool, float, str, str]:
    source_text = normalize_visible_text(source_html)
    local_text = normalize_visible_text(local_html)
    exact = source_text == local_text
    similarity = SequenceMatcher(a=source_text, b=local_text).ratio()
    return exact, similarity, source_text, local_text


def read_local_html(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def choose_existing_path(paths: Iterable[Path]) -> Path | None:
    for path in paths:
        if path.exists() and path.is_file():
            return path
    return None


def maybe_build_hugo(public_dir: Path) -> None:
    cmd = ["hugo", "--destination", str(public_dir)]
    subprocess.run(cmd, check=True)


def source_candidates_for_url(url: str, offline_dir: Path) -> list[Path]:
    parsed = urlparse(url)
    host = (parsed.hostname or "").lower()
    hosts = [host]
    if host == "opengis.ch":
        hosts.append("www.opengis.ch")

    candidates: list[Path] = []
    for path in equivalent_blog_paths(url_path(url)):
        cleaned = path.lstrip("/")
        for candidate_host in hosts:
            host_root = offline_dir / candidate_host
            if path == "/":
                candidates.append(host_root / "index.html")
                continue

            if cleaned.endswith("/"):
                candidates.append(host_root / cleaned / "index.html")
            else:
                candidates.append(host_root / cleaned)
                candidates.append(host_root / cleaned / "index.html")

    return candidates


def read_source_html(
    *,
    url: str,
    offline_dir: Path | None,
    timeout: int,
) -> tuple[str | None, str | None, str | None, bool]:
    if offline_dir is not None:
        for candidate in source_candidates_for_url(url, offline_dir):
            if candidate.exists() and candidate.is_file():
                return "offline", str(candidate), read_local_html(candidate), True

    try:
        remote_html = fetch_url_text(url, timeout=timeout)
        return "remote", None, remote_html, True
    except Exception:
        return None, None, None, False


def language_segment(path: str) -> str:
    parts = path.strip("/").split("/", 1)
    if not parts or not parts[0]:
        return ""
    return parts[0] if parts[0] in LANG_SEGMENTS else ""


def choose_alias_candidate(missing_path: str, candidates: list[LocalPageEntry]) -> LocalPageEntry:
    missing_lang = language_segment(missing_path)

    def rank(entry: LocalPageEntry) -> tuple[int, int]:
        candidate_lang = language_segment(entry.url)
        same_lang = 1 if missing_lang and missing_lang == candidate_lang else 0
        length_penalty = -abs(len(entry.url) - len(missing_path))
        return same_lang, length_penalty

    return max(candidates, key=rank)


def build_local_page_index(
    public_dir: Path,
) -> tuple[dict[str, LocalPageEntry], dict[str, list[LocalPageEntry]]]:
    by_url: dict[str, LocalPageEntry] = {}
    by_text_hash: dict[str, list[LocalPageEntry]] = {}

    for html_file in public_dir.rglob("*.html"):
        if not html_file.is_file():
            continue

        url = public_file_to_url(public_dir, html_file)
        text = normalize_visible_text(read_local_html(html_file))
        text_hash = sha256_text(text)

        entry = LocalPageEntry(
            url=url,
            html_file=str(html_file),
            text=text,
            text_sha256=text_hash,
        )
        by_url[url] = entry
        by_text_hash.setdefault(text_hash, []).append(entry)

    return by_url, by_text_hash


def normalize_source_path(source_value: str) -> str:
    raw = source_value.strip().strip("\"").strip("'")
    if not raw:
        return "/"

    if "://" in raw:
        path = urlparse(raw).path or "/"
    else:
        parts = raw.split("/", 1)
        if len(parts) == 2 and "." in parts[0]:
            path = f"/{parts[1]}"
        else:
            path = raw if raw.startswith("/") else f"/{raw}"

    path = unquote(path)

    if path.endswith("/index.html"):
        base = path[: -len("/index.html")]
        return normalize_route_path(base if base else "/")

    return normalize_route_path(path)


def parse_frontmatter_fields(markdown_text: str) -> dict[str, str]:
    lines = markdown_text.splitlines()
    if len(lines) < 3 or lines[0].strip() != "---":
        return {}

    end_index = None
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            end_index = idx
            break

    if end_index is None:
        return {}

    fields: dict[str, str] = {}
    for line in lines[1:end_index]:
        match = re.match(r"^\s*([A-Za-z0-9_-]+):\s*(.+?)\s*$", line)
        if not match:
            continue
        fields[match.group(1).lower()] = match.group(2).strip().strip("\"").strip("'")
    return fields


def build_content_indexes(
    content_dir: Path,
) -> tuple[dict[str, str], dict[str, ContentEntry]]:
    url_to_file: dict[str, str] = {}
    source_to_content: dict[str, ContentEntry] = {}

    for markdown_file in content_dir.rglob("index*.md"):
        if not markdown_file.is_file():
            continue

        fields = parse_frontmatter_fields(read_local_html(markdown_file))
        raw_url = fields.get("url")
        if not raw_url:
            continue

        url = normalize_route_path(raw_url)
        content_file = str(markdown_file)
        url_to_file.setdefault(url, content_file)

        raw_source = fields.get("source")
        if raw_source:
            source_path = normalize_source_path(raw_source)
            source_to_content.setdefault(
                source_path,
                ContentEntry(url=url, content_file=content_file, source_path=source_path),
            )

    return url_to_file, source_to_content


def parse_alias_items(raw_items: list[str]) -> list[str]:
    parsed: list[str] = []
    for raw in raw_items:
        value = raw.strip().strip("\"").strip("'")
        if value:
            parsed.append(normalize_route_path(value))
    return parsed


def add_alias_to_markdown(content_file: Path, alias_path: str) -> bool:
    alias_path = normalize_route_path(alias_path)
    text = read_local_html(content_file)
    lines = text.splitlines()

    if len(lines) < 3 or lines[0].strip() != "---":
        return False

    fm_end = None
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            fm_end = idx
            break

    if fm_end is None:
        return False

    fm_lines = lines[1:fm_end]
    body_lines = lines[fm_end + 1 :]

    aliases_idx = None
    aliases_end = None
    aliases: list[str] = []

    for idx, line in enumerate(fm_lines):
        match = re.match(r"^\s*aliases:\s*(.*)$", line)
        if not match:
            continue

        aliases_idx = idx
        remainder = match.group(1).strip()
        aliases_end = idx + 1

        if remainder and remainder != "[]":
            if remainder.startswith("[") and remainder.endswith("]"):
                inline = remainder[1:-1]
                aliases.extend(parse_alias_items(inline.split(",")))
            else:
                aliases.extend(parse_alias_items([remainder]))

        scan = idx + 1
        while scan < len(fm_lines):
            item_match = re.match(r"^\s*-\s*(.+?)\s*$", fm_lines[scan])
            if not item_match:
                break
            aliases.extend(parse_alias_items([item_match.group(1)]))
            scan += 1
        aliases_end = scan
        break

    aliases = sorted(set(aliases))
    if alias_path in aliases:
        return False

    aliases.append(alias_path)
    aliases = sorted(set(aliases))
    alias_block = ["aliases:"] + [f'  - "{item}"' for item in aliases]

    if aliases_idx is not None and aliases_end is not None:
        new_fm = fm_lines[:aliases_idx] + alias_block + fm_lines[aliases_end:]
    else:
        insert_idx = len(fm_lines)
        for idx, line in enumerate(fm_lines):
            if re.match(r"^\s*url:\s*", line):
                insert_idx = idx + 1
                break
        new_fm = fm_lines[:insert_idx] + alias_block + fm_lines[insert_idx:]

    out_lines = ["---"] + new_fm + ["---"] + body_lines
    content_file.write_text("\n".join(out_lines).rstrip("\n") + "\n", encoding="utf-8")
    return True


def audit_single_url(
    *,
    url: str,
    public_dir: Path,
    timeout: int,
    similarity_threshold: float,
    offline_dir: Path | None,
    local_by_url: dict[str, LocalPageEntry],
    local_by_hash: dict[str, list[LocalPageEntry]],
    content_url_index: dict[str, str],
    content_source_index: dict[str, ContentEntry],
) -> PageAuditResult:
    path = url_path(url)
    local_entry = None
    for candidate_path in equivalent_blog_paths(path):
        local_entry = local_by_url.get(candidate_path)
        if local_entry is not None:
            break

    issues: list[str] = []
    local_exists = local_entry is not None
    if not local_exists:
        issues.append("local_page_missing")

    source_type, source_file, source_html, source_fetch_ok = read_source_html(
        url=url,
        offline_dir=offline_dir,
        timeout=timeout,
    )

    if not source_fetch_ok or source_html is None:
        issues.append("source_fetch_failed")
        return PageAuditResult(
            url=url,
            path=path,
            local_file=local_entry.html_file if local_entry else None,
            local_exists=local_exists,
            source_type=source_type,
            source_file=source_file,
            source_fetch_ok=False,
            local_read_ok=local_exists,
            text_exact_match=False,
            text_similarity=None,
            source_text_chars=None,
            local_text_chars=len(local_entry.text) if local_entry else None,
            source_text_sha256=None,
            local_text_sha256=local_entry.text_sha256 if local_entry else None,
            matched_local_url=None,
            matched_local_file=None,
            alias_content_file=None,
            alias_applied=False,
            issues=issues,
        )

    source_text = normalize_visible_text(source_html)
    source_hash = sha256_text(source_text)

    if local_entry is not None:
        similarity = SequenceMatcher(a=source_text, b=local_entry.text).ratio()
        exact = source_text == local_entry.text
        if not exact and similarity < similarity_threshold:
            issues.append("text_mismatch")
        elif not exact:
            issues.append("text_diff_within_threshold")

        return PageAuditResult(
            url=url,
            path=path,
            local_file=local_entry.html_file,
            local_exists=True,
            source_type=source_type,
            source_file=source_file,
            source_fetch_ok=True,
            local_read_ok=True,
            text_exact_match=exact,
            text_similarity=similarity,
            source_text_chars=len(source_text),
            local_text_chars=len(local_entry.text),
            source_text_sha256=source_hash,
            local_text_sha256=local_entry.text_sha256,
            matched_local_url=path,
            matched_local_file=local_entry.html_file,
            alias_content_file=None,
            alias_applied=False,
            issues=issues,
        )

    mapped_content = None
    for candidate_path in equivalent_blog_paths(path):
        mapped_content = content_source_index.get(candidate_path)
        if mapped_content is not None:
            break
    if mapped_content is not None:
        matched_entry = local_by_url.get(mapped_content.url)
        issues.append("content_found_under_different_url")

        similarity = None
        local_chars = None
        local_hash = None
        if matched_entry is not None:
            similarity = SequenceMatcher(a=source_text, b=matched_entry.text).ratio()
            local_chars = len(matched_entry.text)
            local_hash = matched_entry.text_sha256

        return PageAuditResult(
            url=url,
            path=path,
            local_file=None,
            local_exists=False,
            source_type=source_type,
            source_file=source_file,
            source_fetch_ok=True,
            local_read_ok=matched_entry is not None,
            text_exact_match=similarity == 1.0 if similarity is not None else False,
            text_similarity=similarity,
            source_text_chars=len(source_text),
            local_text_chars=local_chars,
            source_text_sha256=source_hash,
            local_text_sha256=local_hash,
            matched_local_url=mapped_content.url,
            matched_local_file=matched_entry.html_file if matched_entry else None,
            alias_content_file=mapped_content.content_file,
            alias_applied=False,
            issues=issues,
        )

    candidates = local_by_hash.get(source_hash, [])
    if not candidates:
        return PageAuditResult(
            url=url,
            path=path,
            local_file=None,
            local_exists=False,
            source_type=source_type,
            source_file=source_file,
            source_fetch_ok=True,
            local_read_ok=False,
            text_exact_match=False,
            text_similarity=None,
            source_text_chars=len(source_text),
            local_text_chars=None,
            source_text_sha256=source_hash,
            local_text_sha256=None,
            matched_local_url=None,
            matched_local_file=None,
            alias_content_file=None,
            alias_applied=False,
            issues=issues,
        )

    matched_entry = choose_alias_candidate(path, candidates)
    issues.append("content_found_under_different_url")

    return PageAuditResult(
        url=url,
        path=path,
        local_file=None,
        local_exists=False,
        source_type=source_type,
        source_file=source_file,
        source_fetch_ok=True,
        local_read_ok=False,
        text_exact_match=True,
        text_similarity=1.0,
        source_text_chars=len(source_text),
        local_text_chars=len(matched_entry.text),
        source_text_sha256=source_hash,
        local_text_sha256=matched_entry.text_sha256,
        matched_local_url=matched_entry.url,
        matched_local_file=matched_entry.html_file,
        alias_content_file=content_url_index.get(matched_entry.url),
        alias_applied=False,
        issues=issues,
    )


def audit_urls_concurrent(
    *,
    urls: list[str],
    public_dir: Path,
    timeout: int,
    similarity_threshold: float,
    concurrency: int,
    offline_dir: Path | None,
    local_by_url: dict[str, LocalPageEntry],
    local_by_hash: dict[str, list[LocalPageEntry]],
    content_url_index: dict[str, str],
    content_source_index: dict[str, ContentEntry],
) -> list[PageAuditResult]:
    if not urls:
        return []

    max_workers = max(1, concurrency)
    ordered_results: list[PageAuditResult | None] = [None] * len(urls)

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures: dict[concurrent.futures.Future[PageAuditResult], int] = {}
        for idx, url in enumerate(urls):
            future = executor.submit(
                audit_single_url,
                url=url,
                public_dir=public_dir,
                timeout=timeout,
                similarity_threshold=similarity_threshold,
                offline_dir=offline_dir,
                local_by_url=local_by_url,
                local_by_hash=local_by_hash,
                content_url_index=content_url_index,
                content_source_index=content_source_index,
            )
            futures[future] = idx

        for future in concurrent.futures.as_completed(futures):
            idx = futures[future]
            ordered_results[idx] = future.result()

    return [result for result in ordered_results if result is not None]


def apply_alias_updates(results: list[PageAuditResult]) -> list[dict[str, str]]:
    updates: list[dict[str, str]] = []
    seen: set[tuple[str, str]] = set()

    for result in results:
        if not result.alias_content_file:
            continue
        if "content_found_under_different_url" not in result.issues:
            continue

        key = (result.alias_content_file, result.path)
        if key in seen:
            continue
        seen.add(key)

        content_file = Path(result.alias_content_file)
        if add_alias_to_markdown(content_file, result.path):
            result.alias_applied = True
            updates.append(
                {
                    "content_file": result.alias_content_file,
                    "alias_added": result.path,
                    "target_url": result.matched_local_url or "",
                }
            )

    return updates


def summarize(results: list[PageAuditResult]) -> dict[str, int | float]:
    similarities = [r.text_similarity for r in results if r.text_similarity is not None]

    return {
        "checked_pages": len(results),
        "local_page_missing": sum("local_page_missing" in r.issues for r in results),
        "source_fetch_failed": sum("source_fetch_failed" in r.issues for r in results),
        "text_exact_match": sum(r.text_exact_match for r in results),
        "text_mismatch": sum("text_mismatch" in r.issues for r in results),
        "text_diff_within_threshold": sum("text_diff_within_threshold" in r.issues for r in results),
        "content_found_under_different_url": sum(
            "content_found_under_different_url" in r.issues for r in results
        ),
        "alias_applied": sum(r.alias_applied for r in results),
        "average_similarity": round(sum(similarities) / len(similarities), 6) if similarities else 0.0,
    }


def write_report(path: Path, report: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=2, ensure_ascii=True), encoding="utf-8")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Compare opengis.ch sitemap pages with local Hugo output and emit JSON report."
    )
    parser.add_argument(
        "--sitemap-url",
        default="https://opengis.ch/sitemap.xml",
        help="Sitemap URL to crawl (supports sitemap index recursion).",
    )
    parser.add_argument(
        "--public-dir",
        default="public",
        help="Path to local Hugo build output directory.",
    )
    parser.add_argument(
        "--offline-dir",
        default="/home/bky/DEVTMP/opengis_hugo/opengis-offline",
        help="Optional offline mirror root used as preferred content source.",
    )
    parser.add_argument(
        "--output",
        default="reports/sitemap_audit_report.json",
        help="JSON report output path.",
    )
    parser.add_argument(
        "--html-output",
        default="",
        help="Optional standalone HTML viewer output path. Defaults to the JSON output path with a .html suffix.",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=20,
        help="HTTP timeout seconds for fallback remote fetches.",
    )
    parser.add_argument(
        "--similarity-threshold",
        type=float,
        default=0.995,
        help="Threshold below which non-exact text is flagged as mismatch.",
    )
    parser.add_argument(
        "--max-pages",
        type=int,
        default=0,
        help="Optional cap for number of sitemap URLs to audit (0 = all).",
    )
    parser.add_argument(
        "--concurrency",
        type=int,
        default=20,
        help="Max concurrent page audits.",
    )
    parser.add_argument(
        "--apply-aliases",
        action="store_true",
        help="Apply suggested aliases directly to matched content files.",
    )
    parser.add_argument(
        "--build",
        action="store_true",
        help="Run `hugo --destination <public-dir>` before auditing.",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    public_dir = Path(args.public_dir)
    output_path = Path(args.output)
    html_output_path = Path(args.html_output) if args.html_output else derive_html_output_path(output_path)
    offline_dir = Path(args.offline_dir) if args.offline_dir else None

    if args.build:
        maybe_build_hugo(public_dir)

    if not public_dir.exists() or not public_dir.is_dir():
        raise FileNotFoundError(
            f"Local public directory does not exist: {public_dir}. Build with `hugo` or use --build."
        )

    if offline_dir is not None and not offline_dir.exists():
        offline_dir = None

    allowed_domains = {"opengis.ch", "www.opengis.ch"}
    sitemap_urls = collect_sitemap_urls(args.sitemap_url, timeout=args.timeout)

    filtered = [
        url
        for url in sitemap_urls
        if is_allowed_domain(url, allowed_domains) and is_html_page_url(url)
    ]

    if args.max_pages > 0:
        filtered = filtered[: args.max_pages]

    local_by_url, local_by_hash = build_local_page_index(public_dir)
    content_url_index, content_source_index = build_content_indexes(Path("content"))

    results = audit_urls_concurrent(
        urls=filtered,
        public_dir=public_dir,
        timeout=args.timeout,
        similarity_threshold=args.similarity_threshold,
        concurrency=args.concurrency,
        offline_dir=offline_dir,
        local_by_url=local_by_url,
        local_by_hash=local_by_hash,
        content_url_index=content_url_index,
        content_source_index=content_source_index,
    )

    alias_updates: list[dict[str, str]] = []
    if args.apply_aliases:
        alias_updates = apply_alias_updates(results)

    summary = summarize(results)

    report = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "source_sitemap_url": args.sitemap_url,
        "local_public_dir": str(public_dir),
        "offline_dir": str(offline_dir) if offline_dir else None,
        "allowed_domains": sorted(allowed_domains),
        "total_urls_in_sitemap": len(sitemap_urls),
        "total_urls_checked": len(filtered),
        "summary": summary,
        "alias_updates": alias_updates,
        "pages": [asdict(item) for item in results],
    }

    write_report(output_path, report)
    write_html_report(report, json_report_path=output_path, html_output_path=html_output_path)

    print(
        json.dumps(
            {
                "report": str(output_path),
                "html_report": str(html_output_path),
                "total_urls_in_sitemap": len(sitemap_urls),
                "checked": len(filtered),
                "summary": summary,
                "alias_updates": len(alias_updates),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
