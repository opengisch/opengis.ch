import subprocess
import tempfile
import textwrap
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
FIXTURE_IMAGE_BYTES = (REPO_ROOT / "static/images/qfield_blog_default.png").read_bytes()


class BlogCardImageTests(unittest.TestCase):
    def test_blog_list_and_homepage_cards_use_post_bundle_featured_images(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir)
            content_dir = tmp_path / "content"
            destination = tmp_path / "public"

            posts = (
                ("2026/01/09/bundle-image-post", "Bundle Image Post", "bundle-featured.png"),
                ("2026/01/08/second-bundle-post", "Second Bundle Post", "second-featured.png"),
                ("2026/01/07/third-bundle-post", "Third Bundle Post", "third-featured.png"),
            )

            for rel_dir, title, image_name in posts:
                page_dir = content_dir / "blog" / rel_dir
                page_dir.mkdir(parents=True)
                (page_dir / "index.md").write_text(
                    textwrap.dedent(
                        f"""\
                        ---
                        title: "{title} - OPENGIS.ch"
                        date: {rel_dir.split('/')[0]}-{rel_dir.split('/')[1]}-{rel_dir.split('/')[2]}
                        slug: "{rel_dir.split('/')[-1]}"
                        url: "/{rel_dir}/"
                        images:
                          - "{image_name}"
                        ---

                        Intro paragraph for {title}.
                        """
                    ),
                    encoding="utf-8",
                )
                (page_dir / image_name).write_bytes(FIXTURE_IMAGE_BYTES)

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

            blog_html = (destination / "blog/index.html").read_text(encoding="utf-8")
            home_html = (destination / "index.html").read_text(encoding="utf-8")

        self.assertIn("bundle-featured_hu_", blog_html)
        self.assertIn("second-featured_hu_", blog_html)
        self.assertIn("third-featured_hu_", blog_html)
        self.assertNotIn('/images/qfield_blog_default.png', blog_html)

        self.assertIn("bundle-featured_hu_", home_html)
        self.assertIn("second-featured_hu_", home_html)
        self.assertIn("third-featured_hu_", home_html)

    def test_blog_list_and_homepage_cards_emit_modern_picture_sources_for_bundle_images(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir)
            content_dir = tmp_path / "content"
            destination = tmp_path / "public"

            post_dir = content_dir / "blog" / "2026" / "01" / "09" / "bundle-image-post"
            post_dir.mkdir(parents=True)
            (post_dir / "index.md").write_text(
                textwrap.dedent(
                    """\
                    ---
                    title: "Bundle Image Post - OPENGIS.ch"
                    date: 2026-01-09
                    slug: "bundle-image-post"
                    url: "/2026/01/09/bundle-image-post/"
                    images:
                      - "bundle-featured.png"
                    ---

                    Intro paragraph for Bundle Image Post.
                    """
                ),
                encoding="utf-8",
            )
            (post_dir / "bundle-featured.png").write_bytes(FIXTURE_IMAGE_BYTES)

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

            blog_html = (destination / "blog/index.html").read_text(encoding="utf-8")
            home_html = (destination / "index.html").read_text(encoding="utf-8")

        self.assertIn('type="image/webp"', blog_html)
        self.assertIn(".webp", blog_html)

        self.assertIn('type="image/webp"', home_html)
        self.assertIn(".webp", home_html)


if __name__ == "__main__":
    unittest.main()
