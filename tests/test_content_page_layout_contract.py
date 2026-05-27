import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
ROOT_PAGE_LAYOUTS = {
    "clickup-form.html",
    "content-page.html",
    "core-values.html",
    "course-calendar.html",
    "custom-development.html",
    "qfield-app.html",
    "qfield-installation.html",
    "qfield-training.html",
    "qgis-support.html",
    "qgis-sustainability-initiative.html",
    "rapidmapper.html",
    "static-embed.html",
    "training-consulting.html",
}
EXPLICIT_LAYOUT_PAGES = {
    "content/pages/about/core-values/index.md": 'layout: "core-values"',
    "content/pages/about/jobs/index.md": 'layout: "clickup-form"',
    "content/pages/about/newsletter/index.md": 'layout: "static-embed"',
    "content/pages/campaigns/crowdfunding-erweiterte-unterstutzung-fur-kreisbogen-in-qgis/index.md": 'layout: "static-embed"',
    "content/pages/qfield/app/index.md": 'layout: "qfield-app"',
    "content/pages/qfield/app/installation/index.md": 'layout: "qfield-installation"',
    "content/pages/qfield/jump-start-packages/qfield-training/index.md": 'layout: "qfield-training"',
    "content/pages/qfield/rapidmapper/index.md": 'layout: "rapidmapper"',
    "content/pages/services/consulting/training-consulting/index.md": 'layout: "training-consulting"',
    "content/pages/services/courses/calendar/index.md": 'layout: "course-calendar"',
    "content/pages/services/courses/interlis-model-baker/archive/index.md": 'layout: "course-calendar"',
    "content/pages/services/courses/overview/index.md": 'layout: "course-calendar"',
    "content/pages/services/courses/postgis/archive/index.md": 'layout: "course-calendar"',
    "content/pages/services/courses/pyqgis/index.md": 'layout: "course-calendar"',
    "content/pages/services/courses/qfield/archive/index.md": 'layout: "course-calendar"',
    "content/pages/services/courses/qgis/archive/index.md": 'layout: "course-calendar"',
    "content/pages/services/courses/registration/index.md": 'layout: "clickup-form"',
    "content/pages/services/custom-development/index.md": 'layout: "custom-development"',
    "content/pages/services/support-maintenance/order-support-contract/index.md": 'layout: "clickup-form"',
    "content/pages/services/support-maintenance/qgis-support/index.md": 'layout: "qgis-support"',
    "content/pages/services/support-maintenance/qgis-sustainability-initiative/index.md": 'layout: "qgis-sustainability-initiative"',
    "content/pages/qfield/jump-start-packages/book-private-course/index.md": 'layout: "clickup-form"',
}
CONTENT_ONLY_PAGE_FILES = (
    "content/pages/about/core-values/index.de.md",
    "content/pages/about/core-values/index.fr.md",
    "content/pages/about/core-values/index.it.md",
    "content/pages/about/core-values/index.md",
    "content/pages/about/newsletter/index.de.md",
    "content/pages/about/newsletter/index.fr.md",
    "content/pages/about/newsletter/index.it.md",
    "content/pages/about/newsletter/index.md",
    "content/pages/campaigns/crowdfunding-erweiterte-unterstutzung-fur-kreisbogen-in-qgis/index.de.md",
    "content/pages/campaigns/crowdfunding-erweiterte-unterstutzung-fur-kreisbogen-in-qgis/index.fr.md",
    "content/pages/campaigns/crowdfunding-erweiterte-unterstutzung-fur-kreisbogen-in-qgis/index.it.md",
    "content/pages/campaigns/crowdfunding-erweiterte-unterstutzung-fur-kreisbogen-in-qgis/index.md",
    "content/pages/qfield/app/index.de.md",
    "content/pages/qfield/app/index.fr.md",
    "content/pages/qfield/app/index.it.md",
    "content/pages/qfield/app/index.md",
    "content/pages/qfield/app/installation/index.de.md",
    "content/pages/qfield/app/installation/index.fr.md",
    "content/pages/qfield/app/installation/index.it.md",
    "content/pages/qfield/app/installation/index.md",
    "content/pages/qfield/app/supported-devices/index.md",
    "content/pages/qfield/rapidmapper/index.de.md",
    "content/pages/qfield/rapidmapper/index.fr.md",
    "content/pages/qfield/rapidmapper/index.it.md",
    "content/pages/qfield/rapidmapper/index.md",
    "content/pages/services/consulting/training-consulting/index.de.md",
    "content/pages/services/consulting/training-consulting/index.fr.md",
    "content/pages/services/consulting/training-consulting/index.it.md",
    "content/pages/services/consulting/training-consulting/index.md",
    "content/pages/services/custom-development/index.de.md",
    "content/pages/services/custom-development/index.fr.md",
    "content/pages/services/custom-development/index.it.md",
    "content/pages/services/custom-development/index.md",
    "content/pages/services/support-maintenance/qgis-sustainability-initiative/index.de.md",
    "content/pages/services/support-maintenance/qgis-sustainability-initiative/index.fr.md",
    "content/pages/services/support-maintenance/qgis-sustainability-initiative/index.it.md",
    "content/pages/services/support-maintenance/qgis-sustainability-initiative/index.md",
    "content/pages/system/about/index.md",
    "content/pages/system/our-qgis-sustainability-initiative/index.md",
    "content/pages/system/qfield-love/index.md",
)


