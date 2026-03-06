# OPENGIS.ch (Hugo)

Hugo site for the OPENGIS.ch marketing website, using the `qfield-theme-v3` bootstrap-based theme.

## Recent updates (March 2, 2026)
- Replaced legacy course-category redirect aliases with real route-backed pages under `content/pages/course-categories/**` (EN/DE/FR/IT), so old WordPress taxonomy URLs such as `/category/courses/qgis-courses/` and localized `/de|fr|it/category/...` paths now load actual content pages instead of redirecting.
- Updated `qgis-courses` category pages (EN/DE/FR/IT) to render archive post cards from language-specific `course_posts` front matter, matching production archive behavior instead of showing the calendar iframe.
- Styled standalone course CTA links in content (for example “Register here”) as green rounded pill buttons in `assets/sass/styles.scss` for calendar/registration routes across EN/DE/FR/IT.
- Restored `course-registration` functionality to match the live site by adding a dedicated registration page renderer in `themes/qfield-theme-v3/layouts/_default/single.html` with language-specific ClickUp form embeds for EN/DE/FR/IT.
- Added registration-form initialization in `themes/qfield-theme-v3/assets/js/main.js` so page query parameters are forwarded to the embedded ClickUp URL and fallback link.
- Added dedicated registration iframe/fallback styling (including dark mode and mobile min-height) in `assets/sass/styles.scss`.
- Removed imported placeholder “Recent Posts” body content from all `content/pages/course-registration/index*.md` files so registration pages render cleanly through the dedicated embed layout.
- Restored `courses-calendar` functionality to match the live site by adding a dedicated calendar page renderer in `themes/qfield-theme-v3/layouts/_default/single.html` with language-specific ClickUp shared-list iframe sources for EN/DE/FR/IT.
- Added dedicated calendar iframe styling (including dark-mode border handling and mobile min-height) in `assets/sass/styles.scss`.
- Removed imported placeholder “Recent Posts” body content from `content/pages/courses-calendar/index.md` so the English calendar page shows the embedded calendar functionality instead of stale list text.
- Added a dedicated `book-private-course` page renderer in `themes/qfield-theme-v3/layouts/_default/single.html` that includes the requested ClickUp iframe embed (`https://forms.clickup.com/f/22wqj-11141/2YYC027R5B98SX991E`) plus a direct-link fallback.
- Added client-side booking-form setup in `themes/qfield-theme-v3/assets/js/main.js` to append current URL query parameters (for example `wpf10757_9`) to the iframe source and fallback link.
- Added `book-private-course` iframe/fallback styles (including dark mode and mobile sizing) in `assets/sass/styles.scss`.
- Fixed QField jump-start booking links in all `content/pages/qfield-training/index*.md` variants to use live `book-private-course` routes (EN/DE/FR/IT) instead of legacy hashed paths (`indexbc77.html`, `index4953.html`) that returned 404.
- Added backward-compatible aliases on `content/pages/book-private-course/index*.md` so old hashed booking URLs (`/book-private-course/indexbc77.html`, `/book-private-course/index4953.html`, and localized equivalents) now resolve.
- Fixed runaway gallery initialization retries in `themes/qfield-theme-v3/assets/js/main.js` so pages without `.gallery-wrapper` elements no longer loop `setTimeout` calls and spam console logs.
- Updated the order-support-contract embed flow to use a data-driven ClickUp URL (`data-clickup-src`) with a persistent fallback link, and disabled iframe auto-loading on localhost by default (override with `?embed_clickup=1`) to prevent local Split/Datadog DNS errors from third-party form scripts.
- Added local-fallback styling and dark-mode-safe helper text for the order support form in `assets/sass/styles.scss`.

