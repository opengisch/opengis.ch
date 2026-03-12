import tempfile
import unittest
from pathlib import Path
from unittest import mock

from scripts import sitemap_content_audit as audit


class SitemapParsingTests(unittest.TestCase):
    def test_parse_urlset(self) -> None:
        xml = """<?xml version=\"1.0\" encoding=\"UTF-8\"?>
        <urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">
          <url><loc>https://opengis.ch/</loc></url>
          <url><loc>https://opengis.ch/de/entwicklung/</loc></url>
        </urlset>
        """
        urls, nested = audit.parse_sitemap_xml(xml)
        self.assertEqual(
            urls,
            [
                "https://opengis.ch/",
                "https://opengis.ch/de/entwicklung/",
            ],
        )
        self.assertEqual(nested, [])

    def test_parse_sitemapindex(self) -> None:
        xml = """<?xml version=\"1.0\" encoding=\"UTF-8\"?>
        <sitemapindex xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">
          <sitemap><loc>https://opengis.ch/page-sitemap.xml</loc></sitemap>
          <sitemap><loc>https://opengis.ch/post-sitemap.xml</loc></sitemap>
        </sitemapindex>
        """
        urls, nested = audit.parse_sitemap_xml(xml)
        self.assertEqual(urls, [])
        self.assertEqual(
            nested,
            [
                "https://opengis.ch/page-sitemap.xml",
                "https://opengis.ch/post-sitemap.xml",
            ],
        )


class UrlAndFileMappingTests(unittest.TestCase):
    def test_url_path_and_candidates_root(self) -> None:
        public_dir = Path("public")
        candidates = audit.local_candidates_for_url("https://opengis.ch/", public_dir)
        self.assertEqual(candidates, [public_dir / "index.html"])

    def test_candidates_for_pretty_url(self) -> None:
        public_dir = Path("public")
        candidates = audit.local_candidates_for_url(
            "https://opengis.ch/de/entwicklung/", public_dir
        )
        self.assertEqual(candidates, [public_dir / "de/entwicklung/index.html"])

    def test_candidates_for_html_url(self) -> None:
        public_dir = Path("public")
        candidates = audit.local_candidates_for_url(
            "https://opengis.ch/book-private-course/indexbc77.html", public_dir
        )
        self.assertEqual(
            candidates,
            [
                public_dir / "book-private-course/indexbc77.html",
                public_dir / "book-private-course/indexbc77/index.html",
            ],
        )

    def test_equivalent_blog_paths_adds_blog_prefix(self) -> None:
        self.assertEqual(
            audit.equivalent_blog_paths("/2025/05/29/1-million-downloads-qfields-big-milestone/"),
            [
                "/2025/05/29/1-million-downloads-qfields-big-milestone/",
                "/blog/2025/05/29/1-million-downloads-qfields-big-milestone/",
            ],
        )

    def test_equivalent_blog_paths_removes_blog_prefix(self) -> None:
        self.assertEqual(
            audit.equivalent_blog_paths("/de/blog/2025/05/29/example/"),
            [
                "/de/blog/2025/05/29/example/",
                "/de/2025/05/29/example/",
            ],
        )


