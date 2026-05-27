import subprocess
import tempfile
import textwrap
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class GalleryShortcodeTests(unittest.TestCase):
    def test_gallery_shortcode_renders_wrapper_markup(self) -> None:
        with tempfile.TemporaryDirectory(dir=REPO_ROOT) as tmp_dir:
            tmp_path = Path(tmp_dir)
            content_dir = tmp_path / "content"
            page_dir = content_dir / "pages" / "gallery-shortcode-smoke"
            destination = tmp_path / "public"
            content_dir_arg = str(content_dir.relative_to(REPO_ROOT))
            destination_arg = str(destination.relative_to(REPO_ROOT))
            page_dir.mkdir(parents=True)

            (page_dir / "index.md").write_text(
                textwrap.dedent(
                    """\
                    ---
                    title: "Gallery Shortcode Smoke"
                    ---

                    {{< gallery autoplay="true" interval="3200" controls="true" indicators="false" >}}
                    <figure class="figure">
                      <img class="gallery-img img-fluid" src="/images/opengis-logo.png" alt="Logo one">
                      <figcaption class="figure-caption">First image</figcaption>
                    </figure>
                    <figure class="figure">
                      <img class="gallery-img img-fluid" src="/images/qfield_blog_default.png" alt="Logo two">
                      <figcaption class="figure-caption">Second image</figcaption>
                    </figure>
                    {{< /gallery >}}
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
                    content_dir_arg,
                    "--destination",
                    destination_arg,
                ],
                check=True,
                cwd=REPO_ROOT,
                capture_output=True,
                text=True,
            )

            html = (destination / "gallery-shortcode-smoke/index.html").read_text(encoding="utf-8")

        self.assertIn('class="gallery-wrapper"', html)
        self.assertIn('data-gallery-id="gallery-', html)
        self.assertIn('data-autoplay="true"', html)
        self.assertIn('data-interval="3200"', html)
        self.assertIn('data-controls="true"', html)
        self.assertIn('data-indicators="false"', html)
        self.assertIn(".carousel-item .gallery-img", html)

    def test_gallery_styles_and_lightbox_selectors_exist(self) -> None:
        styles = (REPO_ROOT / "assets/sass/styles.scss").read_text(encoding="utf-8")
        script = (REPO_ROOT / "assets/js/main.js").read_text(encoding="utf-8")

        self.assertIn(".gallery-carousel", styles)
        self.assertIn(".gallery-lightbox", styles)
        self.assertIn("function initializeGalleries()", script)
        self.assertIn("function openGalleryFullscreen(", script)


if __name__ == "__main__":
    unittest.main()