## Recent updates (February 25, 2026)
- Restructured site config to match `qfield_hugo_v2`: one canonical `config/_default/hugo.yaml` plus environment overrides in `config/development/hugo.yaml`, `config/staging/hugo.yaml`, and `config/production/hugo.yaml`.
- Consolidated previously split config fragments (`hugo.yaml`, `config/_default/{config,languages,markup,params}.yaml`, and `config/_default/menus/*.yaml`) into `config/_default/hugo.yaml`.
- Removed the previous TOML and split-YAML config files; the active site config now follows a single-file default + env override structure.
- Kept `themes/qfield-theme-v3/theme.toml` as-is because Hugo expects theme metadata in `theme.toml`.
- Fixed a pre-existing table-scope issue from TOML by keeping global Hugo keys (`defaultContentLanguage`, `theme`, `enableRobotsTXT`, etc.) at root scope in `config/_default/hugo.yaml`.
- Backfilled missing blog `image` front matter for 110 localized post files using verified local mirrored assets so cards/social metadata resolve the intended artwork again (including `2024/07/07/qfield-rapid-mapping-ticino`).
- Updated the blog single-post template to render a featured image when `cover.image` or `image` is set, so posts with restored image metadata no longer appear imageless on detail pages.
- Restored the missing embedded RSI video in `2024/07/07/qfield-rapid-mapping-ticino` (EN/DE/FR/IT) by replacing the plain URL link with a responsive iframe embed block.
- Added the RSI embed URL back below the restored iframe in `2024/07/07/qfield-rapid-mapping-ticino` (EN/DE/FR/IT) as a clickable external link.
- Fixed markdown block separation in the same Ticino post variants so the `## Empowering Response with Advanced Technology` section and following list render as markdown (not raw text) after the embed/link block.
- Restored missing featured image + VideoPress embeds for `2023/10/24/qfield-3-0-amazonia-is-here` (EN/DE/FR/IT), including clickable links below both restored players.
- Added Vimeo embed blocks to legacy posts that previously had only plain Vimeo links, so videos render inline again on blog single pages.
- Added a fallback in `themes/qfield-theme-v3/layouts/blog/single.html` to use the first image found in post content when no `cover.image`/`image` front matter is defined.
- Added `scripts/sync_blog_media_from_offline.py` and ran a full offline source comparison (`/mnt/xtreme/DV/DEVTMP/opengis_hugo/opengis-offline`) across all 964 localized blog files.
- Restored 116 missing embedded videos in 72 blog markdown files from the offline source mirror while preserving clickable source links below each embedded player.
- Sanitized ClickUp embeds in the default non-blog single-page renderer (`themes/qfield-theme-v3/layouts/_default/single.html`) by converting ClickUp iframes to direct links and stripping the ClickUp embed script include.
- Reordered the right-side navbar controls so language and theme switchers now sit at the outermost right edge of the desktop navbar (after the search form).
- Restored canonical routing for `content/pages/**` with `permalinks.pages: /:contentbasename/`, so key links resolve at root-style paths (for example `/custom-development/`, `/qgis-support/`, `/core-values/`) instead of `/pages/...`.
- Added DE/FR/IT aliases for translated service/core-values URLs (including related support/course entries), fixing menu-link 404s on paths such as `/de/entwicklung/`, `/fr/developpement/`, and `/it/supporto-qgis/`.
- Refactored the homepage GeoNinjas section into structured YAML data (`data/geoninjas.yaml` with card/link fields) and render it through the shared `{{< geoninjas >}}` shortcode, replacing duplicated team-grid HTML in all localized home files (`content/_index*.md`).
- Refactored the homepage feature-card section (“What makes us special?”) into `data/home_features.yaml` rendered via `{{< home-features >}}`, so the ISO card/icon markup is consistent across EN/DE/FR/IT and no longer duplicated in localized home markdown files.
- Moved homepage section rendering from raw HTML in localized `_index` markdown files into `layouts/index.html`, and centralized shared/localized homepage copy in `data/homepage.yaml`; `content/_index*.md` now contains front matter only.
- Normalized `qfield-rapidmapper` image sources in all language variants (`content/pages/qfield-rapidmapper/index*.md`) to a stable site-root static image path (`/i0.wp.com/.../qfield-rapidmappera86e.jpg`) with alt text, replacing broken `wp-json/otter` dynamic `.html` references and brittle relative query-string URLs.
- Added a reusable `blog-video` shortcode (`themes/qfield-theme-v3/layouts/shortcodes/blog-video.html`) and replaced raw iframe wrapper HTML in 104 localized blog files with `{{< blog-video ... >}}`, keeping blog markdown content-focused while layout code owns embed markup.
- Set a development-only `baseURL` override (`config/development/hugo.yaml` -> `http://localhost:1313/`) so local alias URLs like `/de/kurskalender/` and `/de/entwicklung/` resolve/redirect on localhost instead of jumping to `https://www.opengis.ch/`.
- Refactored `data/home_features.yaml` to support localized feature content (`title.<lang>` / `body.<lang>`) and updated homepage feature rendering to use language-specific values with English fallback.
- Replaced placeholder feature translations in `data/home_features.yaml` with explicit DE/FR/IT localized copy for all homepage feature cards.
- Changed the active GeoNinjas team-filter chip color from blue to the site green palette (light + dark mode) in `assets/sass/styles.scss`.
- Added localization-ready homepage service content in `data/homepage.yaml` (`alt.<lang>`, `title.<lang>`, `tagline.<lang>`, `body.<lang>`) and updated `layouts/index.html` to render service text with current-language lookup plus English fallback.
- Replaced placeholder English values in homepage service localizations with real `de`/`fr`/`it` copy for all service cards (`alt`, `title`, `tagline`, `body`) in `data/homepage.yaml`.
- Restored the missing Swiss Made Software badge image at `static/wp-content/uploads/2020/04/SMS-Logo-1h-72dpi_RGB.png`, fixing 404s for footer and page references that use `/wp-content/uploads/2020/04/SMS-Logo-1h-72dpi_RGB.png`.
- Fixed support-contract CTA links in all `qgis-support` language pages to use the canonical route `../order-support-contract/?days=...` instead of non-generated legacy paths like `index7ac1.html`.
- Added legacy aliases to `content/pages/order-support-contract/index*.md` so old hashed URLs (`index7ac1.html`, `index58b3.html`, `indexe55b.html`, `indexdc5b.html`) continue to resolve in EN/DE/FR/IT.
- Added a dedicated `order-support-contract` render branch in `themes/qfield-theme-v3/layouts/_default/single.html` that embeds the ClickUp form iframe (`id="cu-form"`) and maps `?days=` URL parameters to form `Plan`/`Days` query values (2, 5, 10, 0).
- Added `order-support-contract` iframe styling in `assets/sass/styles.scss`, including dark-mode border handling and mobile min-height sizing so the embedded form remains visible and usable across themes/devices.
- Added homepage GeoNinjas team filtering in `layouts/index.html`: dynamic filter chips (`ALL` + teams), card-level `data-team` tags, and client-side show/hide logic so visitors can filter ninjas by team.
- Added GeoNinjas filter labels to shared homepage data (`data/homepage.yaml`: `geoninjas_teams_heading`, `geoninjas_teams_caption`) and matching styles/dark-mode/mobile behavior in `assets/sass/styles.scss`.
- Restyled the homepage clients section in `assets/sass/styles.scss` to a large 3-column logo wall (with light panel background, centered logo cells, larger logo sizing, and spacing) plus responsive 2/1-column breakpoints to match the provided reference layout.
- Moved GeoNinjas filtering logic from inline homepage markup into `themes/qfield-theme-v3/assets/js/main.js` and removed inline scripts from `layouts/index.html`, making team filtering CSP-compatible (`script-src 'self' ...`) again.
- Moved `order-support-contract` ClickUp `?days=` handling from inline script in `themes/qfield-theme-v3/layouts/_default/single.html` into `themes/qfield-theme-v3/assets/js/main.js` to avoid CSP inline-script violations.
- Restored the missing newsletter background image path by adding `static/wp-content/uploads/2019/04/beetruck_banner_1800x530@2x.jpg` from existing mirrored assets, fixing the reported local 404.
- Added Bootstrap Icons to GeoNinjas social/link pills (`GitHub`, `Twitter`, `LinkedIn`, `Mastodon`, `Website`) in both homepage rendering (`layouts/index.html`) and the shared `geoninjas` shortcode (`themes/qfield-theme-v3/layouts/shortcodes/geoninjas.html`), plus icon-aligned pill styling in `assets/sass/styles.scss`.
- Updated GeoNinjas social/link pills to icon-only buttons (no text labels) while preserving accessibility via `aria-label` and `title` attributes in both `layouts/index.html` and `themes/qfield-theme-v3/layouts/shortcodes/geoninjas.html`; adjusted pill sizing in `assets/sass/styles.scss`.
- Adjusted GeoNinjas card typography in `assets/sass/styles.scss` to match the requested look (name/role/team sizing and casing), and kept displayed team labels in `layouts/index.html` as full values (e.g., `Team QField`) instead of stripped uppercase variants.
- Improved GeoNinjas card composition with a new `team-card__body` wrapper (in both homepage and shortcode renderers), refined avatar/text/icon spacing, preserved side-by-side mobile card layout, and added dark-mode contrast refinements for card borders and icon pills in `assets/sass/styles.scss`.

