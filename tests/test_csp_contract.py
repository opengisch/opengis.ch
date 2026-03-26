import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class CspContractTests(unittest.TestCase):
    def test_csp_only_allows_current_font_providers(self) -> None:
        meta_csp = (
            REPO_ROOT / "themes/qfield-theme-v3/layouts/partials/head/content-security-policy.html"
        ).read_text(encoding="utf-8")
        header_csp = (REPO_ROOT / "themes/qfield-theme-v3/layouts/index.headers").read_text(encoding="utf-8")

        for content in (meta_csp, header_csp):
            self.assertIn("script-src 'self'", content)
            self.assertIn("style-src 'self' 'unsafe-inline' https://fonts.googleapis.com", content)
            self.assertIn("font-src 'self' data: https://fonts.gstatic.com", content)
            self.assertIn("object-src 'none'", content)
            self.assertIn("base-uri 'none'", content)
            self.assertNotIn("cdn.jsdelivr.net", content)
            self.assertNotIn("use.typekit.net", content)
            self.assertNotIn("p.typekit.net", content)


if __name__ == "__main__":
    unittest.main()
