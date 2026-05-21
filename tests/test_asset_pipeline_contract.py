import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class AssetPipelineContractTests(unittest.TestCase):
    def test_stylesheet_partial_uses_checked_in_css_without_sass_or_postcss(self) -> None:
        template = (REPO_ROOT / "layouts/partials/head/stylesheet.html").read_text(encoding="utf-8")
        stylesheet = (REPO_ROOT / "assets/css/main.css").read_text(encoding="utf-8")
        root_package_json = (REPO_ROOT / "package.json").read_text(encoding="utf-8")

        self.assertIn('{{ $css := resources.Get "css/main.css" -}}', template)
        self.assertNotIn("css.Sass", template)
        self.assertNotIn("toCSS", template)
        self.assertNotIn("postCSS", template)
        self.assertIn("Bootstrap  v5.3.3", stylesheet)
        self.assertIn(".navbar-color-on-scroll", stylesheet)

        self.assertNotIn('"autoprefixer":', root_package_json)
        self.assertNotIn('"postcss":', root_package_json)
        self.assertNotIn('"postcss-cli":', root_package_json)
        self.assertNotIn('"bootstrap":', root_package_json)
        self.assertNotIn('"@popperjs/core":', root_package_json)

    def test_stylesheet_partial_fingerprints_font_awesome_assets(self) -> None:
        template = (REPO_ROOT / "layouts/partials/head/stylesheet.html").read_text(encoding="utf-8")

        self.assertIn('resources.FromString "font-awesome/css/all.min20b9.css"', template)
        self.assertIn('readFile "static/font-awesome/css/all.min20b9.css"', template)
        self.assertIn('resources.FromString "font-awesome/css/v4-shims.min20b9.css"', template)
        self.assertIn('readFile "static/font-awesome/css/v4-shims.min20b9.css"', template)
        self.assertIn('resources.Fingerprint "sha512"', template)
        self.assertIn('integrity="{{ $fontAwesomeAll.Data.Integrity }}"', template)
        self.assertIn('integrity="{{ $fontAwesomeShims.Data.Integrity }}"', template)
        self.assertNotIn('href="{{ "/font-awesome/css/all.min20b9.css" | relURL }}"', template)
        self.assertNotIn('href="{{ "/font-awesome/css/v4-shims.min20b9.css" | relURL }}"', template)

    def test_footer_scripts_are_deferred_and_use_sha512_in_development(self) -> None:
        template = (REPO_ROOT / "layouts/partials/footer/script-footer.html").read_text(encoding="utf-8")

        self.assertIn('{{ $bootstrap = $bootstrap | fingerprint "sha512" -}}', template)
        self.assertIn('{{ $appBundle = $appBundle | minify | fingerprint "sha512" -}}', template)
        self.assertIn('integrity="{{ $bootstrap.Data.Integrity }}" crossorigin="anonymous" defer', template)
        self.assertIn('integrity="{{ $appBundle.Data.Integrity }}" crossorigin="anonymous" defer', template)
        self.assertNotIn('fingerprint "md5"', template)
        self.assertNotIn('?v={{ $bootstrap.Data.Integrity }}', template)
        self.assertNotIn('?v={{ $appBundle.Data.Integrity }}', template)


if __name__ == "__main__":
    unittest.main()
