import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class NavbarDropdownLayoutTests(unittest.TestCase):
    def test_navbar_dropdown_styles_cover_collapsed_lg_breakpoint(self) -> None:
        styles = (REPO_ROOT / "assets/sass/styles.scss").read_text(encoding="utf-8")
        header = (REPO_ROOT / "layouts/partials/header/header.html").read_text(encoding="utf-8")

        self.assertIn("@media (max-width: 991.98px)", styles)
        self.assertIn(".navbar-default .dropdown-menu {\n    position: static;", styles)
        self.assertIn('class="dropdown-submenu"', header)
        self.assertIn('class="dropdown-item dropdown-toggle{{ if $childActive }} active{{ end }}"', header)
        self.assertIn(".navbar-default .dropdown-item-icon", styles)
        self.assertIn(".navbar-default .dropdown-submenu > .dropdown-toggle::after", styles)
        self.assertIn("border-left: 1px solid rgba(60, 72, 88, 0.12);", styles)
        self.assertIn("font-weight: 400;", styles)
        self.assertIn("font-size: 0.78rem;", styles)
        self.assertIn("font-size: 0.85rem;", styles)
        self.assertIn("letter-spacing: 0.03em;", styles)


if __name__ == "__main__":
    unittest.main()
