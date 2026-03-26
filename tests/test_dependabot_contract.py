import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class DependabotContractTests(unittest.TestCase):
    def test_dependabot_tracks_workflows_and_both_npm_manifests(self) -> None:
        config = (REPO_ROOT / ".github/dependabot.yml").read_text(encoding="utf-8")

        self.assertIn("version: 2", config)
        self.assertIn('package-ecosystem: "github-actions"', config)
        self.assertIn('directory: "/"', config)
        self.assertIn('package-ecosystem: "npm"', config)
        self.assertIn('directory: "/themes/qfield-theme-v3"', config)
        self.assertIn('interval: "weekly"', config)
        self.assertIn('prefix: "ci"', config)
        self.assertIn('prefix: "deps"', config)
        self.assertIn("root-build-tooling:", config)
        self.assertIn("theme-build-tooling:", config)
        self.assertIn('- "dependencies"', config)


if __name__ == "__main__":
    unittest.main()
