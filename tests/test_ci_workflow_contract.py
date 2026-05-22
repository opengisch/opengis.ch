import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class CiWorkflowContractTests(unittest.TestCase):
    def test_repo_has_github_actions_workflow_for_local_validation_commands(self) -> None:
        workflow = (REPO_ROOT / ".github/workflows/test.yml").read_text(encoding="utf-8")

        self.assertIn("name: Test", workflow)
        self.assertIn("push:", workflow)
        self.assertIn("pull_request:", workflow)
        self.assertIn("uses: actions/checkout@v4", workflow)
        self.assertIn("submodules: recursive", workflow)
        self.assertIn("ssh-key: ${{ secrets.OPENGIS_HUGO_THEME_SSH_KEY }}", workflow)
        self.assertIn("uses: actions/setup-python@v5", workflow)
        self.assertIn('python-version: "3.12"', workflow)
        self.assertIn("uses: actions/setup-node@v4", workflow)
        self.assertIn('node-version: "22"', workflow)
        self.assertIn("uses: browser-actions/setup-chrome@v1", workflow)
        self.assertIn("id: setup-chrome", workflow)
        self.assertIn("run: npm ci", workflow)
        self.assertIn("uses: peaceiris/actions-hugo@v3", workflow)
        self.assertIn('hugo-version: "0.147.9"', workflow)
        self.assertIn('run: python -m unittest discover -s tests -p "test_*.py"', workflow)
        self.assertIn("run: python -m compileall scripts tests", workflow)
        self.assertIn("run: hugo --environment development", workflow)
        self.assertIn("run: ./scripts/run_lighthouse_ci.sh", workflow)
        self.assertIn("run: ./scripts/run_pa11y_ci.sh", workflow)
        self.assertIn("CHROME_BIN: ${{ steps.setup-chrome.outputs.chrome-path }}", workflow)
        self.assertIn("run: ./scripts/run_htmltest_ci.sh", workflow)

    def test_htmltest_script_checks_curated_rendered_pages(self) -> None:
        script = (REPO_ROOT / "scripts/run_htmltest_ci.sh").read_text(encoding="utf-8")

        self.assertIn('DirectoryPath: /work/public', script)
        self.assertIn('FilePath: ${relative_page}', script)
        self.assertIn('CheckExternal: false', script)
        self.assertIn('docker run --rm -v "${root_dir}:/work" -v "${config_file}:/tmp/htmltest.yml:ro" wjdp/htmltest -c /tmp/htmltest.yml', script)
        self.assertIn('"public/index.html"', script)
        self.assertIn('"public/de/index.html"', script)
        self.assertIn('"public/fr/index.html"', script)
        self.assertIn('"public/it/index.html"', script)
        self.assertIn('"public/jobs/index.html"', script)
        self.assertIn('"public/qgis-support/index.html"', script)
        self.assertIn('"public/qfield-rapidmapper/index.html"', script)
        self.assertIn('"public/core-values/index.html"', script)
        self.assertIn('"public/category/qfield/highlights/index.html"', script)
        self.assertIn('"public/de/category/qfield-de/highlights/index.html"', script)
        self.assertIn('"public/fr/category/qfield/highlights/index.html"', script)
        self.assertIn('"public/it/category/qfield-it/highlights/index.html"', script)

    def test_pages_workflow_publishes_and_cleans_up_pr_previews(self) -> None:
        workflow = (REPO_ROOT / ".github/workflows/pages.yml").read_text(encoding="utf-8")

        self.assertIn("name: Deploy Pages", workflow)
        self.assertIn("branches: [ main ]", workflow)
        self.assertIn("types: [ opened, reopened, synchronize, closed ]", workflow)
        self.assertIn('PRODUCTION_URL: "https://www.opengis.ch/"', workflow)
        self.assertIn('PREVIEW_ROOT: "https://www.opengis.ch/pr-preview"', workflow)
        self.assertIn('DEPLOY_BRANCH: "gh-pages"', workflow)
        self.assertIn("uses: actions/checkout@v4", workflow)
        self.assertIn("submodules: recursive", workflow)
        self.assertIn("ssh-key: ${{ secrets.OPENGIS_HUGO_THEME_SSH_KEY }}", workflow)
        self.assertNotIn("uses: actions/setup-node@v4", workflow)
        self.assertNotIn("run: npm ci", workflow)
        self.assertIn("uses: peaceiris/actions-hugo@v3", workflow)
        self.assertIn("hugo --environment production --gc --minify --baseURL", workflow)
        self.assertIn("hugo --environment staging -D --baseURL", workflow)
        self.assertIn("rsync -a --delete --exclude \".git\" --exclude \"pr-preview/\" public/", workflow)
        self.assertTrue((REPO_ROOT / "static/CNAME").exists())
        self.assertEqual("www.opengis.ch", (REPO_ROOT / "static/CNAME").read_text(encoding="utf-8").strip())
        self.assertTrue((REPO_ROOT / "CNAME").exists())
        self.assertEqual("www.opengis.ch", (REPO_ROOT / "CNAME").read_text(encoding="utf-8").strip())
        self.assertIn("cp CNAME \"${deploy_dir}/CNAME\"", workflow)
        self.assertIn("PREVIEW_PATH: pr-preview/pr-${{ github.event.pull_request.number }}", workflow)
        self.assertIn("mkdir -p \"${deploy_dir}/${PREVIEW_PATH}\"", workflow)
        self.assertIn("rsync -a --delete --exclude \"CNAME\" public/ \"${deploy_dir}/${PREVIEW_PATH}/\"", workflow)
        self.assertIn('marker="<!-- opengis-pr-preview -->"', workflow)
        self.assertIn("rm -rf \"${deploy_dir}/${PREVIEW_PATH}\"", workflow)
        self.assertIn("PR preview removed after this pull request was closed.", workflow)

    def test_robots_txt_blocks_preview_paths_and_non_production_builds(self) -> None:
        robots_template = (REPO_ROOT / "layouts/robots.txt").read_text(encoding="utf-8")

        self.assertIn('{{- if eq hugo.Environment "production" }}', robots_template)
        self.assertIn("Disallow: /404.html", robots_template)
        self.assertIn("Disallow: /pr-preview/", robots_template)
        self.assertIn('Sitemap: {{ "sitemap.xml" | absURL }}', robots_template)
        self.assertIn("{{- else }}", robots_template)
        self.assertIn("Disallow: /", robots_template)


if __name__ == "__main__":
    unittest.main()
