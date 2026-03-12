import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class GeoNinjasCardTests(unittest.TestCase):
    def test_homepage_and_shortcode_use_reveal_enabled_card_markup(self) -> None:
        homepage = (REPO_ROOT / "layouts/index.html").read_text(encoding="utf-8")
        shortcode = (REPO_ROOT / "themes/qfield-theme-v3/layouts/shortcodes/geoninjas.html").read_text(encoding="utf-8")

        self.assertIn('data-reveal="fade-left"', homepage)
        self.assertIn('data-reveal-delay="{{ mul $index 70 }}"', homepage)
        self.assertIn('class="team-card__media"', homepage)
        self.assertIn('data-reveal="fade-left"', shortcode)
        self.assertIn('data-reveal-delay="{{ mul $index 70 }}"', shortcode)
        self.assertIn('class="team-card__media"', shortcode)

    def test_scroll_reveal_logic_and_card_styles_exist(self) -> None:
        script = (REPO_ROOT / "themes/qfield-theme-v3/assets/js/main.js").read_text(encoding="utf-8")
        styles = (REPO_ROOT / "assets/sass/styles.scss").read_text(encoding="utf-8")

        self.assertIn('querySelectorAll(\'[data-reveal="fade-left"]\')', script)
        self.assertIn("new IntersectionObserver", script)
        self.assertIn("item.style.setProperty('--reveal-delay'", script)
        self.assertIn(".team-card.is-visible", styles)
        self.assertIn("transform: translate3d(-44px, 0, 0);", styles)
        self.assertIn(".team-card__media", styles)
        self.assertIn("@media (prefers-reduced-motion: reduce)", styles)


if __name__ == "__main__":
    unittest.main()