## Recent updates (February 20, 2026)
- Removed 17 markdown files in `content/**` containing the placeholder text `Page has moved` and pruned 9 newly empty directories left behind after the cleanup.
- Restored missing `content/pages/**` files and subfolders from `/mnt/xtreme/DV/DEVTMP/opengis_hugo/converted-md` (no overwrite mode), recovering 4,880 files and 4,718 directories after accidental deletion.
- Ran a targeted post-restore cleanup pass removing 685 placeholder markdown files (`Page not found`, `Page has moved`, `Seite nicht gefunden`, `Page non trouvée`, `Pagina non trovata`) and pruned 45 empty directories.
- Flattened multilingual page structure by moving all files from `content/pages/de|fr|it/**` into shared page folders under `content/pages/**` and renaming them as language-specific files (`*.de.md`, `*.fr.md`, `*.it.md`), removing the separate `de`, `fr`, and `it` subtree roots.
- Consolidated translated top-level page slug folders into canonical shared page folders (for example `support-qgis` + `supporto-qgis` + `qgis-support-wartung` into `qgis-support`), moving 21 localized files and removing the redundant source folders.
- Ran a recursive `content/pages` language-folder audit and merged all remaining `*-de`/`*-fr`/`*-it` split folders into canonical siblings (309 files moved in this pass), leaving no language-suffixed split directories and no empty folders.
- Restored missing `content/pages/**` content again from `/mnt/xtreme/DV/DEVTMP/opengis_hugo/converted-md` after accidental over-pruning (`4,877` files, `4,718` directories), then reapplied only language-folder normalization (`3,055` moves from `de|fr|it` trees and `309` recursive suffix-folder merges) while keeping non-language slugs such as `...-it` untouched.

