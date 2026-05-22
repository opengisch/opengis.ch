import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class PartialParameterDocsTests(unittest.TestCase):
    def test_shared_parameterized_partials_document_their_contracts(self) -> None:
        documented_partials = {
            "layouts/partials/image.html": [
                "Image Partial",
                'partial "image.html"',
                'Parameters:',
                '- "src" string, required',
                '- "sizes" string, optional',
            ],
            "layouts/partials/page-card-image.html": [
                "Page Card Image Partial",
                'partial "page-card-image.html"',
                'Parameters:',
                '- "page" page, required',
                'Returns:',
            ],
            "themes/opengis-hugo-theme/layouts/_partials/content/carousel.html": [
                "Bootstrap Carousel",
                'partial "carousel.html"',
                'Parameters:',
                '- "imagesPattern" to pass to resources.Match',
                '- "withControls" boolean',
            ],
            "layouts/partials/assistance/service-card.html": [
                "Service Card Partial",
                'partial "assistance/service-card.html"',
                'Parameters:',
                '- "service" map, required',
                '- "context" page, optional',
            ],
        }

        for relative_path, snippets in documented_partials.items():
            with self.subTest(partial=relative_path):
                content = (REPO_ROOT / relative_path).read_text(encoding="utf-8")
                for snippet in snippets:
                    self.assertIn(snippet, content)


if __name__ == "__main__":
    unittest.main()
