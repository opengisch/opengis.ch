import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class BootstrapJsBundleTests(unittest.TestCase):
    def test_footer_uses_prebuilt_bootstrap_bundle_without_node_build(self) -> None:
        template = (REPO_ROOT / "layouts/partials/footer/script-footer.html").read_text(encoding="utf-8")
        package_json = (REPO_ROOT / "package.json").read_text(encoding="utf-8")

        self.assertIn('{{ $bootstrap := resources.Get "js/bootstrap/bootstrap.bundle.min.js" }}', template)
        self.assertNotIn("bootstrap := resources.Get \"js/bootstrap/bootstrap.bundle.min.js\" | js.Build", template)
        self.assertNotIn("bootstrap.entry.js", template)
        self.assertNotIn('"bootstrap":', package_json)
        self.assertNotIn('"@popperjs/core":', package_json)


if __name__ == "__main__":
    unittest.main()
