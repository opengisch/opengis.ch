import json
import tempfile
import unittest
from pathlib import Path

from scripts import sitemap_audit_viewer as viewer


class SitemapAuditViewerTests(unittest.TestCase):
    def sample_report(self) -> dict[str, object]:
        return {
            "generated_at_utc": "2026-03-09T09:49:43+00:00",
            "source_sitemap_url": "https://opengis.ch/sitemap.xml",
            "local_public_dir": "public",
            "offline_dir": "/tmp/offline",
            "allowed_domains": ["opengis.ch", "www.opengis.ch"],
            "total_urls_in_sitemap": 3,
            "total_urls_checked": 3,
            "summary": {
                "checked_pages": 3,
                "local_page_missing": 1,
                "source_fetch_failed": 0,
                "text_exact_match": 1,
                "text_mismatch": 1,
                "text_diff_within_threshold": 0,
                "content_found_under_different_url": 0,
                "alias_applied": 0,
                "average_similarity": 0.715,
            },
            "pages": [
                {
                    "url": "https://www.opengis.ch/missing/",
                    "path": "/missing/",
                    "local_file": None,
                    "matched_local_url": None,
                    "matched_local_file": None,
                    "alias_content_file": None,
                    "source_file": None,
                    "source_type": "remote",
                    "text_similarity": None,
                    "issues": ["local_page_missing"],
                },
                {
                    "url": "https://www.opengis.ch/mismatch/",
                    "path": "/mismatch/",
                    "local_file": "public/mismatch/index.html",
                    "matched_local_url": "/mismatch/",
                    "matched_local_file": "public/mismatch/index.html",
                    "alias_content_file": None,
                    "source_file": "/tmp/offline/www.opengis.ch/mismatch/index.html",
                    "source_type": "offline",
                    "text_similarity": 0.42,
                    "issues": ["text_mismatch"],
                },
                {
                    "url": "https://www.opengis.ch/ok/",
                    "path": "/ok/",
                    "local_file": "public/ok/index.html",
                    "matched_local_url": "/ok/",
                    "matched_local_file": "public/ok/index.html",
                    "alias_content_file": None,
                    "source_file": "/tmp/offline/www.opengis.ch/ok/index.html",
                    "source_type": "offline",
                    "text_similarity": 1.0,
                    "issues": [],
                },
            ],
        }

    def test_build_view_model_summarizes_pages(self) -> None:
        model = viewer.build_view_model(self.sample_report(), "report.json")

        self.assertEqual(model["report_label"], "report.json")
        self.assertEqual(model["clean_pages"], 1)
        self.assertEqual(model["total_pages"], 3)
        self.assertEqual(model["average_similarity"], "71.5%")
        self.assertEqual(model["summary_cards"][0]["value"], "3")
        self.assertEqual(model["issue_counts"][0]["key"], "local_page_missing")
        self.assertEqual(model["pages"][0]["status_label"], "Local page missing")
        self.assertTrue(model["pages"][2]["is_clean"])

    def test_render_html_embeds_viewer_payload(self) -> None:
        model = viewer.build_view_model(self.sample_report(), "report.json")
        html = viewer.render_html(model)

        self.assertIn("Sitemap Audit Viewer", html)
        self.assertIn('"report_label":"report.json"', html)
        self.assertIn('"status_label":"Local page missing"', html)
        self.assertIn("Problems only: on", html)

    def test_write_html_report_uses_json_filename_as_label(self) -> None:
        report = self.sample_report()

        with tempfile.TemporaryDirectory() as tmp_dir:
            json_path = Path(tmp_dir) / "sitemap_audit_report.json"
            html_path = Path(tmp_dir) / "sitemap_audit_report.html"
            json_path.write_text(json.dumps(report), encoding="utf-8")

            viewer.write_html_report(
                report,
                json_report_path=json_path,
                html_output_path=html_path,
            )

            html = html_path.read_text(encoding="utf-8")
            self.assertIn('"report_label":"sitemap_audit_report.json"', html)
            self.assertIn('"clean_pages":1', html)


if __name__ == "__main__":
    unittest.main()
