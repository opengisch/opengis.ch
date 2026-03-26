import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class ConfigFormatContractTests(unittest.TestCase):
    def test_hugo_config_uses_toml_across_default_and_environment_overrides(self) -> None:
        config_files = {
            "config/_default/hugo.toml": [
                'baseURL = "https://www.opengis.ch/"',
                'defaultContentLanguage = "en"',
                '[params.options]',
            ],
            "config/development/hugo.toml": [
                'baseURL = "http://localhost:1313/"',
                '[params]',
                'environment = "development"',
            ],
            "config/staging/hugo.toml": [
                '[params]',
                'environment = "staging"',
            ],
            "config/production/hugo.toml": [
                '[params]',
                'environment = "production"',
            ],
        }

        for relative_path, snippets in config_files.items():
            with self.subTest(config=relative_path):
                content = (REPO_ROOT / relative_path).read_text(encoding="utf-8")
                for snippet in snippets:
                    self.assertIn(snippet, content)

        self.assertFalse((REPO_ROOT / "config/_default/hugo.yaml").exists())
        self.assertFalse((REPO_ROOT / "config/development/hugo.yaml").exists())
        self.assertFalse((REPO_ROOT / "config/staging/hugo.yaml").exists())
        self.assertFalse((REPO_ROOT / "config/production/hugo.yaml").exists())


if __name__ == "__main__":
    unittest.main()
