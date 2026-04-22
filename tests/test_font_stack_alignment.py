import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class FontStackAlignmentTests(unittest.TestCase):
    def test_site_styles_match_restored_local_font_stack(self) -> None:
        styles = (REPO_ROOT / "assets/sass/styles.scss").read_text(encoding="utf-8")
        stylesheet = (REPO_ROOT / "layouts/partials/head/stylesheet.html").read_text(encoding="utf-8")

        self.assertNotIn("fonts.googleapis.com", stylesheet)
        self.assertNotIn("fonts.gstatic.com", stylesheet)
        self.assertIn('font-family: "Avenir Next", "Segoe UI", "Helvetica Neue", sans-serif;', styles)
        self.assertIn('font-family: "Trebuchet MS", "Avenir Next", "Segoe UI", sans-serif;', styles)
        self.assertNotIn('font-family: "Roboto Slab", "Trebuchet MS", serif;', styles)
        self.assertNotIn('font-family: "Roboto", "Segoe UI", sans-serif;', styles)
        self.assertNotIn('font-family: "Didact Gothic", "Trebuchet MS", sans-serif;', styles)
        self.assertIn("font-weight: 500;", styles)
        self.assertIn("line-height: 1.618;", styles)
        self.assertIn("font-size: 2.625rem;", styles)
        self.assertIn("font-size: 2.3125rem;", styles)
        self.assertIn(".opg-hero-title,", styles)
        self.assertIn(".jumpstart-card__price {", styles)
        self.assertIn("font-weight: 700;", styles)

    def test_theme_styles_do_not_keep_the_old_source_sans_stack(self) -> None:
        stylesheet = (REPO_ROOT / "layouts/partials/head/stylesheet.html").read_text(encoding="utf-8")
        theme_styles = (REPO_ROOT / "themes/opengis-hugo-theme/assets/sass/styles.scss").read_text(encoding="utf-8")

        self.assertNotIn("fonts.googleapis.com", stylesheet)
        self.assertEqual(theme_styles, "")
        self.assertNotIn("Source Sans 3", theme_styles)


if __name__ == "__main__":
    unittest.main()
