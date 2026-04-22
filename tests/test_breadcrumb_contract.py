import subprocess
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class BreadcrumbContractTests(unittest.TestCase):
    def test_custom_development_breadcrumb_skips_empty_pages_ancestor(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            destination = Path(tmp_dir) / "public"

            subprocess.run(
                [
                    "hugo",
                    "--environment",
                    "development",
                    "--destination",
                    str(destination),
                ],
                check=True,
                cwd=REPO_ROOT,
                capture_output=True,
                text=True,
            )

            html = (destination / "custom-development/index.html").read_text(encoding="utf-8")

        self.assertIn('<nav class="header-breadcrumb" aria-label="breadcrumb">', html)
        self.assertIn('<a href="/">Home</a>', html)
        self.assertIn('<li class="breadcrumb-item active" aria-current="page">Custom Development</li>', html)
        self.assertNotIn('<a href="/pages/"></a>', html)


if __name__ == "__main__":
    unittest.main()
