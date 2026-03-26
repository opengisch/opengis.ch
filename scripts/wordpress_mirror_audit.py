#!/usr/bin/env python3
"""Audit WordPress-style mirrored static roots against source references."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path


MIRROR_ROOTS = (
    "i0.wp.com",
    "i1.wp.com",
    "wp-content",
    "wp-json",
    "slides.opengis.ch",
    "usabilityhub.opengis.ch",
)
SOURCE_DIRS = ("content", "layouts", "themes", "data", "config")
TEXT_EXTENSIONS = {
    ".css",
    ".html",
    ".js",
    ".json",
    ".md",
    ".scss",
    ".toml",
    ".txt",
    ".xml",
    ".yaml",
    ".yml",
}


@dataclass(frozen=True)
class MirrorFile:
    root: str
    path: str
    size_bytes: int


REFERENCE_RE = re.compile(
    r"(?P<path>/(?:i0\.wp\.com|i1\.wp\.com|wp-content|wp-json|slides\.opengis\.ch|usabilityhub\.opengis\.ch)/[^\s\"')>]+)"
)


def iter_source_files(repo_root: Path) -> list[Path]:
    files: list[Path] = []
    for source_dir in SOURCE_DIRS:
        root = repo_root / source_dir
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if path.is_file() and path.suffix.lower() in TEXT_EXTENSIONS:
                files.append(path)
    return sorted(files)


def collect_mirror_files(static_root: Path) -> list[MirrorFile]:
    mirror_files: list[MirrorFile] = []
    for root_name in MIRROR_ROOTS:
        mirror_root = static_root / root_name
        if not mirror_root.exists():
            continue
        for path in sorted(p for p in mirror_root.rglob("*") if p.is_file()):
            mirror_files.append(
                MirrorFile(
                    root=root_name,
                    path="/" + path.relative_to(static_root).as_posix(),
                    size_bytes=path.stat().st_size,
                )
            )
    return mirror_files


def collect_references(repo_root: Path) -> dict[str, list[str]]:
    references: dict[str, list[str]] = defaultdict(list)
    for source_file in iter_source_files(repo_root):
        text = source_file.read_text(encoding="utf-8")
        for match in REFERENCE_RE.finditer(text):
            raw_path = match.group("path")
            normalized_path = raw_path.split("?", 1)[0]
            references[normalized_path].append(str(source_file.relative_to(repo_root)))
    return references


def audit_mirrors(repo_root: Path) -> dict[str, object]:
    static_root = repo_root / "static"
    mirror_files = collect_mirror_files(static_root)
    references = collect_references(repo_root)

    referenced_files: list[dict[str, object]] = []
    unreferenced_files: list[dict[str, object]] = []
    root_totals = Counter()
    root_referenced = Counter()
    root_sizes = Counter()

    for mirror_file in mirror_files:
        root_totals[mirror_file.root] += 1
        root_sizes[mirror_file.root] += mirror_file.size_bytes
        reference_sources = references.get(mirror_file.path, [])
        record = {
            "root": mirror_file.root,
            "path": mirror_file.path,
            "size_bytes": mirror_file.size_bytes,
            "reference_count": len(reference_sources),
        }
        if reference_sources:
            root_referenced[mirror_file.root] += 1
            record["sources"] = reference_sources
            referenced_files.append(record)
        else:
            unreferenced_files.append(record)

    root_summary = []
    for root_name in MIRROR_ROOTS:
        if root_totals[root_name] == 0:
            continue
        root_summary.append(
            {
                "root": root_name,
                "file_count": root_totals[root_name],
                "referenced_file_count": root_referenced[root_name],
                "unreferenced_file_count": root_totals[root_name] - root_referenced[root_name],
                "size_bytes": root_sizes[root_name],
            }
        )

    root_summary.sort(key=lambda item: item["root"])
    unreferenced_files.sort(key=lambda item: item["path"])
    referenced_files.sort(key=lambda item: item["path"])

    return {
        "summary": {
            "mirror_root_count": len(root_summary),
            "mirror_file_count": len(mirror_files),
            "referenced_file_count": len(referenced_files),
            "unreferenced_file_count": len(unreferenced_files),
        },
        "roots": root_summary,
        "referenced_files": referenced_files,
        "unreferenced_files": unreferenced_files,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Repository root to audit",
    )
    parser.add_argument(
        "--output",
        type=Path,
        required=True,
        help="JSON output path for the audit report",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    report = audit_mirrors(args.repo_root)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        f"Wrote WordPress mirror audit to {args.output} "
        f"with {report['summary']['unreferenced_file_count']} unreferenced mirrored files."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
