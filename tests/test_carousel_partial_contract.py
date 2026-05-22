import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class CarouselPartialContractTests(unittest.TestCase):
    def test_carousel_partial_emits_avif_webp_and_fallback_variants(self) -> None:
        template = (
            REPO_ROOT / "themes/opengis-hugo-theme/layouts/_partials/content/carousel.html"
        ).read_text(encoding="utf-8")

        self.assertIn('Resize "2560x webp"', template)
        self.assertIn('Resize "1280x webp"', template)
        self.assertIn('Resize "320x webp"', template)
        self.assertIn('src="{{ $imageMedium.RelPermalink }}"', template)


if __name__ == "__main__":
    unittest.main()
