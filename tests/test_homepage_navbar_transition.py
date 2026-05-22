import subprocess
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class HomepageNavbarTransitionTests(unittest.TestCase):
    def test_homepage_renders_scroll_aware_hero_navbar(self) -> None:
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

        self.assertIn('class="navbar navbar-expand-lg navbar-default navbar-color-on-scroll navbar-transparent hestia_left shadow-sm fixed-top og-navbar og-navbar-home"', html)
        self.assertIn('data-home-hero-nav="true"', html)
        self.assertIn('data-scroll-threshold="32"', html)

    def test_scroll_script_and_styles_include_homepage_transition_rules(self) -> None:
        script = (REPO_ROOT / "assets/js/main.js").read_text(encoding="utf-8")
        styles = (REPO_ROOT / "assets/sass/styles.scss").read_text(encoding="utf-8")

        self.assertIn("navbar.dataset.homeHeroNav === 'true'", script)
        self.assertIn("navbar.dataset.scrollThreshold", script)
        self.assertIn("document.documentElement.scrollHeight <= window.innerHeight + 1", script)
        self.assertIn("const shouldUseCompactNavbarAtRest = () => {", script)
        self.assertIn("updateNavbarOffset()", script)
        self.assertIn(".navbar-default.og-navbar-home:not(.scrolled)", styles)
        self.assertIn(".og-navbar.og-navbar-home:not(.scrolled)", styles)
        self.assertIn(".navbar-default.navbar-transparent.scrolled", styles)
        self.assertIn(".navbar-default.og-navbar-home:not(.scrolled) .navbar-nav > .nav-item > .nav-link", styles)
        self.assertIn(".navbar-default.og-navbar-home:not(.scrolled) .dropdown-menu .dropdown-item", styles)
        self.assertIn(".navbar-default.og-navbar-home.scrolled", styles)
        self.assertIn(".navbar-default.scrolled {", styles)
        self.assertIn(".navbar-default.scrolled .navbar-logo", styles)
        self.assertIn(".navbar-default.scrolled .navbar-brand,", styles)
        self.assertIn(':root[data-bs-theme="dark"] .navbar-default.og-navbar-home:not(.scrolled)', styles)
        self.assertIn("background: transparent;", styles)
        self.assertIn("background-color: transparent;", styles)
        self.assertIn("font-weight: 500;", styles)


if __name__ == "__main__":
    unittest.main()
