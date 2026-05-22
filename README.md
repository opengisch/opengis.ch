# OPENGIS.ch

Operational runbook for the Hugo site in this repository.

Progress tracking for the Hugo/Bootstrap cleanup lives in `HUGO_BOOTSTRAP_ANALYSIS.md`, `claude_improvements.md`, and `IMPROVE_PLAN.md`, and those status docs are kept in sync with completed repository work.
The March 25, 2026 tracker sync reflects the completed TOML config migration, modern image formats, service worker/PWA slice, Dependabot setup, and WordPress-mirror audit tooling; the main remaining improvement items are critical CSS extraction, tighter CSP, a fuller JS build pipeline, and additional mirror pruning.

## Requirements

- Hugo extended 0.161.1
- Python 3
- Node.js and npm only for the Lighthouse and pa11y smoke scripts

## Hugo Config

- Main config: `config/_default/hugo.yaml`
- Environment overrides:
  - `config/development/hugo.yaml`
  - `config/staging/hugo.yaml`
  - `config/production/hugo.yaml`

## Content Layout

- `content/pages/` is now organized around the live navigation instead of a flat page-bundle list.
- Main top-level buckets are `about/`, `services/`, `qfield/`, `contact/`, plus supporting `campaigns/` and `system/` folders for non-menu content that still needs stable routes.
- Service and course bundles now live under nested folders such as `content/pages/services/support-maintenance/` and `content/pages/services/courses/**`, while QField-related bundles live under `content/pages/qfield/**`.

## Run Hugo

Start the local dev server:

```bash
hugo server
```

Build the site into `public/`:

```bash
hugo
```

