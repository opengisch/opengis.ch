import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class HomepageClientLogoAltTests(unittest.TestCase):
    def test_homepage_client_logos_have_non_empty_alt_text(self) -> None:
        homepage_data = (REPO_ROOT / "data/homepage.yaml").read_text(encoding="utf-8")
        homepage_layout = (REPO_ROOT / "layouts/index.html").read_text(encoding="utf-8")

        self.assertIn('alt: "SOB"', homepage_data)
        self.assertIn('alt: "swisstopo"', homepage_data)
        self.assertIn('alt: "SIGE client logo"', homepage_data)
        self.assertIn('alt: "Geoformer"', homepage_data)
        self.assertIn('alt: "Pacific Community"', homepage_data)
        self.assertNotIn('alt: ""', homepage_data)
        self.assertIn('<a href="{{ .href | safeURL }}"><img src="{{ .image | safeURL }}" alt="{{ .alt }}"></a>', homepage_layout)


if __name__ == "__main__":
    unittest.main()
