import re
import unittest
from pathlib import Path


INLINE_CAPTION_PATTERN = re.compile(r"!\[\]\(([^)]+)\)([^\n]*?)(?=(?:\s*!\[\])|\n|$)")


def is_safe_caption(caption: str) -> bool:
    normalized = caption.strip()
    if not normalized or len(normalized) > 120:
        return False
    for token in ("[", "](", "](<", "http://", "https://", "<", ">"):
        if token in normalized:
            return False
    return True


class BlogMarkdownImageAltContractTests(unittest.TestCase):
    def test_blog_markdown_images_do_not_leave_safe_inline_captions_outside_alt_text(self) -> None:
        offenders: list[str] = []

        for path in sorted(Path("content/blog").rglob("*.md")):
            text = path.read_text(encoding="utf-8")
            for _, caption in INLINE_CAPTION_PATTERN.findall(text):
                if is_safe_caption(caption):
                    offenders.append(f"{path.as_posix()}: {caption.strip()}")

        self.assertFalse(
            offenders,
            "Found blog markdown image lines that should move their inline caption into alt text:\n"
            + "\n".join(offenders[:20]),
        )


if __name__ == "__main__":
    unittest.main()