## Recent updates (February 19, 2026)
- Deduplicated `content/pages` by removing 751 hash-suffixed `index<hash>.md` files that matched canonical `index.md`/`index.<lang>.md` content (ignoring `source:`), while keeping referenced, content-different, and no-canonical edge-case files.
- Added `scripts/localize_blog_images.py` and migrated blog content image references so each blog post folder now contains its own local image assets where source files are available in `static/` (440 bundled images across 122 post folders), with unresolved external-only sources reported separately.
- Removed 360 duplicate source images from legacy original asset mirrors (`static/i*.wp.com/**` and `static/wp-content/uploads/**`) when those files were already bundled inside blog post folders under `content/blog/**`, and pruned empty mirror directories.
- Flattened the `content/pages` tree by moving all `content/pages/www.opengis.ch/*` entries directly under `content/pages/` and removing the `www.opengis.ch` wrapper folder.
- Removed 220 markdown pages in `content/pages/**` containing the exact `Page not found` text to clean out placeholder/404-style imported content pages.
- Removed an additional 671 localized 404-like markdown files (`Seite nicht gefunden`, `Page non trouvée`, `Pagina non trovata`) from `content/**` (669 in `content/pages`, 2 in `content/blog`).
- Removed all dated blog-post duplicate folders from `content/pages` that were already present in `content/blog` (`302` folders removed, leaving `0` overlapping dated post folders).
- Removed all remaining empty directories under `content/` after the cleanup passes (`241` empty folders removed).

