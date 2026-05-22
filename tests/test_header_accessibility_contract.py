import subprocess
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class HeaderAccessibilityContractTests(unittest.TestCase):
    def test_header_template_uses_accessible_controls(self) -> None:
        template = (REPO_ROOT / "layouts/partials/header/header.html").read_text(encoding="utf-8")
        dark_mode = (REPO_ROOT / "assets/js/dark-mode.js").read_text(encoding="utf-8")

        self.assertIn('class="navbar-brand d-flex align-items-center"', template)
        self.assertIn('aria-label="{{ .Site.Title }} home"', template)
        self.assertIn('href="{{ .URL | relLangURL }}"{{ if $active }} aria-current="page"{{ end }}', template)
        self.assertIn('href="{{ .URL | relLangURL }}"{{ if $grandActive }} aria-current="page"{{ end }}', template)
        self.assertIn('href="{{ .URL | relLangURL }}"{{ if $childActive }} aria-current="page"{{ end }}', template)
        self.assertIn('class="dropdown-submenu"', template)
        self.assertIn('class="nav-link dropdown-toggle btn btn-link"', template)
        self.assertIn('id="navbarLanguageDropdown"', template)
        self.assertIn('aria-label="Change language"', template)
        self.assertIn('id="themeToggle"', template)
        self.assertIn('aria-pressed="false"', template)
        self.assertNotIn('aria-current="true"', template)
        self.assertIn("function syncThemeToggleState(theme) {", dark_mode)
        self.assertIn("btn.setAttribute('aria-pressed', isDark ? 'true' : 'false');", dark_mode)
        self.assertIn("btn.setAttribute('aria-label', isDark ? 'Switch to light theme' : 'Switch to dark theme');", dark_mode)

    def test_homepage_renders_accessible_header_controls(self) -> None:
        with tempfile.TemporaryDirectory(dir=REPO_ROOT) as tmp_dir:
            destination = Path(tmp_dir) / "public"
            destination_arg = str(destination.relative_to(REPO_ROOT))

            subprocess.run(
                [
                    "hugo",
                    "--environment",
                    "development",
                    "--destination",
                    destination_arg,
                ],
                check=True,
                cwd=REPO_ROOT,
                capture_output=True,
                text=True,
            )

            html = (destination / "index.html").read_text(encoding="utf-8")

        self.assertIn('aria-label="OPENGIS.ch home"', html)
        self.assertIn('id="navbarLanguageDropdown"', html)
        self.assertIn('type="button"', html)
        self.assertIn('aria-label="Change language"', html)
        self.assertIn('id="themeToggle"', html)
        self.assertIn('aria-pressed="false"', html)


if __name__ == "__main__":
    unittest.main()
