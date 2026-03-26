import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class HeadAccessibilityContractTests(unittest.TestCase):
    def test_base_template_exposes_skip_link_and_hugo_environment(self) -> None:
        base_template = (REPO_ROOT / "themes/qfield-theme-v3/layouts/_default/baseof.html").read_text(encoding="utf-8")
        styles = (REPO_ROOT / "assets/sass/styles.scss").read_text(encoding="utf-8")

        self.assertIn('data-hugo-environment="{{ hugo.Environment }}"', base_template)
        self.assertIn('<a class="skip-link" href="#content">Skip to main content</a>', base_template)
        self.assertIn(".skip-link {", styles)
        self.assertIn(".skip-link:focus {", styles)
        self.assertIn(':root[data-bs-theme="dark"] .skip-link {', styles)

    def test_head_partial_loads_fonts_via_resource_hints_instead_of_scss_import(self) -> None:
        head = (REPO_ROOT / "themes/qfield-theme-v3/layouts/partials/head/head.html").read_text(encoding="utf-8")
        site_styles = (REPO_ROOT / "assets/sass/styles.scss").read_text(encoding="utf-8")
        theme_styles = (REPO_ROOT / "themes/qfield-theme-v3/assets/sass/styles.scss").read_text(encoding="utf-8")

        self.assertIn('rel="dns-prefetch" href="//fonts.googleapis.com"', head)
        self.assertIn('rel="dns-prefetch" href="//fonts.gstatic.com"', head)
        self.assertIn('rel="preconnect" href="https://fonts.googleapis.com"', head)
        self.assertIn('rel="preconnect" href="https://fonts.gstatic.com" crossorigin', head)
        self.assertIn('rel="preload" href="{{ $googleFontsHref }}" as="style"', head)
        self.assertIn(
            '{{- $googleFontsHref := "https://fonts.googleapis.com/css2?family=Didact+Gothic&family=Roboto:wght@300;400;500;700&display=swap" -}}',
            head,
        )
        self.assertIn('rel="stylesheet" href="{{ $googleFontsHref }}"', head)
        self.assertIn('rel="dns-prefetch" href="//www.googletagmanager.com"', head)
        self.assertIn('rel="preconnect" href="https://www.googletagmanager.com"', head)
        self.assertNotIn('@import url("https://fonts.googleapis.com', site_styles)
        self.assertNotIn('@import url("https://fonts.googleapis.com', theme_styles)


if __name__ == "__main__":
    unittest.main()
