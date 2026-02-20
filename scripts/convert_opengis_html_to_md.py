#!/usr/bin/env python3
from __future__ import annotations

import argparse
import html as html_lib
import os
import re
from pathlib import Path

from bs4 import BeautifulSoup
from html2text import HTML2Text


def is_opengis_path(path: Path) -> bool:
    return any(part.endswith("opengis.ch") for part in path.parts)


def yaml_escape(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"')


def extract_metadata(soup: BeautifulSoup) -> dict:
    metadata: dict[str, object] = {}

    title_tag = soup.find("title")
    if title_tag and title_tag.text:
        title = re.sub(r"\s+", " ", title_tag.text).strip()
        if title:
            metadata["title"] = html_lib.unescape(title)

    author_tag = soup.select_one("h4.author .fn")
    if author_tag and author_tag.text:
        metadata["author"] = author_tag.text.strip()

    published_tag = soup.select_one("time.entry-date.published")
    if published_tag and published_tag.has_attr("datetime"):
        metadata["date"] = published_tag["datetime"]

    updated_tag = soup.select_one("time.updated")
    if updated_tag and updated_tag.has_attr("datetime"):
        metadata["lastmod"] = updated_tag["datetime"]

    categories = [
        link.text.strip()
        for link in soup.select(".entry-categories a")
        if link.text and link.text.strip()
    ]
    if categories:
        metadata["categories"] = categories

    tags = [
        link.text.strip()
        for link in soup.select(".entry-tags a")
        if link.text and link.text.strip()
    ]
    if tags:
        metadata["tags"] = tags

    return metadata


def extract_body_html(soup: BeautifulSoup) -> str | None:
    for element in soup(["script", "style", "noscript"]):
        element.decompose()

    selectors = [
        ".entry-content",
        ".main",
        "article",
        "main",
        "#content",
        ".page-content",
        ".post",
        ".content",
    ]
    for selector in selectors:
        node = soup.select_one(selector)
        if node and node.get_text(strip=True):
            return str(node)

    body = soup.body
    if body and body.get_text(strip=True):
        return str(body)
    return None


def build_frontmatter(metadata: dict, source: str) -> str:
    lines = ["---"]
    title = metadata.get("title")
    if title:
        lines.append(f'title: "{yaml_escape(str(title))}"')
    author = metadata.get("author")
    if author:
        lines.append(f'author: "{yaml_escape(str(author))}"')
    date_value = metadata.get("date")
    if date_value:
        lines.append(f'date: "{yaml_escape(str(date_value))}"')
    lastmod = metadata.get("lastmod")
    if lastmod:
        lines.append(f'lastmod: "{yaml_escape(str(lastmod))}"')
    categories = metadata.get("categories")
    if categories:
        lines.append("categories:")
        for category in categories:
            lines.append(f'  - "{yaml_escape(str(category))}"')
    tags = metadata.get("tags")
    if tags:
        lines.append("tags:")
        for tag in tags:
            lines.append(f'  - "{yaml_escape(str(tag))}"')
    lines.append(f'source: "{yaml_escape(source)}"')
    lines.append("---")
    return "\n".join(lines) + "\n\n"


def html_to_md(html_text: str) -> str:
    converter = HTML2Text()
    converter.body_width = 0
    converter.ignore_links = False
    converter.ignore_images = False
    converter.ignore_emphasis = False
    converter.protect_links = True
    converter.single_line_break = True
    converter.ul_item_mark = "-"
    return converter.handle(html_text)


def convert_file(
    src_path: Path,
    dst_path: Path,
    add_frontmatter: bool,
    rel_source: str,
    overwrite: bool,
    full_page: bool,
) -> bool:
    if dst_path.exists() and not overwrite:
        return False
    html_text = src_path.read_text(encoding="utf-8", errors="ignore")
    soup = BeautifulSoup(html_text, "html.parser")
    body_html = html_text if full_page else extract_body_html(soup)
    if not body_html:
        body_html = html_text
    md_text = html_to_md(body_html)
    if add_frontmatter:
        metadata = extract_metadata(soup)
        md_text = build_frontmatter(metadata, rel_source) + md_text
    dst_path.parent.mkdir(parents=True, exist_ok=True)
    dst_path.write_text(md_text, encoding="utf-8")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Convert opengis HTML files to Markdown for Hugo."
    )
    parser.add_argument(
        "--input",
        default="opengis-offline",
        help="Root directory containing the scraped HTML files.",
    )
    parser.add_argument(
        "--output",
        default="converted-md",
        help="Root directory for Markdown output.",
    )
    parser.add_argument(
        "--include-non-opengis",
        action="store_true",
        help="Also convert non-opengis domains under the input root.",
    )
    parser.add_argument(
        "--frontmatter",
        action="store_true",
        help="Add minimal Hugo frontmatter (title + source).",
    )
    parser.add_argument(
        "--full-page",
        action="store_true",
        help="Convert the full HTML page instead of the main content.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing Markdown files.",
    )
    args = parser.parse_args()

    input_root = Path(args.input)
    output_root = Path(args.output)

    if not input_root.exists():
        raise SystemExit(f"Input directory not found: {input_root}")

    html_files = [p for p in input_root.rglob("*.html") if p.is_file()]
    converted = 0
    skipped = 0

    for src_path in html_files:
        if not args.include_non_opengis and not is_opengis_path(src_path):
            continue

        rel_path = src_path.relative_to(input_root)
        rel_source = rel_path.as_posix()
        dst_path = output_root / rel_path
        dst_path = dst_path.with_suffix(".md")

        if convert_file(
            src_path,
            dst_path,
            add_frontmatter=args.frontmatter,
            rel_source=rel_source,
            overwrite=args.overwrite,
            full_page=args.full_page,
        ):
            converted += 1
        else:
            skipped += 1

    print(
        "Conversion complete.",
        f"Converted: {converted}.",
        f"Skipped: {skipped}.",
        f"Output: {output_root}",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
