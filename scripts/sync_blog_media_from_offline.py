#!/usr/bin/env python3
from __future__ import annotations

import argparse
import html
import re
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from bs4 import BeautifulSoup


VIDEO_PROVIDERS = {"videopress", "vimeo", "youtube", "rsi"}


@dataclass(frozen=True)
class VideoEmbed:
    key: str
    provider: str
    src: str
    link: str
    title: str


def split_frontmatter(text: str) -> tuple[list[str], str] | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end == -1:
        return None
    fm_text = text[4:end]
    body = text[end + 5 :]
    return fm_text.splitlines(), body


def join_frontmatter(fm_lines: list[str], body: str) -> str:
    return "---\n" + "\n".join(fm_lines) + "\n---\n" + body


def source_from_frontmatter(fm_lines: list[str]) -> str | None:
    for line in fm_lines:
        m = re.match(r'^\s*source:\s*"([^"]+)"\s*$', line)
        if m:
            return m.group(1).strip()
    return None


def has_feature_image_frontmatter(fm_lines: list[str]) -> bool:
    for line in fm_lines:
        if re.match(r"^\s*image\s*:", line):
            return True
        if re.match(r"^\s*cover\s*:", line):
            return True
    return False


def normalize_iframe_src(raw: str) -> str:
    src = html.unescape(raw.strip())
    if src.startswith("//"):
        return "https:" + src
    return src


def normalize_video_embed(raw_src: str) -> VideoEmbed | None:
    src = normalize_iframe_src(raw_src)
    parsed = urlparse(src)
    host = parsed.netloc.lower()
    path = parsed.path
    query = parse_qs(parsed.query)

    if "videopress.com" in host:
        m = re.match(r"^/embed/([A-Za-z0-9]+)$", path)
        if not m:
            return None
        embed_id = m.group(1)
        canonical_src = f"https://videopress.com/embed/{embed_id}"
        return VideoEmbed(
            key=f"videopress:{embed_id}",
            provider="videopress",
            src=canonical_src,
            link=canonical_src,
            title="VideoPress video",
        )

    if "player.vimeo.com" in host:
        m = re.match(r"^/video/([0-9]+)$", path)
        if not m:
            return None
        embed_id = m.group(1)
        canonical_src = f"https://player.vimeo.com/video/{embed_id}"
        return VideoEmbed(
            key=f"vimeo:{embed_id}",
            provider="vimeo",
            src=canonical_src,
            link=f"https://vimeo.com/{embed_id}",
            title=f"Vimeo video {embed_id}",
        )

    if host.endswith("vimeo.com"):
        m = re.match(r"^/([0-9]+)$", path)
        if not m:
            return None
        embed_id = m.group(1)
        return VideoEmbed(
            key=f"vimeo:{embed_id}",
            provider="vimeo",
            src=f"https://player.vimeo.com/video/{embed_id}",
            link=f"https://vimeo.com/{embed_id}",
            title=f"Vimeo video {embed_id}",
        )

    if host.endswith("youtube.com") and path.startswith("/embed/"):
        video_id = path.split("/embed/", 1)[1].split("/", 1)[0]
        if not video_id:
            return None
        return VideoEmbed(
            key=f"youtube:{video_id}",
            provider="youtube",
            src=f"https://www.youtube.com/embed/{video_id}",
            link=f"https://www.youtube.com/watch?v={video_id}",
            title="YouTube video",
        )

    if host == "youtu.be":
        video_id = path.strip("/").split("/", 1)[0]
        if not video_id:
            return None
        return VideoEmbed(
            key=f"youtube:{video_id}",
            provider="youtube",
            src=f"https://www.youtube.com/embed/{video_id}",
            link=f"https://www.youtube.com/watch?v={video_id}",
            title="YouTube video",
        )

    if host.endswith("rsi.ch") and path == "/play/embed":
        urn = query.get("urn", [""])[0]
        if not urn:
            return None
        canonical_query = parsed.query
        canonical_src = f"https://www.rsi.ch/play/embed?{canonical_query}" if canonical_query else "https://www.rsi.ch/play/embed"
        return VideoEmbed(
            key=f"rsi:{urn}",
            provider="rsi",
            src=canonical_src,
            link=canonical_src,
            title="RSI embedded video",
        )

    return None


def extract_source_embeds(soup: BeautifulSoup) -> list[VideoEmbed]:
    container = (
        soup.select_one(".entry-content")
        or soup.select_one("article")
        or soup.select_one("main")
        or soup.select_one("#content")
        or soup.body
    )
    if container is None:
        return []

    seen: set[str] = set()
    embeds: list[VideoEmbed] = []
    for iframe in container.find_all("iframe"):
        src = iframe.get("src")
        if not src:
            continue
        video = normalize_video_embed(src)
        if video is None:
            continue
        if video.provider not in VIDEO_PROVIDERS:
            continue
        if video.key in seen:
            continue
        seen.add(video.key)
        embeds.append(video)
    return embeds


def extract_local_iframe_keys(markdown_text: str) -> set[str]:
    keys: set[str] = set()
    for match in re.finditer(r"""<iframe[^>]*\bsrc=(["'])(.*?)\1""", markdown_text, re.IGNORECASE):
        video = normalize_video_embed(match.group(2))
        if video:
            keys.add(video.key)
    return keys


def render_embed_block(video: VideoEmbed) -> str:
    return (
        '<div class="blog-embed-video">\n'
        "  <iframe\n"
        f'    src="{video.src}"\n'
        f'    title="{video.title}"\n'
        '    loading="lazy"\n'
        '    allow="autoplay; encrypted-media; picture-in-picture; fullscreen"\n'
        "    allowfullscreen>\n"
        "  </iframe>\n"
        "</div>\n\n"
        f"[{video.link}](<{video.link}>)"
    )


