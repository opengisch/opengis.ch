import params from "@params";

const serviceWorkerUrl = params.serviceWorkerUrl || "/sw.js";
const environment = params.environment || "development";
const shouldRegisterServiceWorker =
  "serviceWorker" in navigator &&
  window.isSecureContext &&
  environment !== "development";

if (shouldRegisterServiceWorker) {
  window.addEventListener("load", () => {
    navigator.serviceWorker.register(serviceWorkerUrl).catch((error) => {
      if (document.documentElement.dataset.hugoEnvironment === "development") {
        console.warn("Service worker registration failed", error);
      }
    });
  });
}
