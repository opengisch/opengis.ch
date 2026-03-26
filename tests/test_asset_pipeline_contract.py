import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class AssetPipelineContractTests(unittest.TestCase):
    def test_stylesheet_partial_runs_postcss_with_theme_local_config(self) -> None:
        template = (REPO_ROOT / "themes/qfield-theme-v3/layouts/partials/head/stylesheet.html").read_text(encoding="utf-8")
        config = (REPO_ROOT / "themes/qfield-theme-v3/postcss.config.js").read_text(encoding="utf-8")
        root_package_json = (REPO_ROOT / "package.json").read_text(encoding="utf-8")

        self.assertIn('{{- $postcssOptions := dict "config" "themes/qfield-theme-v3" "noMap" true -}}', template)
        self.assertIn('| toCSS $sassOptions | postCSS $postcssOptions', template)
        self.assertNotIn('{{/*- $postcssOptions := dict "use" "autoprefixer" "noMap" true -*/}}', template)

        self.assertIn('require("autoprefixer")', config)
        self.assertIn('"autoprefixer":', root_package_json)
        self.assertIn('"postcss":', root_package_json)
        self.assertIn('"postcss-cli":', root_package_json)

    def test_stylesheet_partial_fingerprints_font_awesome_assets(self) -> None:
        template = (REPO_ROOT / "themes/qfield-theme-v3/layouts/partials/head/stylesheet.html").read_text(encoding="utf-8")

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
        template = (REPO_ROOT / "themes/qfield-theme-v3/layouts/partials/footer/script-footer.html").read_text(encoding="utf-8")

        self.assertIn('{{ $bootstrap := $bootstrap | fingerprint "sha512" -}}', template)
        self.assertIn('{{ $js := . | fingerprint "sha512" -}}', template)
        self.assertIn('integrity="{{ $bootstrap.Data.Integrity }}" crossorigin="anonymous" defer', template)
        self.assertIn('integrity="{{ $js.Data.Integrity }}" crossorigin="anonymous" defer', template)
        self.assertNotIn('fingerprint "md5"', template)
        self.assertNotIn('?v={{ $bootstrap.Data.Integrity }}', template)
        self.assertNotIn('?v={{ $js.Data.Integrity }}', template)


if __name__ == "__main__":
    unittest.main()
