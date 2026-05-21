import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class BootstrapSassBundleTests(unittest.TestCase):
    def test_checked_in_css_contains_bootstrap_without_runtime_sass_pipeline(self) -> None:
        template = (REPO_ROOT / "layouts/partials/head/stylesheet.html").read_text(encoding="utf-8")
        styles = (REPO_ROOT / "assets/css/main.css").read_text(encoding="utf-8")

        self.assertIn("Bootstrap  v5.3.3", styles)
        self.assertIn("--bs-primary", styles)
        self.assertIn(".navbar", styles)
        self.assertNotIn("css.Sass", template)
        self.assertNotIn("sass/main.scss", template)


if __name__ == "__main__":
    unittest.main()
