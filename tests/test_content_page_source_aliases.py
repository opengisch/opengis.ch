import re
import unittest
from pathlib import Path

from scripts import sitemap_content_audit as audit


REPO_ROOT = Path(__file__).resolve().parents[1]
CONTENT_PAGES = REPO_ROOT / "content/pages"


def _extract_aliases(markdown_text: str) -> set[str]:
    lines = markdown_text.splitlines()
    if len(lines) < 3 or lines[0].strip() != "---":
        return set()

    fm_end = None
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            fm_end = idx
            break

    if fm_end is None:
        return set()

    fm_lines = lines[1:fm_end]
    aliases: list[str] = []

    for idx, line in enumerate(fm_lines):
        match = re.match(r"^\s*aliases:\s*(.*)$", line)
        if not match:
            continue

        remainder = match.group(1).strip()
        if remainder and remainder != "[]":
            if remainder.startswith("[") and remainder.endswith("]"):
                aliases.extend(audit.parse_alias_items(remainder[1:-1].split(",")))
            else:
                aliases.extend(audit.parse_alias_items([remainder]))

        scan = idx + 1
        while scan < len(fm_lines):
            item_match = re.match(r"^\s*-\s*(.+?)\s*$", fm_lines[scan])
            if not item_match:
                break
            aliases.extend(audit.parse_alias_items([item_match.group(1)]))
            scan += 1
        break

    return set(aliases)


class ContentPageSourceAliasTests(unittest.TestCase):
    def test_content_page_frontmatter_uses_valid_delimiter(self) -> None:
        invalid = []

        for markdown_file in sorted(CONTENT_PAGES.rglob("index*.md")):
            first_line = markdown_file.read_text(encoding="utf-8").splitlines()[0]
            if first_line.strip() != "---":
                invalid.append(str(markdown_file.relative_to(REPO_ROOT)))

        self.assertEqual(invalid, [])

    def test_all_content_pages_preserve_source_routes_as_aliases(self) -> None:
        missing_aliases: list[str] = []

        for markdown_file in sorted(CONTENT_PAGES.rglob("index*.md")):
            markdown_text = markdown_file.read_text(encoding="utf-8")
            fields = audit.parse_frontmatter_fields(markdown_text)
            source_value = fields.get("source")
            if not source_value:
                continue

            source_path = audit.normalize_source_path(source_value)
            aliases = _extract_aliases(markdown_text)

            if source_path not in aliases:
                missing_aliases.append(f"{markdown_file.relative_to(REPO_ROOT)} -> missing {source_path}")

        self.assertEqual(missing_aliases, [])


if __name__ == "__main__":
    unittest.main()
