# Hugo Bootstrap Theme

[![Build and Deploy to gh-pages branch](https://github.com/filipecarneiro/hugo-bootstrap-theme/actions/workflows/gh-pages.yml/badge.svg)](https://github.com/filipecarneiro/hugo-bootstrap-theme/actions/workflows/gh-pages.yml) [![Publish to GitHub Pages](https://github.com/filipecarneiro/hugo-bootstrap-theme/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/filipecarneiro/hugo-bootstrap-theme/actions/workflows/pages/pages-build-deployment)

Theme for a blazing fast static website and/or blog using bootstrap 5.

![Screenshot](https://github.com/filipecarneiro/hugo-bootstrap-theme/blob/main/images/tn.png)

## Local customizations

- Replaced legacy alias mappings with real route-backed category pages under `content/pages/course-categories/**` (EN/DE/FR/IT) for old WordPress course taxonomy URLs (`/category/courses/qgis-courses/` plus DE/FR/IT category paths), preventing menu/category-link 404s without redirect pages.
- Added course-archive rendering in `layouts/_default/single.html` for category pages with `course_posts` front matter, so `qgis-courses` routes now show post listings (EN/DE/FR/IT) instead of the calendar iframe.
- Styled standalone course registration/calendar CTA links in content (e.g. “Register here”) as green rounded pill buttons via `assets/sass/styles.scss`, including localized EN/DE/FR/IT routes.
- Added a dedicated `course-registration` layout branch in `layouts/_default/single.html` with language-specific ClickUp registration form embeds for `/course-registration/`, `/de/kursanmeldung/`, `/fr/inscriptions-aux-cours/`, and `/it/iscrizione-corsi/`.
- Added registration-iframe initialization in `assets/js/main.js` so current query parameters are passed through to the embedded form URL/fallback link.
- Added registration embed styles in `/assets/sass/styles.scss` (desktop/mobile sizing and dark-mode border/fallback text).
- Removed stale imported “Recent Posts” placeholder body from all `content/pages/course-registration/index*.md` files.
- Added a dedicated `courses-calendar` layout branch in `layouts/_default/single.html` with language-specific ClickUp shared-calendar iframes so `/courses-calendar/`, `/de/kurskalender/`, `/fr/calendrier-des-cours/`, and `/it/calendario-corsi/` match production behavior.
- Added styles for the calendar embed iframe in `/assets/sass/styles.scss` (desktop/mobile height and dark-mode border).
- Removed stale imported “Recent Posts” placeholder body from `content/pages/courses-calendar/index.md` so the English calendar page focuses on the embedded calendar.
- Added a dedicated `book-private-course` branch in `layouts/_default/single.html` that renders the requested ClickUp booking iframe (`forms.clickup.com/f/22wqj-11141/2YYC027R5B98SX991E`) and a fallback external link.
- Added booking-iframe initialization in `assets/js/main.js` to pass through current page query parameters (for example `wpf10757_9`) into the embed URL.
- Added `book-private-course` form styles in `/assets/sass/styles.scss` (desktop/mobile sizing and dark-mode fallback text color).
- Fixed QField jump-start booking CTAs in all localized `content/pages/qfield-training/index*.md` pages to point to canonical `book-private-course` URLs with query params, replacing legacy hashed URL targets that produced 404s.
- Added legacy aliases in `content/pages/book-private-course/index*.md` so old hashed paths (`indexbc77.html` / `index4953.html`, including DE/FR/IT variants) continue to resolve.
- Fixed gallery initialization in `assets/js/main.js` to return immediately when no gallery wrappers are present, removing the endless retry loop and repeated console noise on pages without galleries.
- Updated the order-support-contract iframe flow to read a `data-clickup-src` URL, keep a direct fallback form link in markup, and skip automatic iframe loading on localhost unless `?embed_clickup=1` is set.
- Added corresponding order-support fallback text and dark-mode-safe styles in the site-level Sass (`/assets/sass/styles.scss`).
- Restructured OPENGIS site config to mirror `qfield_hugo_v2`: single `config/_default/hugo.yaml` plus `config/{development,staging,production}/hugo.yaml` environment overrides.
- Migrated OPENGIS and `exampleSite` config/data files from TOML to YAML and removed the corresponding TOML files.
- Kept `theme.toml` unchanged because Hugo expects theme metadata in TOML format.
- Set the site default theme to light in `config/_default/hugo.yaml` (`params.defaultTheme: light`), while keeping dark mode available as a user toggle.
- Backfilled missing blog `image` front matter for posts that had recoverable local mirror assets, including the Ticino rapid-mapping post (`2024/07/07/qfield-rapid-mapping-ticino`).
- Updated `layouts/blog/single.html` to render a featured image block when a post defines `cover.image` or `image`.
- Restored the missing RSI embed video in the Ticino rapid-mapping post variants (EN/DE/FR/IT) and added responsive `.blog-embed-video` styling in the site Sass.
- Kept the RSI embed URL visible below the restored video as a clickable external link in all Ticino post language variants.
- Fixed markdown separation around the Ticino embed/link block so the following heading/content (`## Empowering Response with Advanced Technology`, participation list) is parsed and rendered correctly instead of appearing as raw text.
- Restored the missing featured image + two VideoPress embeds for the Amazonia post variants (EN/DE/FR/IT) using the live source embed IDs.
- Added inline Vimeo embed blocks to legacy posts that only contained plain Vimeo links, while keeping the source link visible below each embed.
- Extended `layouts/blog/single.html` with a featured-image fallback that pulls the first image from rendered post content when front matter does not define `cover.image`/`image`.
- Added `scripts/sync_blog_media_from_offline.py` to reconcile blog markdown media against the offline mirror at `/mnt/xtreme/DV/DEVTMP/opengis_hugo/opengis-offline`.
- Applied that offline sync across all localized blog files, restoring 116 missing embedded videos in 72 files and keeping direct clickable source links under each inserted embed.
- Sanitized ClickUp embeds in `layouts/_default/single.html` by replacing ClickUp iframes with direct links and removing the ClickUp embed script tag from rendered content.
- Reordered right-side navbar controls in `layouts/partials/header/header.html` so the language and theme switchers render at the outermost right edge (after search) on desktop.
- Restored canonical routing for imported `content/pages/**` entries by configuring `permalinks.pages: /:contentbasename/` in the site config, preventing `/pages/...` URL regressions.
- Added translated DE/FR/IT aliases on service/core-values/support/course pages so existing localized menu URLs continue to resolve instead of returning 404.
- Refactored homepage GeoNinjas content into structured YAML (`data/geoninjas.yaml` card/link records) and render it via `layouts/shortcodes/geoninjas.html`, replacing duplicated team-grid markup across localized `_index` markdown files.
- Refactored homepage feature cards into structured YAML data (`data/home_features.yaml`) rendered by `layouts/shortcodes/home-features.html`, ensuring identical icon/image wrapper markup (including the ISO card) across all localized home pages.
- Moved homepage section structure out of localized `_index` markdown HTML into `layouts/index.html`, backed by shared/localized content in `data/homepage.yaml`; localized home markdown files now only carry front matter metadata.
- Normalized `qfield-rapidmapper` image links across all language variants to a stable site-root static image path (`/i0.wp.com/.../qfield-rapidmappera86e.jpg`) with alt text, replacing `wp-json/otter` dynamic `.html` references and brittle relative query-string URLs.
- Added `layouts/shortcodes/blog-video.html` and migrated raw blog embed wrappers from markdown HTML to `{{< blog-video ... >}}` shortcode usage across 104 localized blog post files.
- Added `baseURL: http://localhost:1313/` in `config/development/hugo.yaml` so local alias pages in development do not redirect to the production domain.
- Refactored `data/home_features.yaml` to use localized text fields and updated both homepage render paths (`layouts/index.html` and `layouts/shortcodes/home-features.html`) to resolve feature copy by active language with English fallback.
- Replaced placeholder feature translations in `data/home_features.yaml` with explicit DE/FR/IT localized feature-card copy (titles and bodies).
- Updated GeoNinjas team-filter active chip styling in `assets/sass/styles.scss` to use the site green palette in light and dark mode (instead of Bootstrap blue).
- Hardened service-page layout detection in `_default/single.html` by matching normalized permalink/url paths in addition to trailing slug checks, so `qfield-training` and `qgis-support` consistently use their dedicated hero/header layouts.
- Added an OPENGIS blog layout that mirrors the QField v2 list and single post presentation, including list/card toggles, share buttons, and related posts with dark-mode adjustments.
- Limited blog share icon artwork to a maximum of 50px to match the requested sizing.
- Sized the share buttons to match the 50px icon cap.
- Set the share button icon sizing to 44px for the blog share footer (handled in the site-level Sass bundle).
- Added navbar offset padding for non-home pages via the site-level Sass to keep fixed headers from covering content.
- Updated the navbar offset script to include fixed headers and added a fallback content padding value.
- Applied the `--navbar-offset` variable directly to non-home `#content` so fixed headers no longer cover top content.
- Increased the landing page hero top padding to clear the fixed navbar.
- Updated blog list image selection to avoid global fallbacks and correctly resolve static image paths.
- Reorganized multilingual Services menu entries into nested submenus (Support, Consulting, Courses) to match the expected hierarchy.
- Improved nested dropdown handling in the header partial and Sass for Bootstrap 5, with mobile submenu fallback styling.
- Added optional menu icon rendering in the header partial and configured Bootstrap icon classes for multilingual menu entries.
- Restored the blog list and single templates from `qfield_hugo_v2` to match the prior v2 blog presentation.
- Added the matching v2 blog list/single/related Sass rules to the active site-level stylesheet so the restored templates render with the intended visual design in light and dark mode.
- Corrected the blog single wrapper/container width interplay so title/meta and post content now consistently share the same centered `80%` width.
- Updated blog list behavior to default to card view and to derive card images from the first post content image when no explicit cover/image is provided.
- Added service-page detection in the default single template and applied `80%` width content rules so all multilingual service pages share the expected content width.
- Added a dedicated custom-development page mode in `_default/single.html` (EN/DE/FR/IT slugs) and matching site Sass so the page now renders like the legacy design (social-distancing hero, quote, 3x2 icon cards, CTA) in both light and dark mode.
- Added a dedicated support-contract page mode in `_default/single.html` for `qgis-support`/translated slugs to render the legacy pricing/SLA card layouts from content markdown.
- Added responsive + dark-mode Sass for the support page, plus parser fixes for single-line quote author extraction (`..., CEO`) and duplicated VAT footnotes inside the final SLA card.
- Added a dedicated sustainability-initiative page mode in `_default/single.html` (QGIS sustainability slugs) to render hero + intro/quote + icon sections and support CTA in the legacy style.
- Added matching responsive + dark-mode sustainability styles in `assets/sass/styles.scss` used by the site-level Sass pipeline.
- Refined sustainability page layout alignment so intro/quote blocks match section width, and set the Code Reviews section icon to render on the right on desktop.
- Updated the footer certification mark to use the Swiss Made Software logo image instead of text-chip markup, with responsive sizing and keyboard-focus styles.
- Added the missing consulting submenu entry in multilingual menu configs so Services > Consulting now includes both the consulting-services link and the QField jump-start packages link.
- Set the consulting-services menu icon class to `obfx-menu-icon fa fa-handshake-o` and updated header dropdown icon rendering so legacy `obfx-menu-icon` class sets are emitted unchanged.
- Switched the `_default/single.html` fallback for non-blog pages to a custom-development-style page shell (social-distancing hero, gray background, centered 80% width), and added matching generic single-page content styles with dark-mode support.
- Added a dedicated jump-start packages page mode in `_default/single.html` for `qfield-training`/`qfield-jump-start-packages`, with a left intro block and two pricing cards parsed from markdown plus matching responsive/dark-mode Sass.
- Updated the support page mode in `_default/single.html` to use the same hero/header shell as the other non-blog single pages, and aligned support-page hero width/responsive/dark-mode styling in `assets/sass/styles.scss`.

## Demo

- [https://filipecarneiro.github.io/hugo-bootstrap-theme/](https://filipecarneiro.github.io/hugo-bootstrap-theme/)

## Features

- 🛡️ Security aware
  
  Get A+ scores on Mozilla Observatory out of the box. Easily change the default Security Headers to suit your needs.

- ⚡Fast by default
  
  Get 100 scores on Google Lighthouse by default. Hugo Bootstrap Theme removes unused css, prefetches links, and lazy loads images.
  
- 📈 SEO-ready
  
  Use sensible defaults for structured data, open graph, and Twitter cards. Or easily change the Search Engine Optimization settings to your liking.

## Framework

### Hugo

Hugo is the **world’s fastest static website engine**. It’s written in Go (aka Golang).

- [Hugo Documentation](https://gohugo.io/documentation/)

- [Go template documentation](https://golang.org/pkg/text/template/#hdr-Functions)

### Bootstrap

Get started with Bootstrap

- [Bootstrap 5.3](https://getbootstrap.com/docs/5.3/getting-started/introduction/)

- [Install Bootstrap in your Node.js powered apps with the npm package](https://getbootstrap.com/docs/5.3/getting-started/download/#npm)

### Requirements

The tools used are cross-platform and should work on Windows, MacOS and Linux. You will need the following tools to be downloaded and installed:

- [Hugo static site builder](https://github.com/goHugoio/Hugo/releases) - IMPORTANT: make sure you pick the extended version, Hugo_extended_0.xx.x_…

- [Node & NPM](https://nodejs.org/) - We use this to maintain project dependencies

- [Git](https://git-scm.com/downloads) - This is optional, but highly recommended for version control and remote backups.

## Usage

### Test the theme locally on your computer

Clone this repo:

```
git clone https://github.com/filipecarneiro/hugo-bootstrap-theme.git
```

Test if the site is working:

```
hugo server -D --disableFastRender --source exampleSite
```

This launches Hugo development server and you can see the example site by opening http://localhost:1313/hugo-bootstrap-theme/.

You can also use Hugo as an installed NPM local package. In this case, you don't need to install Hugo globally:

```
npm install
npm run start
```

This will install Hugo in a `bin` subfolder and then run it, using the NPM package `exec-bin`.

### Install on an existing Hugo site

#### Step 1: Install via NPM

```
npm install @filipecarneiro/hugo-bootstrap-theme
```

Hugo bootstrap theme package will also add bootstrap and feather-icons to node modules.

#### Step 2: Add to Config

Then add the theme `hugo-bootstrap-theme` to your sites [configuration file](https://gohugo.io/getting-started/configuration/#configuration-file) `config.toml`, `config.yaml` or `config.json`:

```toml
theme = "hugo-bootstrap-theme"
themesdir = "node_modules/@filipecarneiro"
```

The new themes directory (themesdir) is needed to get the new theme from the `node_modules` folder.

#### Step 3: Test your site

```
hugo server -D --disableFastRender
```

#### Step 4: Check your parameters

Check your `copyright` variable, your menus (the theme supports `main`, `footer` and `social` menus), etc.

Have a look on exampleSite for inspiration :)

### Start from Scratch

#### Step 1: Create a new Hugo site

Follow [Hugo Quick Start](https://gohugo.io/getting-started/quick-start/) to create a new site, add a sample page and change basic settings.

Since you've created an Git repository, let's specify some Hugo files and folders to ignore.

Create a `.gitignore` file on the root of your project with this content:

```txt
public
node_modules
resources
.hugo_build.lock
```

Optionally, add a remote repository and push your code.

#### Step 2: Install and configure Hugo Bootstrap Theme

Update npm to the latest version:

```
npm install -g npm
```

If you don't have npm, [download and install Node.js and npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm).

Then, create an npm package for your site:

```
npm init -y
```

If wanted, you can customize your package information, editing the generated `package.json` file.

Now, install Hugo Bootstrap Theme:

```
npm install @filipecarneiro/hugo-bootstrap-theme --save-dev
```

Then add the theme `hugo-bootstrap-theme` to your site configuration file `config.toml`:

```toml
theme = 'hugo-bootstrap-theme'
themesdir = 'node_modules/@filipecarneiro'
```

Change the existing `theme` value from `ananke` to `hugo-bootstrap-theme` and add a new line for `themesdir`, like above.

Add some [configuration](https://gohugo.io/getting-started/configuration/), like `copyright`, `description` and your menus (the theme supports `main`, `footer` and `social` menus).

Have a look on exampleSite for inspiration :)
