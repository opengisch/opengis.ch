# Hugo + Bootstrap Improvements Checklist

Based on a comprehensive analysis of the repository's Hugo and Bootstrap best practices.

Status last synced with branch state: March 25, 2026.

---

## 🔴 Critical

- [x] **Fix `aria-current` in dropdown menus** — `aria-current="true"` in dropdown items ([header.html:53,69](themes/qfield-theme-v3/layouts/partials/header/header.html#L53)) should be `aria-current="page"` (only for the active page) or removed entirely; `"true"` is not a valid ARIA token for page context
- [ ] **Tighten Content-Security-Policy** — Remove `'unsafe-inline'` from `style-src`; use nonce-based or hash-based inline style exemptions instead; audit and remove unused external domains (Typekit is whitelisted but appears unused)
- [x] **Add CI/CD automated testing** — No GitHub Actions workflow exists; regressions in accessibility, SCSS bundle, or JS behavior are not caught automatically; add `.github/workflows/test.yml` running the existing Python test suite

---

## 🟠 High

- [x] **Add SRI hashes to Font Awesome assets** — Font Awesome stylesheets ([stylesheet.html:20-21](themes/qfield-theme-v3/layouts/partials/head/stylesheet.html)) use `relURL` with a static hash suffix instead of Hugo's `resources.Fingerprint`; process them through the Hugo asset pipeline for proper integrity attributes
- [x] **Enable PostCSS / Autoprefixer** — PostCSS is commented out ([stylesheet.html:2](themes/qfield-theme-v3/layouts/partials/head/stylesheet.html)); no vendor prefixes are generated automatically, requiring manual maintenance; uncomment and configure
- [x] **Add `defer` and SRI to development scripts** — Development-environment `<script>` tags ([script-footer.html](themes/qfield-theme-v3/layouts/partials/head/script-footer.html)) lack `defer`, blocking rendering; also missing `crossorigin="anonymous"` and consistent hashing (dev uses MD5, prod uses SHA512)
- [x] **Fix SCSS options ordering** — `$sassOptions` is modified _after_ `toCSS` is called ([stylesheet.html](themes/qfield-theme-v3/layouts/partials/head/stylesheet.html)); move `outputStyle: compressed` override _before_ the `toCSS` call to ensure correct processing order

---

## 🟡 Medium

- [ ] **Implement critical CSS extraction** — No above-the-fold CSS is inlined; add a build step (e.g. `critical` npm package or Hugo pipe post-processing) to inline render-critical styles and defer the full stylesheet
- [x] **Add Lighthouse CI integration** — No automated performance/accessibility scoring; integrate `lighthouse-ci` into the CI pipeline to track Core Web Vitals regressions on PRs
- [x] **Add automated accessibility testing** — Existing tests verify HTML structure but not rendered a11y; add `pa11y-ci` or `axe-core` scanning against the built site
- [x] **Add HTML validation** — Integrate `html-proofer` or `htmltest` in CI to catch broken links, missing alt text, and malformed markup
- [x] **Document shortcode/partial parameters** — No JSDoc-style comments on partials explaining accepted parameters (e.g. `src`, `alt`, `loading`, `sizes`); add a header comment block to each partial in [layouts/partials/](themes/qfield-theme-v3/layouts/partials/)
- [x] **Fix image partial sizes/widths mismatch** — The `$sizes` string default `"640,960,1280"` does not match the actual widths slice `400 640 960 1280 1600`; align them so responsive size hints are accurate
- [x] **Replace setTimeout retry loop with MutationObserver** — [main.js](themes/qfield-theme-v3/assets/js/main.js) polls for the filter container with up to 10 × 100 ms retries; replace with a `MutationObserver` or `DOMContentLoaded` guard for cleaner, event-driven initialization

---

## 🟢 Low

- [ ] **Clean up WordPress mirror assets** — `/static/` still contains mirrored WordPress roots that are partially live (`i0.wp.com`, `wp-content`, `slides.opengis.ch`, `usabilityhub.opengis.ch`), but a new source-reference audit in `scripts/wordpress_mirror_audit.py` now identifies dead mirrors and this pass pruned the unreferenced `static/i1.wp.com/**` and `static/wp-json/otter/**` leftovers
- [x] **Audit all images for alt text** — `scripts/image_alt_audit.py` now generates JSON/CSV reports for rendered-site image alt coverage, and the markdown cleanup passes normalized both single-image and same-line gallery caption anti-patterns across the remaining historical blog and page backlog. After the final cleanup passes covering the remaining multilingual release/news, hiring, crowdfunding, homepage-logo, and legacy translated content, the March 25, 2026 rendered-site baseline now reports `0` review findings (`0` empty-alt reviews and `0` generic-alt reviews).
- [x] **Generate modern image formats** — The shared image partial and reusable carousel now emit AVIF and WebP variants with original-format fallbacks, so Hugo-managed responsive images no longer stop at the original raster format
- [x] **Consider Service Worker / PWA** — The site now registers a minimal same-origin service worker outside development, exposes a web app manifest, and caches static same-origin CSS/JS/font/image assets for repeat visits without touching navigations
- [x] **Audit and prune Typekit from CSP** — `use.typekit.net` and `p.typekit.net` are in the CSP allowlist but no Typekit usage was found in templates or SCSS; remove if unused
- [x] **Remove unused Bootstrap components from JS bundle** — Bootstrap's JS bundle includes all components (including unused ones like offcanvas, toast, popover); consider importing only required modules to reduce JS payload

---

## Already Done (for reference)

- [x] Skip link added to base template
- [x] Google Fonts migrated from SCSS `@import` to `<head>` preconnect + stylesheet with `display=swap`
- [x] Bootstrap SCSS tree-shaking implemented (unused components removed)
- [x] Header: language switcher converted to `<button>`, brand link has `aria-label`
- [x] Active nav links correctly use `aria-current="page"` (main level)
- [x] Dark mode: `aria-pressed` and `aria-label` dynamically synchronized on theme toggle
- [x] Production scripts use SHA512 fingerprinting with SRI `integrity` attributes and `defer`
- [x] All images use `loading="lazy"` and `decoding="async"`
- [x] Debug logging gated behind development/localhost check in `main.js`
- [x] Bootstrap upgraded to 5.3.3 (latest stable)