def insert_embed_blocks(body: str, blocks: list[str]) -> str:
    if not blocks:
        return body
    payload = "\n\n".join(blocks)
    related_match = re.search(r"(?m)^### _Related_\s*$", body)
    if related_match:
        start = related_match.start()
        head = body[:start].rstrip()
        tail = body[start:]
        return f"{head}\n\n{payload}\n\n{tail}"
    return body.rstrip() + "\n\n" + payload + "\n"


def normalize_image_path_from_url(url: str, static_root: Path) -> str | None:
    value = html.unescape(url.strip())
    if not value:
        return None
    if value.startswith("//"):
        value = "https:" + value

    parsed = urlparse(value)
    host = parsed.netloc.lower()
    path = parsed.path

    candidates: list[str] = []
    if host and re.match(r"^i[0-9]+\.wp\.com$", host):
        candidates.append(f"/{host}{path}")
    if host in {"www.opengis.ch", "opengis.ch"} and path.startswith("/wp-content/uploads/"):
        candidates.append(f"/i0.wp.com/www.opengis.ch{path}")
        candidates.append(path)
    if not host and path:
        if path.startswith("/i0.wp.com/") or path.startswith("/i1.wp.com/") or path.startswith("/i2.wp.com/"):
            candidates.append(path)
        if path.startswith("/wp-content/uploads/"):
            candidates.append(f"/i0.wp.com/www.opengis.ch{path}")
            candidates.append(path)

    for candidate in candidates:
        candidate_fs = static_root / candidate.lstrip("/")
        if candidate_fs.is_file():
            return candidate
    return None


def extract_source_feature_image(soup: BeautifulSoup, static_root: Path) -> str | None:
    og = soup.select_one('meta[property="og:image"]')
    if og and og.get("content"):
        normalized = normalize_image_path_from_url(og["content"], static_root)
        if normalized:
            return normalized

    container = (
        soup.select_one(".entry-content")
        or soup.select_one("article")
        or soup.select_one("main")
        or soup.select_one("#content")
        or soup.body
    )
    if container:
        img = container.find("img")
        if img and img.get("src"):
            normalized = normalize_image_path_from_url(img["src"], static_root)
            if normalized:
                return normalized
    return None


def add_image_frontmatter(fm_lines: list[str], image_value: str) -> list[str]:
    new_lines = fm_lines[:]
    insert_at = len(new_lines)
    for idx, line in enumerate(new_lines):
        if re.match(r"^\s*source\s*:", line):
            insert_at = idx + 1
            break
    new_lines.insert(insert_at, f'image: "{image_value}"')
    return new_lines


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Sync missing blog media from offline source HTML."
    )
    parser.add_argument(
        "--blog-root",
        default="content/blog",
        help="Path to blog markdown root.",
    )
    parser.add_argument(
        "--offline-root",
        default="/mnt/xtreme/DV/DEVTMP/opengis_hugo/opengis-offline",
        help="Root of offline mirrored source HTML.",
    )
    parser.add_argument(
        "--static-root",
        default="static",
        help="Root of static assets.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Report changes without writing files.",
    )
    args = parser.parse_args()

    blog_root = Path(args.blog_root)
    offline_root = Path(args.offline_root)
    static_root = Path(args.static_root)

    files = sorted(blog_root.rglob("index*.md"))

    scanned = 0
    skipped_no_frontmatter = 0
    skipped_no_source = 0
    skipped_missing_source_file = 0
    changed_files = 0
    files_with_video_changes = 0
    files_with_image_changes = 0
    embeds_inserted = 0
    images_added = 0

    for md_file in files:
        text = md_file.read_text(encoding="utf-8")
        split = split_frontmatter(text)
        scanned += 1
        if split is None:
            skipped_no_frontmatter += 1
            continue
        fm_lines, body = split
        source_rel = source_from_frontmatter(fm_lines)
        if not source_rel:
            skipped_no_source += 1
            continue

        source_path = offline_root / source_rel
        if not source_path.is_file():
            skipped_missing_source_file += 1
            continue

        soup = BeautifulSoup(source_path.read_text(encoding="utf-8", errors="ignore"), "html.parser")

        source_embeds = extract_source_embeds(soup)
        local_keys = extract_local_iframe_keys(body)
        missing_embeds = [embed for embed in source_embeds if embed.key not in local_keys]

        new_body = body
        if missing_embeds:
            blocks = [render_embed_block(embed) for embed in missing_embeds]
            new_body = insert_embed_blocks(new_body, blocks)

        new_fm_lines = fm_lines
        added_image = False
        if not has_feature_image_frontmatter(fm_lines):
            feature_image = extract_source_feature_image(soup, static_root)
            if feature_image:
                new_fm_lines = add_image_frontmatter(new_fm_lines, feature_image)
                added_image = True

        new_text = join_frontmatter(new_fm_lines, new_body)
        if new_text != text:
            if not args.dry_run:
                md_file.write_text(new_text, encoding="utf-8")
            changed_files += 1
            if missing_embeds:
                files_with_video_changes += 1
                embeds_inserted += len(missing_embeds)
            if added_image:
                files_with_image_changes += 1
                images_added += 1

    print(f"scanned={scanned}")
    print(f"changed_files={changed_files}")
    print(f"files_with_video_changes={files_with_video_changes}")
    print(f"embeds_inserted={embeds_inserted}")
    print(f"files_with_image_changes={files_with_image_changes}")
    print(f"images_added={images_added}")
    print(f"skipped_no_frontmatter={skipped_no_frontmatter}")
    print(f"skipped_no_source={skipped_no_source}")
    print(f"skipped_missing_source_file={skipped_missing_source_file}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
