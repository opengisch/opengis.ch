import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class ConfigFormatContractTests(unittest.TestCase):
    def test_hugo_config_uses_yaml_across_default_and_environment_overrides(self) -> None:
        config_files = {
            "config/_default/hugo.yaml": [
                "baseURL: https://www.opengis.ch/",
                "defaultContentLanguage: en",
                "    label: English",
                "    locale: en-US",
                "  options:",
            ],
            "config/development/hugo.yaml": [
                "baseURL: http://localhost:1313/",
                "params:",
                "  environment: development",
            ],
            "config/staging/hugo.yaml": [
                "params:",
                "  environment: staging",
            ],
            "config/production/hugo.yaml": [
                "params:",
                "  environment: production",
            ],
        }

        for relative_path, snippets in config_files.items():
            with self.subTest(config=relative_path):
                content = (REPO_ROOT / relative_path).read_text(encoding="utf-8")
                for snippet in snippets:
                    self.assertIn(snippet, content)

        self.assertFalse((REPO_ROOT / "config/_default/hugo.toml").exists())
        self.assertFalse((REPO_ROOT / "config/development/hugo.toml").exists())
        self.assertFalse((REPO_ROOT / "config/staging/hugo.toml").exists())
        self.assertFalse((REPO_ROOT / "config/production/hugo.toml").exists())

    def test_hugo_language_config_uses_current_keys(self) -> None:
        config = (REPO_ROOT / "config/_default/hugo.yaml").read_text(encoding="utf-8")

        self.assertNotIn("languageName:", config)
        self.assertNotIn("languageCode:", config)
        for label, locale in (
            ("English", "en-US"),
            ("German", "de-CH"),
            ("French", "fr-CH"),
            ("Italian", "it-CH"),
        ):
            with self.subTest(language=label):
                self.assertIn(f"label: {label}", config)
                self.assertIn(f"locale: {locale}", config)

    def test_hugo_config_keeps_default_mounts_available_for_test_builds(self) -> None:
        config = (REPO_ROOT / "config/_default/hugo.yaml").read_text(encoding="utf-8")

        self.assertNotIn("mounts:", config)
        self.assertNotIn("target: content", config)
        self.assertNotIn("target: layouts", config)


if __name__ == "__main__":
    unittest.main()
