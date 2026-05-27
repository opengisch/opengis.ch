import subprocess
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class BreadcrumbContractTests(unittest.TestCase):
    def test_custom_development_breadcrumb_skips_empty_pages_ancestor(self) -> None:
        with tempfile.TemporaryDirectory(dir=REPO_ROOT) as tmp_dir:
            destination = Path(tmp_dir) / "public"
            destination_arg = str(destination.relative_to(REPO_ROOT))

            subprocess.run(
                [
                    "hugo",
                    "--environment",
                    "development",
                    "--destination",
                    destination_arg,
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
