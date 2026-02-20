#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import shutil
from pathlib import Path
from urllib.parse import unquote, urlparse
import re


MD_IMAGE_RE = re.compile(r"!\[[^\]]*]\(([^)]+)\)")
HTML_IMG_RE = re.compile(r"<img\b[^>]*\bsrc=(['\"])(.*?)\1", re.IGNORECASE)
WP_PROXY_HOST_RE = re.compile(r"^i[0-9]+\.wp\.com$")


def parse_md_target(raw_target: str) -> str:
    target = raw_target.strip()
    if not target:
        return ""
    if target.startswith("<"):
        end = target.find(">")
        if end > 0:
            return target[1:end].strip()
    return target.split()[0].strip()


def extract_image_urls(text: str) -> list[str]:
    urls: list[str] = []
    for match in MD_IMAGE_RE.finditer(text):
        target = parse_md_target(match.group(1))
        if target:
            urls.append(target)
    for match in HTML_IMG_RE.finditer(text):
        target = match.group(2).strip()
        if target:
            urls.append(target)
    return urls


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as f:
        while True:
            chunk = f.read(1024 * 1024)
            if not chunk:
                break
            digest.update(chunk)
    return digest.hexdigest()


def resolve_source_path(url: str, static_root: Path) -> Path | None:
    parsed = urlparse(url)
    path = unquote(parsed.path or "")
    if not path:
        return None

    candidates: list[Path] = []
    if parsed.scheme in {"http", "https"}:
        host = parsed.netloc.lower()
        if WP_PROXY_HOST_RE.match(host):
            candidates.append(static_root / host / path.lstrip("/"))
        if host in {"www.opengis.ch", "opengis.ch"} and path.startswith("/wp-content/"):
            candidates.append(static_root / path.lstrip("/"))
    elif not parsed.scheme and not parsed.netloc:
        match = re.match(r"^/(i[0-9]+\.wp\.com/.+)$", path)
        if match:
            candidates.append(static_root / match.group(1))
        if path.startswith("/wp-content/"):
            candidates.append(static_root / path.lstrip("/"))

    for candidate in candidates:
        if candidate.is_file():
            return candidate
    return None


def is_localization_candidate(url: str) -> bool:
    parsed = urlparse(url)
    path = parsed.path or ""
    if parsed.scheme in {"http", "https"}:
        host = parsed.netloc.lower()
        if WP_PROXY_HOST_RE.match(host):
            return True
        if host in {"www.opengis.ch", "opengis.ch"} and path.startswith("/wp-content/"):
            return True
        return False
    if not parsed.scheme and not parsed.netloc:
        if re.match(r"^/i[0-9]+\.wp\.com/.+", path):
            return True
        if path.startswith("/wp-content/"):
            return True
    return False


def allocate_dest_path(post_dir: Path, source_path: Path) -> Path:
    base = source_path.name
    destination = post_dir / base
    if not destination.exists():
        return destination

    if file_sha256(destination) == file_sha256(source_path):
        return destination

    stem = source_path.stem
    suffix = source_path.suffix
    counter = 2
    while True:
        candidate = post_dir / f"{stem}-{counter}{suffix}"
        if not candidate.exists():
            return candidate
        if file_sha256(candidate) == file_sha256(source_path):
            return candidate
        counter += 1


def collect_post_dirs(blog_root: Path) -> list[Path]:
    post_dirs: set[Path] = set()
    for path in blog_root.rglob("index*.md"):
        if path.name.startswith("_index"):
            continue
        post_dirs.add(path.parent)
    return sorted(post_dirs)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Copy blog image assets into each post folder and rewrite references."
    )
    parser.add_argument("--blog-root", default="content/blog", help="Blog content root.")
    parser.add_argument("--static-root", default="static", help="Static asset root.")
    parser.add_argument(
        "--missing-report",
        default="missing-blog-image-sources.txt",
        help="Path for unresolved image reference report.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Report changes without writing files.",
    )
    args = parser.parse_args()

    blog_root = Path(args.blog_root)
    static_root = Path(args.static_root)
    report_path = Path(args.missing_report)

    if not blog_root.exists():
        raise SystemExit(f"Blog root not found: {blog_root}")
    if not static_root.exists():
        raise SystemExit(f"Static root not found: {static_root}")

    post_dirs = collect_post_dirs(blog_root)

    copied_files = 0
    changed_markdown_files = 0
    changed_posts = 0
    unresolved: list[tuple[str, str, str]] = []

    for post_dir in post_dirs:
        md_files = sorted(post_dir.glob("index*.md"))
        if not md_files:
            continue

        file_texts: dict[Path, str] = {}
        ordered_urls: list[str] = []
        seen_urls: set[str] = set()
        for md_file in md_files:
            text = md_file.read_text(encoding="utf-8")
            file_texts[md_file] = text
            for url in extract_image_urls(text):
                if url not in seen_urls:
                    seen_urls.add(url)
                    ordered_urls.append(url)

        if not ordered_urls:
            continue

        url_replacements: dict[str, str] = {}
        source_to_dest: dict[Path, Path] = {}
        for url in ordered_urls:
            if not is_localization_candidate(url):
                continue
            source_path = resolve_source_path(url, static_root)
            if source_path is None:
                unresolved.append((post_dir.as_posix(), "missing_source", url))
                continue

            if source_path in source_to_dest:
                dest_path = source_to_dest[source_path]
            else:
                dest_path = allocate_dest_path(post_dir, source_path)
                source_to_dest[source_path] = dest_path
                if not args.dry_run and not dest_path.exists():
                    shutil.copy2(source_path, dest_path)
                    copied_files += 1
                elif args.dry_run and not dest_path.exists():
                    copied_files += 1

            url_replacements[url] = f"./{dest_path.name}"

        post_changed = False
        for md_file, original_text in file_texts.items():
            updated_text = original_text
            for source_url, local_url in url_replacements.items():
                updated_text = updated_text.replace(source_url, local_url)
            if updated_text != original_text:
                post_changed = True
                changed_markdown_files += 1
                if not args.dry_run:
                    md_file.write_text(updated_text, encoding="utf-8")

        if post_changed:
            changed_posts += 1

    report_lines = [f"{post}\t{reason}\t{url}" for post, reason, url in unresolved]
    if not args.dry_run:
        report_path.write_text("\n".join(report_lines) + ("\n" if report_lines else ""), encoding="utf-8")

    print(f"posts_scanned={len(post_dirs)}")
    print(f"posts_changed={changed_posts}")
    print(f"markdown_files_changed={changed_markdown_files}")
    print(f"images_copied={copied_files}")
    print(f"unresolved_image_refs={len(unresolved)}")
    if not args.dry_run:
        print(f"missing_report={report_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
