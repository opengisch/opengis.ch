#!/usr/bin/env python3
"""Audit built site HTML for image alt-text coverage and obvious weak labels."""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlparse

WHITESPACE_RE = re.compile(r"\s+")
SEPARATOR_RE = re.compile(r"[-_]+")
GENERIC_ALT_VALUES = {
    "image",
    "photo",
    "picture",
    "graphic",
    "illustration",
    "icon",
    "img",
}


class ImageTagParser(HTMLParser):
    """Collect rendered <img> tags with source positions."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.images: list[dict[str, object]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() != "img":
            return

        attr_map = {name.lower(): (value or "") for name, value in attrs}
        line, column = self.getpos()
        self.images.append(
            {
                "line": line,
                "column": column + 1,
                "attrs": attr_map,
            }
        )


def normalize_whitespace(value: str) -> str:
    return WHITESPACE_RE.sub(" ", value).strip()


def normalize_for_match(value: str) -> str:
    return normalize_whitespace(value).casefold()


def normalize_filename_stem(src: str) -> str:
    path = urlparse(src).path
    stem = PurePosixPath(unquote(path)).stem
    return normalize_for_match(SEPARATOR_RE.sub(" ", stem))


def is_probably_decorative(attrs: dict[str, str]) -> bool:
    role = attrs.get("role", "").strip().lower()
    if role in {"presentation", "none"}:
        return True

    if attrs.get("aria-hidden", "").strip().lower() == "true":
        return True

    if "hidden" in attrs:
        return True

    width = attrs.get("width", "").strip()
    height = attrs.get("height", "").strip()
    if width == "1" and height == "1":
        return True

    classes = normalize_for_match(attrs.get("class", ""))
    if "pixel" in classes:
        return True

    src = attrs.get("src", "").lower()
    if "pixel.gif" in src:
        return True

    style = attrs.get("style", "").replace(" ", "").lower()
    if "display:none" in style or "visibility:hidden" in style:
        return True

    return False


def classify_image(attrs: dict[str, str]) -> tuple[str, int, str] | None:
    src = attrs.get("src", "")

    if "alt" not in attrs:
        return ("missing_alt", 3, "Image tag is missing an alt attribute.")

    alt = normalize_whitespace(attrs.get("alt", ""))
    if not alt:
        if is_probably_decorative(attrs):
            return None
        return (
            "empty_alt_review",
            2,
            "Image has an empty alt attribute but is not marked decorative.",
        )

    normalized_alt = normalize_for_match(alt)
    if normalized_alt in GENERIC_ALT_VALUES:
        return ("generic_alt_review", 1, "Alt text is too generic to describe the image.")

    if normalized_alt == normalize_filename_stem(src):
        return ("generic_alt_review", 1, "Alt text only repeats the image file name.")

    if normalized_alt.endswith(" icon"):
        return (
            "generic_alt_review",
            1,
            "Alt text ends with 'icon' instead of describing the image content.",
        )

    return None


def audit_image_alts(public_dir: Path) -> dict[str, object]:
    findings: list[dict[str, object]] = []
    images_scanned = 0
    decorative_images = 0

    for html_file in sorted(public_dir.rglob("*.html")):
        parser = ImageTagParser()
        parser.feed(html_file.read_text(encoding="utf-8", errors="replace"))
        parser.close()

        source_file = html_file.relative_to(public_dir).as_posix()

        for image in parser.images:
            images_scanned += 1
            attrs = image["attrs"]
            assert isinstance(attrs, dict)

            finding = classify_image(attrs)
            if finding is None:
                if "alt" in attrs and not normalize_whitespace(attrs.get("alt", "")) and is_probably_decorative(attrs):
                    decorative_images += 1
                continue

            kind, severity, reason = finding
            findings.append(
                {
                    "kind": kind,
                    "severity": severity,
                    "reason": reason,
                    "source_file": source_file,
                    "line": image["line"],
                    "column": image["column"],
                    "src": attrs.get("src", ""),
                    "alt": normalize_whitespace(attrs.get("alt", "")),
                    "search_text": " ".join(
                        (
                            kind,
                            source_file,
                            attrs.get("src", ""),
                            normalize_whitespace(attrs.get("alt", "")),
                            reason,
                        )
                    ).lower(),
                }
            )

    finding_counts = Counter(finding["kind"] for finding in findings)

    return {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "public_dir": str(public_dir),
        "summary": {
            "scanned_html_files": len(list(public_dir.rglob("*.html"))),
            "images_scanned": images_scanned,
            "decorative_images": decorative_images,
            "finding_count": len(findings),
            "missing_alt_count": finding_counts["missing_alt"],
            "empty_alt_review_count": finding_counts["empty_alt_review"],
            "generic_alt_review_count": finding_counts["generic_alt_review"],
        },
        "findings": findings,
    }


def derive_csv_output_path(json_report_path: Path) -> Path:
    return json_report_path.with_suffix(".csv") if json_report_path.suffix.lower() == ".json" else Path(
        f"{json_report_path}.csv"
    )


def write_json_report(output_path: Path, report: dict[str, object]) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(report, indent=2, ensure_ascii=True), encoding="utf-8")


def write_csv_report(output_path: Path, report: dict[str, object]) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "severity",
                "kind",
                "source_file",
                "line",
                "column",
                "src",
                "alt",
                "reason",
            ],
        )
        writer.writeheader()
        for finding in report["findings"]:
            writer.writerow(
                {
                    "severity": finding["severity"],
                    "kind": finding["kind"],
                    "source_file": finding["source_file"],
                    "line": finding["line"],
                    "column": finding["column"],
                    "src": finding["src"],
                    "alt": finding["alt"],
                    "reason": finding["reason"],
                }
            )


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Audit built Hugo HTML for image alt-text coverage and weak labels."
    )
    parser.add_argument(
        "--public-dir",
        default="public",
        help="Path to built Hugo output.",
    )
    parser.add_argument(
        "--output",
        default="reports/image_alt_audit_report.json",
        help="JSON report output path.",
    )
    parser.add_argument(
        "--csv-output",
        default="",
        help="Optional CSV report output path. Defaults to the JSON output path with a .csv suffix.",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    public_dir = Path(args.public_dir)
    output_path = Path(args.output)
    csv_output_path = Path(args.csv_output) if args.csv_output else derive_csv_output_path(output_path)

    if not public_dir.exists() or not public_dir.is_dir():
        raise FileNotFoundError(f"Public directory not found: {public_dir}")

    report = audit_image_alts(public_dir)
    write_json_report(output_path, report)
    write_csv_report(csv_output_path, report)

    print(
        json.dumps(
            {
                "report": str(output_path),
                "csv_report": str(csv_output_path),
                "summary": report["summary"],
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
