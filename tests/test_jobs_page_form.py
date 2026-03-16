import subprocess
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
JOBS_FORM_URL = "https://forms.clickup.com/f/22wqj-820/2Z3S1OO9ZF44Y54FQQ"


class JobsPageFormTests(unittest.TestCase):
    def test_jobs_template_and_script_restore_clickup_form(self) -> None:
        template = (REPO_ROOT / "themes/qfield-theme-v3/layouts/_default/single.html").read_text(encoding="utf-8")
        script = (REPO_ROOT / "themes/qfield-theme-v3/assets/js/main.js").read_text(encoding="utf-8")
        styles = (REPO_ROOT / "assets/sass/styles.scss").read_text(encoding="utf-8")

        self.assertIn('{{ else if $isJobsPage }}', template)
        self.assertIn('id="jobs-application-form"', template)
        self.assertIn('data-jobs-clickup-link', template)
        self.assertIn(JOBS_FORM_URL, template)
        self.assertIn("const jobsApplicationForm = document.querySelector('#jobs-application-form.jobs-application-iframe')", script)
        self.assertIn("data-jobs-clickup-link", script)
        self.assertIn(".jobs-application-iframe {", styles)
        self.assertIn(".jobs-application-fallback {", styles)

    def test_jobs_page_renders_application_iframe(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            destination = Path(tmp_dir) / "public"

            subprocess.run(
                [
                    "hugo",
                    "--environment",
                    "development",
                    "--destination",
                    str(destination),
                ],
                check=True,
                cwd=REPO_ROOT,
                capture_output=True,
                text=True,
            )

            html = (destination / "jobs/index.html").read_text(encoding="utf-8")

        self.assertIn('id="jobs-application-form"', html)
        self.assertIn('class="clickup-embed clickup-dynamic-height jobs-application-iframe"', html)
        self.assertIn(f'data-clickup-src="{JOBS_FORM_URL}"', html)
        self.assertIn('data-jobs-clickup-link', html)


if __name__ == "__main__":
    unittest.main()
