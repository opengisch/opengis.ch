import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class ServiceQuoteWidthTests(unittest.TestCase):
    def test_site_styles_keep_service_quotes_full_width(self) -> None:
        styles = (REPO_ROOT / "assets/sass/styles.scss").read_text(encoding="utf-8")

        for selector in (".custom-dev-quote", ".support-quote", ".sustain-quote"):
            match = re.search(rf"{re.escape(selector)}\s*\{{(?P<body>.*?)\n\}}", styles, re.DOTALL)
            self.assertIsNotNone(match, f"Missing selector {selector} in site styles")
            body = match.group("body")
            self.assertIn("width: 100%;", body)
            self.assertIn("max-width: none;", body)
            self.assertIn("box-sizing: border-box;", body)
            self.assertNotIn("width: 80%;", body)
            self.assertNotIn("max-width: 980px;", body)

    def test_theme_styles_keep_service_quotes_full_width(self) -> None:
        styles = (REPO_ROOT / "themes/qfield-theme-v3/assets/sass/styles.scss").read_text(encoding="utf-8")

        for selector in (".custom-dev-quote", ".support-quote"):
            match = re.search(rf"{re.escape(selector)}\s*\{{(?P<body>.*?)\n\}}", styles, re.DOTALL)
            self.assertIsNotNone(match, f"Missing selector {selector} in theme styles")
            body = match.group("body")
            self.assertIn("width: 100%;", body)
            self.assertIn("max-width: none;", body)
            self.assertIn("box-sizing: border-box;", body)
            self.assertNotIn("width: 80%;", body)
            self.assertNotIn("max-width: 980px;", body)


if __name__ == "__main__":
    unittest.main()
