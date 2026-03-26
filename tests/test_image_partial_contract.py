import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class ImagePartialContractTests(unittest.TestCase):
    def test_image_partial_default_sizes_match_generated_widths(self) -> None:
        template = (REPO_ROOT / "themes/qfield-theme-v3/layouts/partials/image.html").read_text(encoding="utf-8")

        self.assertIn('{{- $widths := .widths | default (slice 400 640 960 1280 1600) -}}', template)
        self.assertIn(
            '{{- $sizes := .sizes | default "(max-width: 400px) 400px, (max-width: 640px) 640px, (max-width: 960px) 960px, (max-width: 1280px) 1280px, 1600px" -}}',
            template,
        )
        self.assertNotIn('{{- $sizes := .sizes | default "640,960,1280" -}}', template)

    def test_image_partial_supports_page_resources_and_modern_formats(self) -> None:
        template = (REPO_ROOT / "themes/qfield-theme-v3/layouts/partials/image.html").read_text(encoding="utf-8")

        self.assertIn('{{- $page := .page -}}', template)
        self.assertIn('{{- $resource := .resource | default nil -}}', template)
        self.assertIn('{{- with $page.Resources.GetMatch $src -}}', template)
        self.assertIn('type="image/avif"', template)
        self.assertIn('{{- $processedAVIF := slice -}}', template)
        self.assertIn('{{- $processedAVIF = $processedAVIF | append ($resource.Resize (printf "%dx avif" .)) -}}', template)
        self.assertIn('type="image/webp"', template)
        self.assertIn('{{- $processedWebP = $processedWebP | append ($resource.Resize (printf "%dx webp" .)) -}}', template)
        self.assertIn('style="{{ . | safeCSS }}"', template)


if __name__ == "__main__":
    unittest.main()
