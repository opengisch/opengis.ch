import csv
import tempfile
import unittest
from pathlib import Path

from scripts import image_alt_audit as audit


class ImageAltAuditTests(unittest.TestCase):
    def test_classify_image_finds_missing_empty_and_generic_alt_patterns(self) -> None:
        self.assertEqual(
            audit.classify_image({"src": "/images/example.png"}),
            ("missing_alt", 3, "Image tag is missing an alt attribute."),
        )
        self.assertEqual(
            audit.classify_image({"src": "/images/example.png", "alt": ""}),
            (
                "empty_alt_review",
                2,
                "Image has an empty alt attribute but is not marked decorative.",
            ),
        )
        self.assertEqual(
            audit.classify_image({"src": "/images/vision.png", "alt": "Vision icon"}),
            (
                "generic_alt_review",
                1,
                "Alt text ends with 'icon' instead of describing the image content.",
            ),
        )

    def test_classify_image_ignores_decorative_tracking_pixels(self) -> None:
        self.assertIsNone(
            audit.classify_image(
                {
                    "src": "https://example.com/pixel.gif",
                    "alt": "",
                }
            )
        )

    def test_audit_image_alts_reports_findings_and_decorative_count(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            public_dir = Path(tmp_dir) / "public"
            page_dir = public_dir / "demo"
            page_dir.mkdir(parents=True)
            (page_dir / "index.html").write_text(
                """
                <html><body>
                  <img src="/images/missing.png">
                  <img src="/images/vision.png" alt="Vision icon">
                  <img src="/images/pixel.gif" alt="" width="1" height="1" style="display:none">
                </body></html>
                """,
                encoding="utf-8",
            )

            report = audit.audit_image_alts(public_dir)

            self.assertEqual(report["summary"]["scanned_html_files"], 1)
            self.assertEqual(report["summary"]["images_scanned"], 3)
            self.assertEqual(report["summary"]["decorative_images"], 1)
            self.assertEqual(report["summary"]["finding_count"], 2)
            self.assertEqual(report["summary"]["missing_alt_count"], 1)
            self.assertEqual(report["summary"]["generic_alt_review_count"], 1)

    def test_write_csv_report_outputs_findings(self) -> None:
        report = {
            "summary": {
                "scanned_html_files": 1,
                "images_scanned": 1,
                "decorative_images": 0,
                "finding_count": 1,
                "missing_alt_count": 0,
                "empty_alt_review_count": 0,
                "generic_alt_review_count": 1,
            },
            "findings": [
                {
                    "severity": 1,
                    "kind": "generic_alt_review",
                    "source_file": "index.html",
                    "line": 12,
                    "column": 5,
                    "src": "/images/vision.png",
                    "alt": "Vision icon",
                    "reason": "Alt text ends with 'icon' instead of describing the image content.",
                }
            ],
        }

        with tempfile.TemporaryDirectory() as tmp_dir:
            csv_path = Path(tmp_dir) / "image_alt_audit_report.csv"
            audit.write_csv_report(csv_path, report)

            rows = list(csv.DictReader(csv_path.read_text(encoding="utf-8").splitlines()))
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["kind"], "generic_alt_review")
            self.assertEqual(rows[0]["alt"], "Vision icon")


if __name__ == "__main__":
    unittest.main()
