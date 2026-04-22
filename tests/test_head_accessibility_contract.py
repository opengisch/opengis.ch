import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class HeadAccessibilityContractTests(unittest.TestCase):
    def test_base_template_exposes_skip_link_and_hugo_environment(self) -> None:
        base_template = (REPO_ROOT / "themes/opengis-hugo-theme/layouts/baseof.html").read_text(encoding="utf-8")
        styles = (REPO_ROOT / "assets/sass/styles.scss").read_text(encoding="utf-8")

        self.assertIn('<body class="d-flex flex-column min-vh-100{{ if .IsHome }} home-page{{ end }}">', base_template)
        self.assertIn('<main id="content" class="flex-grow-1">', base_template)
        self.assertIn(".skip-link {", styles)
        self.assertIn(".skip-link:focus {", styles)
        self.assertIn(':root[data-bs-theme="dark"] .skip-link {', styles)

    def test_head_partial_uses_local_font_stack_without_scss_import(self) -> None:
        head = (REPO_ROOT / "layouts/partials/head/stylesheet.html").read_text(encoding="utf-8")
        site_styles = (REPO_ROOT / "assets/sass/styles.scss").read_text(encoding="utf-8")
        theme_styles = (REPO_ROOT / "themes/opengis-hugo-theme/assets/sass/styles.scss").read_text(encoding="utf-8")

        self.assertNotIn("fonts.googleapis.com", head)
        self.assertNotIn("fonts.gstatic.com", head)
        self.assertNotIn('@import url("https://fonts.googleapis.com', site_styles)
        self.assertNotIn('@import url("https://fonts.googleapis.com', theme_styles)


if __name__ == "__main__":
    unittest.main()
