import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
CONTENT_PAGES = REPO_ROOT / "content/pages"


class ContentPageStructureTests(unittest.TestCase):
    def test_navigation_buckets_exist(self) -> None:
        for relative_path in (
            "about",
            "services",
            "qfield",
            "campaigns",
            "system",
        ):
            with self.subTest(relative_path=relative_path):
                self.assertTrue((CONTENT_PAGES / relative_path).is_dir())

    def test_legacy_flat_page_directories_are_gone(self) -> None:
        legacy_flat_directories = (
            "android-gis",
            "book-private-course",
            "category",
            "comments",
            "core-values",
            "course-categories",
            "course-registration",
            "courses-calendar",
            "crowdfunding-erweiterte-unterstutzung-fur-kreisbogen-in-qgis",
            "custom-development",
            "jobs",
            "newsletter",
            "order-support-contract",
            "our-qgis-sustainability-initiative",
            "qfield-love",
            "qfield-rapidmapper",
            "qfield-training",
            "qgis-support",
            "qgis-sustainability-initiative",
            "training-consulting",
        )

        for relative_path in legacy_flat_directories:
            with self.subTest(relative_path=relative_path):
                self.assertFalse((CONTENT_PAGES / relative_path).exists())


if __name__ == "__main__":
    unittest.main()