class ContentPageLayoutContractTests(unittest.TestCase):
    def test_pages_section_cascades_to_root_content_layout(self) -> None:
        section_front_matter = (REPO_ROOT / "content/pages/_index.md").read_text(encoding="utf-8")
        self.assertIn('layout: "content-page"', section_front_matter)

    def test_root_page_layouts_live_in_project(self) -> None:
        layout_dir = REPO_ROOT / "layouts/pages"
        self.assertEqual(ROOT_PAGE_LAYOUTS, {path.name for path in layout_dir.glob("*.html")})
        self.assertFalse(any((REPO_ROOT / "themes/opengis-hugo-theme/layouts/pages").glob("*.html")))

    def test_special_pages_use_explicit_root_layouts(self) -> None:
        for relative_path, expected_layout in EXPLICIT_LAYOUT_PAGES.items():
            with self.subTest(relative_path=relative_path):
                content = (REPO_ROOT / relative_path).read_text(encoding="utf-8")
                self.assertIn(expected_layout, content)

    def test_page_markdown_files_are_content_only(self) -> None:
        for relative_path in CONTENT_ONLY_PAGE_FILES:
            with self.subTest(relative_path=relative_path):
                content = (REPO_ROOT / relative_path).read_text(encoding="utf-8")
                self.assertNotIn("![", content)
                self.assertNotIn("<img", content)
                self.assertNotIn("<iframe", content)
                self.assertNotIn('<div class="page-inline-embed', content)
                self.assertNotIn("gravatar", content)

    def test_default_single_template_stays_generic(self) -> None:
        template = (REPO_ROOT / "themes/opengis-hugo-theme/layouts/single.html").read_text(encoding="utf-8")

        for legacy_marker in (
            "$isJobsPage",
            "$isCustomDevelopmentPage",
            "$isTrainingConsultingPage",
            "$isSupportLayoutPage",
            "$isSustainabilityPage",
            "$isJumpStartPage",
            "$isOrderSupportContractPage",
            "$isBookPrivateCoursePage",
            "$isCoursesCalendarPage",
            "$isCourseRegistrationPage",
            ".RawContent",
        ):
            with self.subTest(legacy_marker=legacy_marker):
                self.assertNotIn(legacy_marker, template)

    def test_page_layouts_do_not_use_external_mirrored_wordpress_cdn_urls(self) -> None:
        for relative_path in (
            "layouts/pages/custom-development.html",
            "layouts/pages/qgis-sustainability-initiative.html",
            "layouts/pages/rapidmapper.html",
        ):
            with self.subTest(relative_path=relative_path):
                template = (REPO_ROOT / relative_path).read_text(encoding="utf-8")
                self.assertNotIn('"https://i0.wp.com/www.opengis.ch/', template)
                self.assertNotIn("'https://i0.wp.com/www.opengis.ch/", template)

    def test_page_front_matter_images_do_not_use_external_mirrored_wordpress_cdn_urls(self) -> None:
        for markdown_path in (REPO_ROOT / "content/pages").glob("**/index*.md"):
            with self.subTest(markdown_path=str(markdown_path.relative_to(REPO_ROOT))):
                content = markdown_path.read_text(encoding="utf-8")
                self.assertNotIn('image: "https://i0.wp.com/www.opengis.ch/', content)
                self.assertNotIn('src: "https://i0.wp.com/www.opengis.ch/', content)

    def test_training_consulting_layout_places_image_beside_quote(self) -> None:
        template = (REPO_ROOT / "layouts/pages/training-consulting.html").read_text(encoding="utf-8")

        self.assertIn('class="row align-items-center g-4 generic-single-content mb-4"', template)
        self.assertIn('class="col-12 col-lg-4"', template)
        self.assertIn('class="col-12 col-lg-8 d-flex align-items-center"', template)
        self.assertIn('class="custom-dev-quote m-0 w-100"', template)

    def test_qfield_training_layout_renders_jumpstart_image_in_copy_column(self) -> None:
        template = (REPO_ROOT / "layouts/pages/qfield-training.html").read_text(encoding="utf-8")
        styles = (REPO_ROOT / "assets/sass/styles.scss").read_text(encoding="utf-8")

        self.assertIn('class="jumpstart-visual"', template)
        self.assertIn('src="{{ "/images/qfield_jumpstart.png" | relURL }}"', template)
        self.assertIn(".jumpstart-visual {", styles)
        self.assertIn(".jumpstart-visual img {", styles)


if __name__ == "__main__":
    unittest.main()
