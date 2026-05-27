import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class ServiceWorkerContractTests(unittest.TestCase):
    def test_favicons_partial_links_manifest_when_present(self) -> None:
        template = (
            REPO_ROOT / "layouts/partials/head/favicons.html"
        ).read_text(encoding="utf-8")

        self.assertIn('os.FileExists "static/manifest.webmanifest"', template)
        self.assertIn('rel="manifest"', template)
        self.assertIn('{{ `manifest.webmanifest` | absURL }}', template)

    def test_footer_registers_service_worker_via_built_asset(self) -> None:
        template = (
            REPO_ROOT / "layouts/partials/footer/script-footer.html"
        ).read_text(encoding="utf-8")

        self.assertIn('resources.Get "js/service-worker-register.js"', template)
        self.assertIn('"serviceWorkerUrl" ("sw.js" | relURL)', template)
        self.assertIn('"environment" hugo.Environment', template)
        self.assertIn('targetPath" "js/service-worker-register.js"', template)
        self.assertIn('integrity="{{ $serviceWorkerRegister.Data.Integrity }}"', template)

    def test_service_worker_registration_script_is_environment_gated(self) -> None:
        script = (
            REPO_ROOT / "assets/js/service-worker-register.js"
        ).read_text(encoding="utf-8")

        self.assertIn('import params from "@params";', script)
        self.assertIn('environment !== "development"', script)
        self.assertIn('navigator.serviceWorker.register(serviceWorkerUrl)', script)
        self.assertIn('window.isSecureContext', script)

    def test_service_worker_only_caches_same_origin_static_get_requests(self) -> None:
        script = (REPO_ROOT / "static/sw.js").read_text(encoding="utf-8")
        manifest = (REPO_ROOT / "static/manifest.webmanifest").read_text(encoding="utf-8")

        self.assertIn('const STATIC_CACHE = "opengis-static-v1";', script)
        self.assertIn('const STATIC_DESTINATIONS = new Set(["style", "script", "font", "image"]);', script)
        self.assertIn('if (request.method !== "GET") {', script)
        self.assertIn("if (requestUrl.origin !== self.location.origin) {", script)
        self.assertIn('if (request.mode === "navigate") {', script)
        self.assertIn("event.respondWith(cacheFirst(request));", script)
        self.assertIn('"display": "standalone"', manifest)
        self.assertIn('"src": "/favicon-192x192.png"', manifest)


if __name__ == "__main__":
    unittest.main()
