import json
import tempfile
import unittest
from pathlib import Path

from scripts import static_asset_audit as audit


class StaticAssetAuditTests(unittest.TestCase):
    def test_extract_srcset_urls(self) -> None:
        self.assertEqual(
            audit.extract_srcset_urls("/a.png 1x, /b.png 2x"),
            ["/a.png", "/b.png"],
        )

    def test_normalize_reference_url_same_host_and_relative(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            public_dir = Path(tmp_dir) / "public"
            source_file = public_dir / "blog/post/index.html"
            source_file.parent.mkdir(parents=True)
            source_file.write_text("", encoding="utf-8")

            self.assertEqual(
                audit.normalize_reference_url(
                    "https://www.opengis.ch/wp-content/uploads/2020/04/test.png?x=1",
                    source_file=source_file,
                    public_dir=public_dir,
                ),
                "/wp-content/uploads/2020/04/test.png",
            )
            self.assertEqual(
                audit.normalize_reference_url(
                    "./image.png",
                    source_file=source_file,
                    public_dir=public_dir,
                ),
                "/blog/post/image.png",
            )
            self.assertEqual(
                audit.normalize_reference_url(
                    "/2022/10/13/qfield-2-4-is-here-and-it-is-%F0%9F%8D%8Ficious/image-3c738.png",
                    source_file=source_file,
                    public_dir=public_dir,
                ),
                "/2022/10/13/qfield-2-4-is-here-and-it-is-🍏icious/image-3c738.png",
            )

    def test_normalize_reference_url_ignores_non_asset_pages(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            public_dir = Path(tmp_dir) / "public"
            source_file = public_dir / "index.html"
            public_dir.mkdir(parents=True)
            source_file.write_text("", encoding="utf-8")

            self.assertIsNone(
                audit.normalize_reference_url(
                    "/contact/",
                    source_file=source_file,
                    public_dir=public_dir,
                )
            )
            self.assertIsNone(
                audit.normalize_reference_url(
                    "/livereload.js?mindelay=10&v=2",
                    source_file=source_file,
                    public_dir=public_dir,
                )
            )

    def test_audit_assets_reports_missing_and_unreferenced_uploads(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            public_dir = Path(tmp_dir) / "public"
            uploads = public_dir / "wp-content/uploads/2020/04"
            uploads.mkdir(parents=True)
            (uploads / "used.png").write_text("x", encoding="utf-8")
            (uploads / "orphan.png").write_text("x", encoding="utf-8")

            page_dir = public_dir / "demo"
            page_dir.mkdir(parents=True)
            (page_dir / "local.png").write_text("x", encoding="utf-8")
            (page_dir / "index.html").write_text(
                """
                <html><body>
                  <img src="/wp-content/uploads/2020/04/used.png" alt="">
                  <img src="/wp-content/uploads/2020/04/missing.png" alt="">
                  <img src="./local.png" alt="">
                </body></html>
                """,
                encoding="utf-8",
            )

            report = audit.audit_assets(public_dir)

            self.assertEqual(report["summary"]["missing_reference_count"], 1)
            self.assertEqual(report["summary"]["unreferenced_upload_count"], 1)
            self.assertEqual(report["missing_references"][0]["asset_path"], "/wp-content/uploads/2020/04/missing.png")
            self.assertEqual(report["unreferenced_uploads"][0]["asset_path"], "/wp-content/uploads/2020/04/orphan.png")

    def test_render_html_report_writes_embedded_data(self) -> None:
        report = {
            "summary": {
                "scanned_html_files": 1,
                "scanned_css_files": 0,
                "total_asset_references": 2,
                "unique_asset_references": 2,
                "missing_reference_count": 1,
                "total_uploaded_files": 1,
                "referenced_uploaded_files": 0,
                "unreferenced_upload_count": 1,
            },
            "findings": [
                {
                    "kind": "missing_reference",
                    "severity": 2,
                    "asset_path": "/wp-content/uploads/test.png",
                    "source_file": "index.html",
                    "reference_url": "/wp-content/uploads/test.png",
                    "count": 1,
                    "search_text": "x",
                }
            ],
        }

        with tempfile.TemporaryDirectory() as tmp_dir:
            json_path = Path(tmp_dir) / "static_asset_audit_report.json"
            html_path = Path(tmp_dir) / "static_asset_audit_report.html"
            audit.render_html_report(report, json_report_path=json_path, html_output_path=html_path)
            html = html_path.read_text(encoding="utf-8")

            self.assertIn("Static Asset Audit", html)
            self.assertIn('"asset_path":"/wp-content/uploads/test.png"', html)
            self.assertIn("Missing references", html)


if __name__ == "__main__":
    unittest.main()
