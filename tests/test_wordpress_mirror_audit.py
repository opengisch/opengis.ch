import json
import tempfile
import unittest
from pathlib import Path

from scripts import wordpress_mirror_audit as audit


class WordPressMirrorAuditTests(unittest.TestCase):
    def test_audit_mirrors_reports_referenced_and_unreferenced_files(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            repo_root = Path(tmp_dir)
            (repo_root / "content").mkdir(parents=True)
            (repo_root / "static/i0.wp.com/www.opengis.ch/wp-content/uploads/2024/07").mkdir(parents=True)
            (repo_root / "static/wp-json/otter/v1/dynamic").mkdir(parents=True)

            referenced_asset = repo_root / "static/i0.wp.com/www.opengis.ch/wp-content/uploads/2024/07/hero.png"
            orphan_asset = repo_root / "static/wp-json/otter/v1/dynamic/index1e68.html"
            referenced_asset.write_text("hero", encoding="utf-8")
            orphan_asset.write_text("legacy", encoding="utf-8")
            (repo_root / "content/page.md").write_text(
                'image: "/i0.wp.com/www.opengis.ch/wp-content/uploads/2024/07/hero.png"\n',
                encoding="utf-8",
            )

            report = audit.audit_mirrors(repo_root)

            self.assertEqual(report["summary"]["mirror_file_count"], 2)
            self.assertEqual(report["summary"]["referenced_file_count"], 1)
            self.assertEqual(report["summary"]["unreferenced_file_count"], 1)
            self.assertEqual(report["referenced_files"][0]["path"], "/i0.wp.com/www.opengis.ch/wp-content/uploads/2024/07/hero.png")
            self.assertEqual(report["unreferenced_files"][0]["path"], "/wp-json/otter/v1/dynamic/index1e68.html")

    def test_main_report_shape_can_be_serialized(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            repo_root = Path(tmp_dir)
            (repo_root / "content").mkdir(parents=True)
            (repo_root / "static/i1.wp.com/www.opengis.ch/wp-content/uploads/2020/03").mkdir(parents=True)
            asset = repo_root / "static/i1.wp.com/www.opengis.ch/wp-content/uploads/2020/03/banner.png"
            asset.write_text("banner", encoding="utf-8")
            output = repo_root / "reports/mirror_audit.json"

            report = audit.audit_mirrors(repo_root)
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_text(json.dumps(report, indent=2), encoding="utf-8")

            written = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(written["summary"]["unreferenced_file_count"], 1)
            self.assertEqual(written["unreferenced_files"][0]["path"], "/i1.wp.com/www.opengis.ch/wp-content/uploads/2020/03/banner.png")


if __name__ == "__main__":
    unittest.main()
