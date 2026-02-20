# OPENGIS.ch (Hugo)

Hugo site for the OPENGIS.ch marketing website, using the `qfield-theme-v3` bootstrap-based theme.

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
- Changed `defaultTheme` to `light` in `config/_default/params.toml`, so first-load theme selection defaults to light mode while still allowing users to toggle dark mode.
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
