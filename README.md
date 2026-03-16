# OPENGIS.ch

Operational runbook for the Hugo site in this repository.

## Requirements

- Hugo extended
- Python 3

## Hugo Config

- Main config: `config/_default/hugo.yaml`
- Environment overrides:
  - `config/development/hugo.yaml`
  - `config/staging/hugo.yaml`
  - `config/production/hugo.yaml`

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
The active typography now follows the live OPENGIS stack again: `Roboto` for body copy, `Didact Gothic` for headings/titles, and the site’s custom title components now use the same heading-style weight/scale treatment instead of a separate local mix.
Service-page quote components now use the full content width instead of a narrower 80% inset, so support/custom-development/sustainability quotes align with the rest of the body copy in both light and dark mode.
Every `content/pages/index*.md` file now keeps its normalized `source:` route in `aliases`, and a regression test checks that content-page front matter stays valid and those source paths remain covered.
The jobs page now uses a dedicated ClickUp application embed again, matching the live legacy `/jobs/` page and keeping a direct fallback link in the markup.
Non-blog content pages that depended on legacy inline embeds now keep them in markdown again, including the Brevo newsletter signup iframe and the crowdfunding progress chart, with shared iframe styling that remains acceptable in dark mode.
The GeoNinjas section now uses a split profile-card layout closer to the live OPENGIS site and reveals cards with a fade-in-from-left scroll animation.
Navbar dropdowns now switch to collapsed-menu-safe static submenu layout for the full `navbar-expand-lg` range, avoiding broken absolute-position panels between tablet and desktop widths.
Homepage hero-navbar colors are now scoped to top-level nav links only, so dropdown panels keep their normal menu-item colors even before the navbar switches to the scrolled state.
Navbar typography is also aligned more closely with the original OPENGIS/Hestia menu styling: lighter top-level weight, smaller menu sizes, and simpler dropdown text treatment.
When the navbar enters the scrolled state it now visibly shrinks, reducing overall height by tightening vertical padding and logo size.
On non-home pages that are too short to scroll, the compact navbar state is now applied immediately so those pages still use the reduced-height header.
The page shell now forces the main content area to grow inside the full-height body flex layout so the footer stays pinned to the bottom of the viewport on short pages.

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

Some regression tests invoke `hugo` directly to validate rendered HTML output, so keep the `hugo` binary available when running the test suite.

Run a fast syntax check for scripts/tests:

```bash
python -m compileall scripts tests
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

### Other Maintenance Scripts

Available one-off maintenance scripts:

- `scripts/convert_opengis_html_to_md.py`
- `scripts/localize_blog_images.py`
- `scripts/sync_blog_media_from_offline.py`

Check script-specific options with:

```bash
python scripts/<script_name>.py --help
```
