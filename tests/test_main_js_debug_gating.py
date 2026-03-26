import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class MainJsDebugGatingTests(unittest.TestCase):
    def test_debug_logging_is_gated_by_environment(self) -> None:
        script = (REPO_ROOT / "themes/qfield-theme-v3/assets/js/main.js").read_text(encoding="utf-8")

        self.assertIn("const debugEnabled =", script)
        self.assertIn("document.documentElement.dataset.hugoEnvironment === 'development'", script)
        self.assertIn("const debugLog = (...args) => {", script)
        self.assertIn("const debugWarn = (...args) => {", script)
        self.assertIn("debugLog('Main.js script loaded at:', new Date().toISOString())", script)
        self.assertIn("if (debugEnabled) {", script)
        self.assertIn("window.testFilter = function(filterName) {", script)
        self.assertIn("let successStoriesObserver = null", script)
        self.assertIn("function observeSuccessStoryCards() {", script)
        self.assertIn("typeof MutationObserver === 'undefined'", script)
        self.assertIn("new MutationObserver(() => {", script)
        self.assertIn("disconnectSuccessStoriesObserver()", script)
        self.assertNotIn("console.log('Main.js script loaded at:", script)
        self.assertNotIn("console.warn('Bootstrap not available for carousel initialization')", script)
        self.assertNotIn("let initAttempts = 0", script)
        self.assertNotIn("setTimeout(initializeApp, 100)", script)


if __name__ == "__main__":
    unittest.main()