For blog layout checks, inspect the generated output under `public/blog/`.
Theme shortcodes such as `gallery` and `blog-video` are rendered as part of a normal Hugo build.
Imported blog posts may start with their own markdown heading; the blog single template strips only the first leading rendered heading so the page title is not duplicated.
The landing page header now renders transparently over the hero image on first load and switches to the fixed solid navbar style after scrolling, so homepage checks should be verified at both scroll positions.
The active header override now renders nested dropdown submenus again for deeper navigation branches, and the breadcrumb override intentionally skips empty structural ancestors such as `/pages/` while keeping the visible label free of the trailing `– OPENGIS.ch` suffix.
The active typography now uses the restored local/system stack again: `Avenir Next` for body copy with `Segoe UI`/`Helvetica Neue` fallbacks, and `Trebuchet MS` for headings, navbar text, and emphasized title components.
Service-page quote components now use the full content width instead of a narrower 80% inset, so support/custom-development/sustainability quotes align with the rest of the body copy in both light and dark mode.
Every `content/pages/index*.md` file now keeps its normalized `source:` route in `aliases`, and a regression test checks that content-page front matter stays valid and those source paths remain covered.
The jobs page now uses a dedicated ClickUp application embed again, matching the live legacy `/jobs/` page and keeping a direct fallback link in the markup.
Non-blog content pages that depended on legacy inline embeds now keep them in markdown again, including the Brevo newsletter signup iframe and the crowdfunding progress chart, with shared iframe styling that remains acceptable in dark mode.
GeoNinjas card reveals now trigger a bit earlier and complete faster, with a shorter translate distance and tighter stagger so the section feels more responsive without disabling motion entirely.
Blog list cards and the homepage blog teaser cards now use the shared page-image resolver again, so post-bundle `images`, `cover.image`, `image`, and first-content-image fallbacks all feed the card thumbnails consistently.
The base shell now exposes a keyboard skip link and a `data-hugo-environment` marker, Google Fonts are loaded from the document head with `dns-prefetch`, `preconnect`, and stylesheet `preload` hints instead of SCSS `@import`, analytics-enabled builds now warm the Google Tag Manager origin too, and the main site script now gates its debug logging to development/local runs.
The header controls are now more semantically correct as well: the language switcher is a real button with `aria-label="Change language"`, active top-level and dropdown nav links consistently emit `aria-current="page"`, the brand link has an explicit home label, and the root `assets/js/dark-mode.js` override keeps the theme toggle `aria-pressed` and label in sync with the current theme. The homepage navbar includes the full scroll-aware class list (`navbar-color-on-scroll navbar-transparent hestia_left shadow-sm fixed-top og-navbar og-navbar-home`) so the hero transparency transition works on page load.
The site stylesheet is checked in at `assets/css/main.css` and loaded directly by `layouts/partials/head/stylesheet.html`, so Hugo builds do not require npm, PostCSS, or Sass compilation for CSS.
The footer uses the prebuilt Bootstrap JavaScript bundle shipped with the theme.
The head/footer asset partials now fingerprint the tracked Font Awesome CSS with SHA512 integrity attributes and use deferred SHA512-hashed scripts in development too, so local runs exercise the same non-blocking script contract as production.
Automated dependency updates are now configured in `.github/dependabot.yml` for the repository GitHub Actions workflow plus the root npm manifest used by browser-audit tooling, so build-tooling drift gets surfaced in small weekly PRs instead of large manual catch-up updates.
The active Hugo configuration now uses YAML again, with `config/_default/hugo.yaml` plus YAML environment overrides under `config/{development,staging,production}/`, and a regression test keeps the old `hugo.toml` files from creeping back in.
Language entries in the Hugo YAML config use Hugo's current `label` and `locale` keys instead of the deprecated `languageName` and `languageCode` keys, so local and CI builds should stay free of those deprecation warnings.
The site now also exposes a `manifest.webmanifest` and registers a minimal same-origin service worker outside development, caching static same-origin CSS, JavaScript, font, and image responses for repeat visits without taking over page navigations.
WordPress/static mirror cleanup is now measured by `scripts/wordpress_mirror_audit.py`, which scans source references before pruning mirrored roots; this branch already removed the dead `static/i1.wp.com/**` and `static/wp-json/otter/**` leftovers while leaving still-linked mirror content in place.
The shared image partial now emits a valid default `sizes` descriptor that matches its generated `400/640/960/1280/1600` width ladder, resolves bundle-local images through `.Page.Resources`, and emits responsive AVIF/WebP `<picture>` sources for processed page-resource images. The reusable carousel helper now follows the same AVIF/WebP-plus-fallback pattern, and the main site script now waits for delayed success-story cards with a `MutationObserver` instead of the old polling retry loop.
The main parameterized partials now carry explicit header docs for their accepted dict keys and return values, which makes the shared image/card/carousel helpers easier to reuse without reopening each file to rediscover the contract.
The root CSP overrides in `layouts/partials/head/content-security-policy.html` and `layouts/home.headers` remain on `'unsafe-inline'` for styles because the templates still emit inline style attributes, but the font policy is back to same-origin/data-only because the site no longer depends on external Google Fonts.
Homepage client-logo metadata now includes descriptive alt text, and the curated `htmltest` smoke script validates those rendered key pages instead of only checking the workflow file.
The GeoNinjas section now uses a split profile-card layout closer to the live OPENGIS site and reveals cards with a fade-in-from-left scroll animation.
Navbar dropdowns now switch to collapsed-menu-safe static submenu layout for the full `navbar-expand-lg` range, avoiding broken absolute-position panels between tablet and desktop widths.
Homepage hero-navbar colors are now scoped to top-level nav links only, so dropdown panels keep their normal menu-item colors even before the navbar switches to the scrolled state.
Navbar typography is also aligned more closely with the original OPENGIS/Hestia menu styling: lighter top-level weight, smaller menu sizes, and simpler dropdown text treatment.
When the navbar enters the scrolled state it now visibly shrinks, reducing overall height by tightening vertical padding and logo size.
On non-home pages that are too short to scroll, the compact navbar state is now applied immediately so those pages still use the reduced-height header.
The page shell now forces the main content area to grow inside the full-height body flex layout so the footer stays pinned to the bottom of the viewport on short pages.
The localized consulting service bundle at `content/pages/services/consulting/training-consulting/index*.md` now renders the shared `static/images/geospatial_consulting.png` asset inline with language-specific alt text, so future artwork changes for that page should keep the shared image and the localized markdown labels synchronized.

Clean rebuild of `public/`:

```bash
hugo --cleanDestinationDir
```

Build with an explicit environment:

```bash
hugo --environment development
hugo --environment staging
hugo --environment production
```

Run the dev server with an explicit environment:

```bash
hugo server --environment development
```

## Repo Scripts

Create the Python virtual environment:

```bash
./scripts/setup_python_venv.sh
source .venv/bin/activate
```

Run Python tests:

```bash
python -m unittest discover -s tests -p "test_*.py"
```

