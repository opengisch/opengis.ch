import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class BootstrapJsBundleTests(unittest.TestCase):
    def test_footer_uses_curated_bootstrap_entrypoint(self) -> None:
        template = (REPO_ROOT / "themes/qfield-theme-v3/layouts/partials/footer/script-footer.html").read_text(encoding="utf-8")

        self.assertIn('{{ $bootstrap := resources.Get "js/bootstrap.entry.js" }}', template)
        self.assertIn('{{ $bootstrapBuildOptions := dict "targetPath" "js/bootstrap.js" "format" "iife" }}', template)
        self.assertIn('{{ $bootstrap = $bootstrap | js.Build $bootstrapBuildOptions -}}', template)
        self.assertNotIn('resources.Get "js/bootstrap/bootstrap.bundle.min.js"', template)

    def test_bootstrap_entry_imports_only_required_components(self) -> None:
        entry = (REPO_ROOT / "themes/qfield-theme-v3/assets/js/bootstrap.entry.js").read_text(encoding="utf-8")
        package_json = (REPO_ROOT / "package.json").read_text(encoding="utf-8")

        required_imports = [
            "import Alert from 'bootstrap/js/dist/alert'",
            "import Carousel from 'bootstrap/js/dist/carousel'",
            "import Collapse from 'bootstrap/js/dist/collapse'",
            "import Dropdown from 'bootstrap/js/dist/dropdown'",
            "import Tooltip from 'bootstrap/js/dist/tooltip'",
        ]
        removed_imports = [
            "import Modal from 'bootstrap/js/dist/modal'",
            "import Offcanvas from 'bootstrap/js/dist/offcanvas'",
            "import Popover from 'bootstrap/js/dist/popover'",
            "import ScrollSpy from 'bootstrap/js/dist/scrollspy'",
            "import Tab from 'bootstrap/js/dist/tab'",
            "import Toast from 'bootstrap/js/dist/toast'",
        ]

        for snippet in required_imports:
            self.assertIn(snippet, entry)

        for snippet in removed_imports:
            self.assertNotIn(snippet, entry)

        self.assertIn("window.bootstrap = {", entry)
        self.assertIn('"bootstrap":', package_json)
        self.assertIn('"@popperjs/core":', package_json)


if __name__ == "__main__":
    unittest.main()
