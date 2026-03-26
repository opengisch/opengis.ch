import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class Pa11yCiContractTests(unittest.TestCase):
    def test_pa11y_config_covers_curated_smoke_pages(self) -> None:
        config = (REPO_ROOT / ".pa11yci.js").read_text(encoding="utf-8")

        self.assertIn('standard: "WCAG2AA"', config)
        self.assertIn('concurrency: 1', config)
        self.assertIn('runners: ["axe"]', config)
        self.assertIn('ignore: ["color-contrast"]', config)
        self.assertIn('executablePath: chromeExecutable', config)
        self.assertIn('"--headless=new"', config)
        self.assertIn('"--no-sandbox"', config)
        self.assertIn("`${baseUrl}/`", config)
        self.assertIn("`${baseUrl}/de/`", config)
        self.assertIn("`${baseUrl}/fr/`", config)
        self.assertIn("`${baseUrl}/it/`", config)
        self.assertNotIn("`${baseUrl}/jobs/`", config)
        self.assertIn("`${baseUrl}/qgis-support/`", config)
        self.assertIn("`${baseUrl}/qfield-rapidmapper/`", config)
        self.assertIn("`${baseUrl}/core-values/`", config)
        self.assertIn("`${baseUrl}/category/qfield/highlights/`", config)

    def test_pa11y_script_serves_public_and_runs_configured_smoke_check(self) -> None:
        script = (REPO_ROOT / "scripts/run_pa11y_ci.sh").read_text(encoding="utf-8")

        self.assertIn('python -m http.server "${port}" --bind "${host}" --directory public', script)
        self.assertIn('CHROME_BIN="${chrome_bin}"', script)
        self.assertIn('PA11Y_BASE_URL="${base_url}"', script)
        self.assertIn('./node_modules/.bin/pa11y-ci --config .pa11yci.js', script)
        self.assertIn('curl -fsS "${base_url}/"', script)

    def test_ci_workflow_installs_chrome_and_runs_pa11y(self) -> None:
        workflow = (REPO_ROOT / ".github/workflows/test.yml").read_text(encoding="utf-8")

        self.assertIn("uses: browser-actions/setup-chrome@v1", workflow)
        self.assertIn("id: setup-chrome", workflow)
        self.assertIn("run: ./scripts/run_pa11y_ci.sh", workflow)
        self.assertIn("CHROME_BIN: ${{ steps.setup-chrome.outputs.chrome-path }}", workflow)


if __name__ == "__main__":
    unittest.main()