## Recent updates (February 16, 2026)
- Changed `defaultTheme` to `light` (now in `config/_default/hugo.yaml` under `params.defaultTheme`), so first-load theme selection defaults to light mode while still allowing users to toggle dark mode.
- Hardened non-blog service-page layout detection in `themes/qfield-theme-v3/layouts/_default/single.html` by matching normalized permalink/url paths (not only trailing slug), ensuring `qfield-training` and `qgis-support` consistently render their dedicated hero/header layouts even when URLs resolve via `index.html`.
- Fixed non-home page content overlap by applying the fixed-navbar offset to `#content` with a safe fallback value.
- Reworked main navigation structure so Services now renders nested submenus (Support, Consulting, Courses) with second-level links across translated menus.
- Improved nested dropdown behavior in the header template/styles for Bootstrap 5, including mobile-friendly submenu layout.
- Restored optional menu entry icons (Bootstrap Icons) for nested navigation items and wired icon classes into the multilingual menu configuration.
- Replaced the current blog list and single templates with the `qfield_hugo_v2` versions to match the previous layout and interaction pattern.
- Synced the active site-level Sass overrides with the restored v2 blog templates so blog list/single/related sections render with the expected v2 styling in both light and dark mode.
- Corrected blog single width logic so title/meta and article body now both render at the same centered `80%` width.
- Set blog list default view to cards and made card thumbnails fall back to the first image in post content (HTML/Markdown) when no cover/image front matter is set.
- Applied the same centered `80%` content width to all service pages across EN/DE/FR/IT service slugs by targeting service pages in the default single-page layout.
- Implemented a dedicated custom-development page renderer (EN/DE/FR/IT) that mirrors the legacy structure: hero banner image, quote block, six icon cards in a 3-column grid, and contact CTA, with matching responsive and dark-mode styling.
- Added a dedicated `qgis-support` layout mode (EN/DE/FR/IT slugs) in `_default/single.html` that renders the two target sections from the legacy design: support plan pricing cards and SLA cards with highlighted tiers.
- Added full responsive/dark-mode Sass for the support contracts page and fixed parser edge cases for localized one-line quote+author content while preventing footnote duplication inside SLA cards.
- Added a dedicated sustainability-initiative layout mode in `_default/single.html` (QGIS sustainability slugs) with a hero banner, intro/quote block, structured icon sections, and support CTA to match the legacy page composition.
- Added matching responsive/dark-mode styling for the sustainability initiative page in the active site stylesheet `assets/sass/styles.scss`.
- Adjusted sustainability page alignment so the top intro/quote text uses the same content width as the sections below, and moved the Code Reviews section icon to the right side on desktop.
- Replaced the footer Swiss Made Software text chip with the official logo image (`/wp-content/uploads/2020/04/SMS-Logo-1h-72dpi_RGB.png`) while keeping responsive sizing and accessible focus styling.
- Restored the missing consulting submenu entry by adding a dedicated “Consulting services” item (plus localized DE/FR/IT equivalents) under the nested Services > Consulting menu.
- Updated the consulting-services submenu icon class to `obfx-menu-icon fa fa-handshake-o` and adjusted header icon rendering to preserve exact `obfx-menu-icon` classes without appending Bootstrap icon helper classes.
- Updated the default non-blog single-page renderer in `_default/single.html` so all non-blog pages (including Consulting services and QField Jump-start packages) use the same custom-development style shell for header, background, and `80%` content width, while blog pages keep the blog layout.
- Added a dedicated jump-start packages layout mode for `qfield-training` and `qfield-jump-start-packages` in `_default/single.html`, rendering the requested two-card pricing section (intro column + Half day / Full day cards) from markdown content with responsive and dark-mode styling.
- Updated the `qgis-support` single-page header to use the same hero shell as other non-blog single pages (social-distancing background, centered title, and matching width behavior) instead of the plain blog-style header.

## Recent updates (February 4, 2026)
- Recreated the blog list and post layouts to mirror the QField v2 presentation (list/card toggle, share bar, related posts) with dark-mode-friendly styling.
- Capped the share button icon artwork at 50px wide on blog posts.
- Ensured share button icons are constrained to 50px with matching button sizing.
- Set the share button icon sizing to 44px for the blog share footer via the site-level Sass bundle.
- Added navbar offset padding for non-home pages so the fixed header does not overlap content.
- Updated the navbar offset script to include fixed headers and added a fallback padding value.
- Increased the landing page hero top padding to clear the fixed navbar.
- Updated blog list image selection to avoid global fallbacks and correctly resolve static image paths.

## Recent updates (January 29, 2026)
- Rebuilt the contact section with a full-width hero background, localized copy blocks, and clearer call-to-action elements that match the reference design.
- Introduced a dark footer that surfaces the latest blog posts, social links, and the Swiss Made badge while keeping the optional scroll-to-top helper.
- Polished the contact/footers visuals (centered heading, green accent links, tighter post list spacing) to align with the final reference.
- Increased contact section height, softened the image overlay, and removed the gap to the footer.
- Restyled contact/footer layout to match the legacy reference (left-aligned contact text, simpler blocks, centered social row, fixed copyright year).
- Increased contact section height and removed the residual gap between the contact and footer sections.
- Added shared social metadata so the footer can render the correct icons without duplicating logic.

## Local workflow
1. Install Hugo (extended) in your environment.
2. Run `hugo` from the repo root to build the site into `public` or `hugo server` for live preview.
3. The Sass pipeline lives in `assets/sass/styles.scss`; changes will be bundled automatically by Hugo modules.
