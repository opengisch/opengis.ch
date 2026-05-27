import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class LighthouseCiContractTests(unittest.TestCase):
    def test_lighthouse_config_covers_curated_smoke_pages_and_thresholds(self) -> None:
        config = (REPO_ROOT / ".lighthouserc.js").read_text(encoding="utf-8")

        self.assertIn('const baseUrl = process.env.LIGHTHOUSE_BASE_URL || "http://127.0.0.1:8100"', config)
        self.assertIn('numberOfRuns: 1', config)
        self.assertIn('`${baseUrl}/`', config)
        self.assertIn('`${baseUrl}/de/`', config)
        self.assertIn('`${baseUrl}/fr/`', config)
        self.assertIn('`${baseUrl}/it/`', config)
        self.assertIn('`${baseUrl}/core-values/`', config)
        self.assertIn('`${baseUrl}/qgis-support/`', config)
        self.assertIn('`${baseUrl}/qfield-rapidmapper/`', config)
        self.assertIn('`${baseUrl}/category/qfield/highlights/`', config)
        self.assertIn('chromeFlags: "--headless=new --no-sandbox"', config)
        self.assertIn('"categories:performance"', config)
        self.assertIn('"categories:accessibility"', config)
        self.assertIn('"categories:best-practices"', config)
        self.assertIn('"categories:seo"', config)
        self.assertIn('target: "filesystem"', config)
        self.assertIn('outputDir: "./reports/lighthouseci"', config)

    def test_lighthouse_script_runs_lhci_against_built_site(self) -> None:
        script = (REPO_ROOT / "scripts/run_lighthouse_ci.sh").read_text(encoding="utf-8")
        package_json = (REPO_ROOT / "package.json").read_text(encoding="utf-8")

        self.assertIn('command -v google-chrome-stable', script)
        self.assertIn('public/index.html', script)
        self.assertIn('python -m http.server "${port}" --bind "${host}" --directory public', script)
        self.assertIn('LIGHTHOUSE_BASE_URL="${base_url}"', script)
        self.assertIn('CHROME_PATH="${chrome_bin}"', script)
        self.assertIn('./node_modules/.bin/lhci autorun --config .lighthouserc.js', script)
        self.assertIn('"@lhci/cli":', package_json)
        self.assertIn('"test:lighthouse": "./scripts/run_lighthouse_ci.sh"', package_json)

    def test_ci_workflow_keeps_lighthouse_manual_only_for_now(self) -> None:
        workflow = (REPO_ROOT / ".github/workflows/test.yml").read_text(encoding="utf-8")

        self.assertRegex(workflow, r"uses:\s+browser-actions/setup-chrome@v\d+\b")
        self.assertIn("id: setup-chrome", workflow)
        self.assertNotIn("run: ./scripts/run_lighthouse_ci.sh", workflow)
        self.assertIn("CHROME_BIN: ${{ steps.setup-chrome.outputs.chrome-path }}", workflow)


if __name__ == "__main__":
    unittest.main()
