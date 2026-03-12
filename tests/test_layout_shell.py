import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class LayoutShellTests(unittest.TestCase):
    def test_base_template_keeps_footer_at_viewport_bottom_on_short_pages(self) -> None:
        base_template = (REPO_ROOT / "themes/qfield-theme-v3/layouts/_default/baseof.html").read_text(encoding="utf-8")

        self.assertIn('class="{{ .Scratch.Get `class` }} d-flex flex-column min-vh-100"', base_template)
        self.assertIn('<div id="content" class="flex-grow-1">', base_template)


if __name__ == "__main__":
    unittest.main()