Some regression tests invoke `hugo` directly to validate rendered HTML output, so keep the `hugo` binary available when running the test suite. CI and deployment currently pin Hugo extended 0.161.1.
The Hugo config intentionally relies on Hugo's default module mounts; do not add a partial `module.mounts` list for only `assets` or `static`, because that disables default content/layout/data mounts and breaks isolated test builds that use `--contentDir` and temporary destinations.
The same three local validation commands are now mirrored in `.github/workflows/test.yml` so pushes and pull requests run the Python tests, compile check, and a development Hugo build automatically.
That workflow checks out the `.gitmodules` entry for `themes/opengis-hugo-theme` recursively via SSH (`git@github.com:opengisch/opengis-hugo-theme.git`), so GitHub Actions needs a repository secret named `OPENGIS_HUGO_THEME_SSH_KEY` with read access to the private theme submodule.
The `.github/workflows/pages.yml` deployment workflow publishes production builds from `main` to the `gh-pages` branch and publishes pull-request previews under `https://www.opengis.ch/pr-preview/pr-<number>/`, preserving the preview tree during production deploys and removing each preview when its pull request closes. It uses the same private theme submodule secret plus the repository `GITHUB_TOKEN` for pushing and PR comments, and the `CNAME` plus `static/CNAME` files keep the GitHub Pages custom domain set to `www.opengis.ch`. This deployment workflow intentionally does not run `npm ci`; CSS is already checked in.
The root `layouts/robots.txt` template allows production indexing while disallowing `/pr-preview/`; staging, development, and PR-preview builds emit `Disallow: /` so preview artifacts are not indexable even when served publicly.
The CI workflow now also runs a curated Lighthouse CI smoke pass via `scripts/run_lighthouse_ci.sh` and `.lighthouserc.js`, serving the built `public/` output on `127.0.0.1` and collecting desktop audits for the homepage, localized homepages, and key service/product landing pages.
The workflow also runs a curated browser-based accessibility smoke check via `scripts/run_pa11y_ci.sh`, which serves `public/` locally and checks a focused set of key first-party pages with `pa11y-ci` using the `axe` runner against WCAG 2 AA. The external-embed jobs page stays under the HTML smoke check instead of the `pa11y` set because the third-party form iframe makes browser navigation timing too unstable for CI.
The CI workflow now also runs a curated `htmltest` smoke check via `scripts/run_htmltest_ci.sh` against key rendered pages in `public/`, which keeps HTML/link validation active without immediately failing on the current backlog of legacy blog issues.

Run a fast syntax check for scripts/tests:

```bash
python -m compileall scripts tests
```

Run the curated Lighthouse CI smoke suite against the built site:

```bash
hugo --environment development
./scripts/run_lighthouse_ci.sh
```

### Sitemap Audit

Generate the sitemap audit JSON and HTML reports:

```bash
python scripts/sitemap_content_audit.py \
  --output reports/sitemap_audit_report.json \
  --html-output reports/sitemap_audit_report.html
```

Open the generated viewer:

- `reports/sitemap_audit_report.html`

Render the HTML viewer again from an existing JSON report:

```bash
python scripts/sitemap_audit_viewer.py \
  --input reports/sitemap_audit_report.json \
  --output reports/sitemap_audit_report.html
```

Apply alias fixes while running the audit:

```bash
python scripts/sitemap_content_audit.py \
  --apply-aliases \
  --output reports/sitemap_audit_report.json \
  --html-output reports/sitemap_audit_report.html
```

Useful options:

- `--build`
- `--max-pages N`
- `--concurrency N`
- `--offline-dir <path>`
- `--similarity-threshold <float>`
- `--html-output <path>`

### Static Asset Audit

Generate the static/uploaded-files audit JSON and HTML reports:

```bash
python scripts/static_asset_audit.py \
  --output reports/static_asset_audit_report.json \
  --html-output reports/static_asset_audit_report.html
```

Outputs:

- `reports/static_asset_audit_report.json`
- `reports/static_asset_audit_report.html`

### Image Alt Audit

Generate the rendered-site image alt-text audit JSON and CSV reports:

```bash
python scripts/image_alt_audit.py \
  --public-dir public \
  --output reports/image_alt_audit_report.json \
  --csv-output reports/image_alt_audit_report.csv
```

Outputs:

- `reports/image_alt_audit_report.json`
- `reports/image_alt_audit_report.csv`

The March 25, 2026 baseline report now flags `0` legacy review items, down from `1,424` after normalizing repeated historical blog markdown caption patterns and adding explicit alt text across the remaining multilingual blog, page, hiring, crowdfunding, homepage-logo, and legacy translated content. Keep the audit script in the maintenance workflow so new imports or translations can be checked before they reintroduce regressions.

### Other Maintenance Scripts

Available one-off maintenance scripts:

- `scripts/convert_opengis_html_to_md.py`
- `scripts/localize_blog_images.py`
- `scripts/sync_blog_media_from_offline.py`

Check script-specific options with:

```bash
python scripts/<script_name>.py --help
```
