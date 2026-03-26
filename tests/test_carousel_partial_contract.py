import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class CarouselPartialContractTests(unittest.TestCase):
    def test_carousel_partial_emits_avif_webp_and_fallback_variants(self) -> None:
        template = (
            REPO_ROOT / "themes/qfield-theme-v3/layouts/partials/content/carousel.html"
        ).read_text(encoding="utf-8")

        self.assertIn("AVIF/WebP variants with original-format fallbacks", template)
        self.assertIn('type="image/avif"', template)
        self.assertIn('type="image/webp"', template)
        self.assertIn('{{ $imageAvifMedium := $image.Resize "1280x avif" -}}', template)
        self.assertIn('{{ $imageWebpMedium := $image.Resize "1280x webp" -}}', template)
        self.assertIn('{{ $imageDefaultMedium := $image.Resize "1280x" -}}', template)
        self.assertIn('src="{{ $imageDefaultMedium.RelPermalink }}"', template)


if __name__ == "__main__":
    unittest.main()
