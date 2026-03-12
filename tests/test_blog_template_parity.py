import subprocess
import tempfile
import textwrap
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class BlogTemplateParityTests(unittest.TestCase):
    def test_blog_list_uses_qfield_v2_structure(self) -> None:
        template = (REPO_ROOT / "themes/qfield-theme-v3/layouts/blog/list.html").read_text(encoding="utf-8")

        self.assertIn('<section class="py-5 text-center bg-light mb-3">', template)
        self.assertIn('"/images/qfield_blog_default.png"', template)
        self.assertNotIn("blog-list-hero", template)
        self.assertNotIn("$contentImage", template)

    def test_blog_single_uses_qfield_v2_navigation_and_layout(self) -> None:
        template = (REPO_ROOT / "themes/qfield-theme-v3/layouts/blog/single.html").read_text(encoding="utf-8")

        self.assertEqual(template.count('{{ "/blog/" | relURL }}'), 2)
        self.assertIn('<div class="row justify-content-center">', template)
        self.assertIn("replaceRE `(?s)^\\s*<h[1-6][^>]*>.*?</h[1-6]>\\s*`", template)
        self.assertNotIn("blog-single-featured-image", template)
        self.assertNotIn("blog-related", template)

    def test_qfield_v2_fallback_asset_exists(self) -> None:
        self.assertTrue((REPO_ROOT / "static/images/qfield_blog_default.png").is_file())

    def test_blog_single_strips_duplicate_leading_heading_from_content(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir)
            content_dir = tmp_path / "content"
            page_dir = content_dir / "blog" / "2026" / "01" / "07" / "duplicate-heading"
            destination = tmp_path / "public"
            page_dir.mkdir(parents=True)

            (page_dir / "index.md").write_text(
                textwrap.dedent(
                    """\
                    ---
                    title: "Duplicate Heading Test - OPENGIS.ch"
                    date: 2026-01-07
                    slug: "duplicate-heading"
                    url: "/2026/01/07/duplicate-heading/"
                    ---

                    # Duplicate Heading Test

                    Intro paragraph for the post body.
                    """
                ),
                encoding="utf-8",
            )

            subprocess.run(
                [
                    "hugo",
                    "--environment",
                    "development",
                    "--contentDir",
                    str(content_dir),
                    "--destination",
                    str(destination),
                ],
                check=True,
                cwd=REPO_ROOT,
                capture_output=True,
                text=True,
            )

            html = (destination / "2026/01/07/duplicate-heading/index.html").read_text(encoding="utf-8")

        self.assertIn("<h1", html)
        self.assertIn("Duplicate Heading Test - OPENGIS.ch", html)
        self.assertIn("Intro paragraph for the post body.</p>", html)
        self.assertNotIn("<h1 id=\"duplicate-heading-test\">Duplicate Heading Test</h1>", html)


if __name__ == "__main__":
    unittest.main()
