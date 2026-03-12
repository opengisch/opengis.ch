import subprocess
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class CourseCategoryCardImageTests(unittest.TestCase):
    def test_course_cards_do_not_render_post_relative_logo_paths(self) -> None:
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

            html = (destination / "category/courses/index.html").read_text(encoding="utf-8")

        self.assertIn(
            'src="/i0.wp.com/www.opengis.ch/wp-content/uploads/2023/12/287987844-8d7c6540-c32c-4d62-bf6e-1636a011567fa86e.png"',
            html,
        )
        self.assertIn('src="/images/opengis-logo.png"', html)
        self.assertNotIn("/2023/03/06/interlis-crashcourse-webinar/images/opengis-logo.png", html)
        self.assertNotIn("/2023/03/06/qgis-model-baker/images/opengis-logo.png", html)
        self.assertNotIn("/2023/03/06/qgis-basic/images/opengis-logo.png", html)
        self.assertNotIn("/2023/02/14/postgis-with-qgis/images/opengis-logo.png", html)
        self.assertNotIn(
            "/2022/03/06/postgresql-postgis-administrator-course/images/opengis-logo.png",
            html,
        )


if __name__ == "__main__":
    unittest.main()
