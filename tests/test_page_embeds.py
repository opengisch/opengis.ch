import subprocess
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
NEWSLETTER_FORM_URL = (
    "https://b678e710.sibforms.com/serve/"
    "MUIFAFWN7NQpnKtkx7xYf7I5Gxg5yJYMJsu5Ea-ijgiin3-L4VaO4ONZ3rLG8CUV8k6qK5n5vyugpzwPZhIznS2hRFxHhCRCey6qM08P9Cr0uevwXIB5vWqq1NMNiTPxw9IsJLLl6DDY8NnCGGmYC17LSQzcbnSBXp0DlQHFQGKSKr45y_x-qYqd0SD6B-bEjORYanlhZRNvTHEv"
)
CROWDFUNDING_CHART_URL = (
    "https://docs.google.com/spreadsheets/d/e/2PACX-1vSQUZgZV6MYLKxjYwshhudga3VP-mIT_9sTyGfaNQ7PUcywszPXC9VmCIV9BOZGKEQ5QN1FEsSVsXNa/"
    "pubchart?oid=1555133790&amp;format=interactive"
)


class PageEmbedTests(unittest.TestCase):
    def test_newsletter_pages_render_legacy_signup_form(self) -> None:
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

            for relative_path in (
                "newsletter/index.html",
                "de/newsletter/index.html",
                "fr/newsletter/index.html",
                "it/newsletter/index.html",
            ):
                html = (destination / relative_path).read_text(encoding="utf-8")
                self.assertIn('class="page-inline-embed__iframe newsletter-signup-iframe"', html)
                self.assertIn(NEWSLETTER_FORM_URL, html)

    def test_crowdfunding_pages_render_legacy_progress_chart(self) -> None:
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

            for relative_path in (
                "crowdfunding-erweiterte-unterstutzung-fur-kreisbogen-in-qgis/index.html",
                "de/crowdfunding-erweiterte-unterstutzung-fur-kreisbogen-in-qgis/index.html",
                "it/crowdfunding-erweiterte-unterstutzung-fur-kreisbogen-in-qgis/index.html",
            ):
                html = (destination / relative_path).read_text(encoding="utf-8")
                self.assertIn('class="page-inline-embed__iframe crowdfunding-progress-iframe"', html)
                self.assertIn(CROWDFUNDING_CHART_URL, html)


if __name__ == "__main__":
    unittest.main()
