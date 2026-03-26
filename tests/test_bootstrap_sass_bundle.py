import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class BootstrapSassBundleTests(unittest.TestCase):
    def test_theme_sass_uses_curated_bootstrap_imports(self) -> None:
        styles = (REPO_ROOT / "themes/qfield-theme-v3/assets/sass/main.scss").read_text(encoding="utf-8")

        required_imports = [
            '@import "bootstrap/functions";',
            '@import "bootstrap/variables";',
            '@import "bootstrap/variables-dark";',
            '@import "bootstrap/maps";',
            '@import "bootstrap/mixins";',
            '@import "bootstrap/utilities";',
            '@import "bootstrap/root";',
            '@import "bootstrap/reboot";',
            '@import "bootstrap/type";',
            '@import "bootstrap/images";',
            '@import "bootstrap/containers";',
            '@import "bootstrap/grid";',
            '@import "bootstrap/forms";',
            '@import "bootstrap/buttons";',
            '@import "bootstrap/transitions";',
            '@import "bootstrap/dropdown";',
            '@import "bootstrap/button-group";',
            '@import "bootstrap/nav";',
            '@import "bootstrap/navbar";',
            '@import "bootstrap/card";',
            '@import "bootstrap/breadcrumb";',
            '@import "bootstrap/pagination";',
            '@import "bootstrap/badge";',
            '@import "bootstrap/alert";',
            '@import "bootstrap/list-group";',
            '@import "bootstrap/close";',
            '@import "bootstrap/tooltip";',
            '@import "bootstrap/carousel";',
            '@import "bootstrap/helpers";',
            '@import "bootstrap/utilities/api";',
        ]

        removed_imports = [
            '@import "bootstrap/bootstrap.scss";',
            '@import "bootstrap/tables";',
            '@import "bootstrap/accordion";',
            '@import "bootstrap/progress";',
            '@import "bootstrap/toasts";',
            '@import "bootstrap/modal";',
            '@import "bootstrap/popover";',
            '@import "bootstrap/spinners";',
            '@import "bootstrap/offcanvas";',
            '@import "bootstrap/placeholders";',
        ]

        self.assertIn('@import "variable-overrides.scss";', styles)

        for snippet in required_imports:
            self.assertIn(snippet, styles)

        for snippet in removed_imports:
            self.assertNotIn(snippet, styles)


if __name__ == "__main__":
    unittest.main()