class HtmlNormalizationTests(unittest.TestCase):
    def test_normalize_visible_text_uses_main(self) -> None:
        html = """
        <html><body>
            <header>Navigation Item</header>
            <main>
              <h1>Hello</h1>
              <p>World</p>
            </main>
            <footer>Footer Text</footer>
        </body></html>
        """
        text = audit.normalize_visible_text(html)
        self.assertEqual(text, "Hello World")

    def test_compare_text_similarity(self) -> None:
        source = "<html><body><main><h1>Title</h1><p>Alpha Beta</p></main></body></html>"
        local = "<html><body><main><h1>Title</h1><p>Alpha  Beta</p></main></body></html>"
        exact, similarity, source_text, local_text = audit.compare_texts(source, local)

        self.assertTrue(exact)
        self.assertAlmostEqual(similarity, 1.0)
        self.assertEqual(source_text, "Title Alpha Beta")
        self.assertEqual(local_text, "Title Alpha Beta")

    def test_is_html_page_url_filters_assets(self) -> None:
        self.assertTrue(audit.is_html_page_url("https://opengis.ch/de/entwicklung/"))
        self.assertFalse(
            audit.is_html_page_url("https://opengis.ch/wp-content/uploads/image.png")
        )

    def test_is_html_page_url_filters_probable_wordpress_attachment_routes(self) -> None:
        self.assertFalse(audit.is_html_page_url("https://www.opengis.ch/_pk87661-resized-2/"))
        self.assertFalse(
            audit.is_html_page_url(
                "https://www.opengis.ch/2025/05/29/1-million-downloads-qfields-big-milestone/qf-support-2-4/"
            )
        )
        self.assertFalse(audit.is_html_page_url("https://www.opengis.ch/0001-0500-mp4/"))
        self.assertFalse(audit.is_html_page_url("https://www.opengis.ch/cropped-logo-round-png/"))
        self.assertFalse(audit.is_html_page_url("https://www.opengis.ch/01_maya_and_lavertezzo/"))
        self.assertFalse(audit.is_html_page_url("https://www.opengis.ch/03/"))
        self.assertTrue(
            audit.is_html_page_url(
                "https://www.opengis.ch/2025/05/29/1-million-downloads-qfields-big-milestone/"
            )
        )


class AliasTests(unittest.TestCase):
    def test_normalize_source_path(self) -> None:
        self.assertEqual(
            audit.normalize_source_path("www.opengis.ch/de/entwicklung/index.html"),
            "/de/entwicklung/",
        )
        self.assertEqual(
            audit.normalize_source_path("https://www.opengis.ch/book-private-course/indexbc77.html"),
            "/book-private-course/indexbc77.html",
        )

    def test_choose_alias_candidate_prefers_language_match(self) -> None:
        candidates = [
            audit.LocalPageEntry(
                url="/custom-development/",
                html_file="public/custom-development/index.html",
                text="same",
                text_sha256="x",
            ),
            audit.LocalPageEntry(
                url="/de/entwicklung/",
                html_file="public/de/entwicklung/index.html",
                text="same",
                text_sha256="x",
            ),
        ]

        picked = audit.choose_alias_candidate("/de/legacy-url/", candidates)
        self.assertEqual(picked.url, "/de/entwicklung/")

    def test_add_alias_to_markdown(self) -> None:
        content = """---
title: Test
url: /de/entwicklung/
---
Body
"""

        with tempfile.TemporaryDirectory() as tmp_dir:
            md_file = Path(tmp_dir) / "index.de.md"
            md_file.write_text(content, encoding="utf-8")

            changed = audit.add_alias_to_markdown(md_file, "/de/legacy-url/")
            self.assertTrue(changed)

            updated = md_file.read_text(encoding="utf-8")
            self.assertIn("aliases:", updated)
            self.assertIn('  - "/de/legacy-url/"', updated)

            unchanged = audit.add_alias_to_markdown(md_file, "/de/legacy-url/")
            self.assertFalse(unchanged)


class AuditFallbackTests(unittest.TestCase):
    def test_audit_single_url_uses_blog_prefixed_local_match(self) -> None:
        local_entry = audit.LocalPageEntry(
            url="/blog/2025/05/29/example/",
            html_file="public/blog/2025/05/29/example/index.html",
            text="Example text",
            text_sha256=audit.sha256_text("Example text"),
        )

        with mock.patch.object(
            audit,
            "read_source_html",
            return_value=("remote", None, "<main>Example text</main>", True),
        ):
            result = audit.audit_single_url(
                url="https://www.opengis.ch/2025/05/29/example/",
                public_dir=Path("public"),
                timeout=20,
                similarity_threshold=0.99,
                offline_dir=None,
                local_by_url={local_entry.url: local_entry},
                local_by_hash={},
                content_url_index={},
                content_source_index={},
            )

        self.assertTrue(result.local_exists)
        self.assertEqual(result.local_file, "public/blog/2025/05/29/example/index.html")


if __name__ == "__main__":
    unittest.main()
