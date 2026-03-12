import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class FontStackAlignmentTests(unittest.TestCase):
    def test_site_styles_match_live_opengis_font_stack(self) -> None:
        styles = (REPO_ROOT / "assets/sass/styles.scss").read_text(encoding="utf-8")

        self.assertIn("family=Didact+Gothic", styles)
        self.assertIn("family=Roboto:wght@300;400;500;700", styles)
        self.assertIn('font-family: "Roboto", "Segoe UI", sans-serif;', styles)
        self.assertIn('font-family: "Didact Gothic", "Trebuchet MS", sans-serif;', styles)
        self.assertNotIn('font-family: "Roboto Slab", "Trebuchet MS", serif;', styles)
        self.assertIn("font-weight: 500;", styles)
        self.assertIn("line-height: 1.618;", styles)
        self.assertIn("font-size: 2.625rem;", styles)
        self.assertIn("font-size: 2.3125rem;", styles)
        self.assertIn(".opg-hero-title,", styles)
        self.assertIn(".jumpstart-card__price {", styles)
        self.assertIn("font-weight: 700;", styles)

    def test_theme_styles_do_not_keep_the_old_source_sans_stack(self) -> None:
        styles = (REPO_ROOT / "themes/qfield-theme-v3/assets/sass/styles.scss").read_text(encoding="utf-8")

        self.assertIn("family=Didact+Gothic", styles)
        self.assertIn("family=Roboto:wght@300;400;500;700", styles)
        self.assertIn('font-family: "Roboto", "Segoe UI", sans-serif;', styles)
        self.assertNotIn("Source Sans 3", styles)


if __name__ == "__main__":
    unittest.main()
