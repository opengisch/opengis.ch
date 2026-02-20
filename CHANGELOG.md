# Changelog

## [Unreleased] - 2026-02-20
- Removed 17 markdown files under `content/**` that contained the moved-page placeholder text `Page has moved`.
- Checked for DE/FR/IT moved-page variants and found no additional localized matches to remove.
- Removed 9 empty directories under `content/` after deleting moved-page placeholder files.
- Restored missing content pages and nested folders from `/mnt/xtreme/DV/DEVTMP/opengis_hugo/converted-md` into `content/pages` using non-overwriting sync (`--ignore-existing`), recovering 4,880 files and 4,718 directories after accidental deletion.
- Removed 685 placeholder markdown files in `content/**` containing `Page not found`, `Page has moved`, `Seite nicht gefunden`, `Page non trouvée`, or `Pagina non trovata`, then deleted 45 empty directories created by that cleanup.
- Flattened localized page trees by moving 2,409 markdown files from `content/pages/de/**`, `content/pages/fr/**`, and `content/pages/it/**` into canonical page folders under `content/pages/**` and renaming them to `*.de.md`, `*.fr.md`, and `*.it.md`; removed the now-empty `de`, `fr`, and `it` root directories.
- Merged 21 localized files from translated top-level slug folders into canonical shared page folders in `content/pages` (including support, consulting, development, values, course registration/calendar, sustainability initiative, crowdfunding, and QField training), then removed the redundant translated source directories.
- Audited `content/pages` recursively for remaining language-split directory names and merged all `*-de`/`*-fr`/`*-it` folders into canonical siblings (`309` files moved and `8` source-only-duplicate files removed); no language-suffixed split directories or empty directories remain.
- Restored `content/pages` from `/mnt/xtreme/DV/DEVTMP/opengis_hugo/converted-md` in non-overwrite mode after accidental over-pruning (`4,877` files and `4,718` directories added), then reapplied language normalization only: moved `3,055` files from `content/pages/de|fr|it/**`, removed `30` source-only duplicates, merged `309` additional recursive `*-de`/`*-fr`/`*-it` split-folder files, and removed `8` more source-only duplicates.

## [Unreleased] - 2026-02-19
- Deduplicated `content/pages` by removing 751 hash-suffixed `index<hash>.md` files where content matched canonical siblings (`index.md` / `index.<lang>.md`) after excluding `source:` front-matter differences.
- Preserved 47 hash-suffixed files intentionally: entries with live hash-link references, content differences, or missing canonical siblings.
- Added `scripts/localize_blog_images.py` to localize blog image references into per-post page-bundle assets.
- Migrated blog markdown image references to local post-folder assets and copied 440 image files into `content/blog/**` (122 post folders).
- Kept 25 image references unresolved because corresponding source files are not present in the local `static/` mirrors (external-only/proxyed assets).
- Removed 360 duplicate original mirror image files from `static/i*.wp.com/**` and `static/wp-content/uploads/**` once equivalent images were bundled into `content/blog/**` post folders.
- Flattened page content structure by moving all children from `content/pages/www.opengis.ch/` into `content/pages/` and removing the domain wrapper directory.
- Removed 220 markdown files in `content/pages/**` that contained the exact `Page not found` string.
- Removed 671 additional localized 404 markdown files in `content/**` containing `Seite nicht gefunden`, `Page non trouvée`, or `Pagina non trovata` (669 from `content/pages`, 2 from `content/blog`).
- Removed all dated duplicate post folders from `content/pages` that were already represented in `content/blog` (`302` folders total), leaving no overlapping dated post directories between the two content trees.
- Removed 241 empty directories under `content/` that remained after deleting duplicate/placeholder pages.

## [Unreleased] - 2026-02-16
- Changed `defaultTheme` from `auto` to `light` in `config/_default/params.toml`, so pages default to light mode on first load while preserving manual dark-mode toggling.
- Hardened service-page detection in `themes/qfield-theme-v3/layouts/_default/single.html` to match normalized permalink/url path segments in addition to trailing slugs, preventing `qfield-training` and `qgis-support` from falling back to the generic single-page branch when rendered with `index.html`-style URLs.
- Updated the support page header in `themes/qfield-theme-v3/layouts/_default/single.html` to use the shared hero style (social-distancing background + centered title), and adjusted support-page Sass in `assets/sass/styles.scss` so width, responsive behavior, and dark-mode hero treatment match other non-blog single pages.
- Added a dedicated jump-start packages layout branch in `themes/qfield-theme-v3/layouts/_default/single.html` for `qfield-training` and `qfield-jump-start-packages`, parsing intro and pricing-card content from markdown and rendering a two-card layout matching the target design.
- Added jump-start page styling in `assets/sass/styles.scss` (intro + card grid, featured card border, pricing typography, CTA buttons, responsive behavior, and dark-mode parity).
- Updated the `_default/single.html` fallback branch to render non-blog single pages in a custom-development-style shell (social-distancing hero header, gray background, and shared 80% content width), while preserving the existing blog single layout; added generic non-blog content styling and dark-mode rules in `assets/sass/styles.scss`.
- Changed the consulting-services submenu icon class to `obfx-menu-icon fa fa-handshake-o` in multilingual menu configs and updated `themes/qfield-theme-v3/layouts/partials/header/header.html` so `obfx-menu-icon` entries are rendered without the appended `dropdown-item-icon` helper class.
- Added the missing nested consulting-services menu entry under Services > Consulting in `config/_default/menus/menus.en.toml`, `config/_default/menus/menus.de.toml`, `config/_default/menus/menus.fr.toml`, and `config/_default/menus/menus.it.toml`, including localized labels and handshake icons.
- Replaced the footer Swiss Made Software text chip in `themes/qfield-theme-v3/layouts/partials/footer/footer.html` with the official logo image asset (`/wp-content/uploads/2020/04/SMS-Logo-1h-72dpi_RGB.png`) and updated footer styles in `assets/sass/styles.scss` for responsive sizing and accessible focus behavior.
- Updated the sustainability page layout so intro/quote blocks use the same width as the main section content and the Code Reviews icon appears on the right side on desktop.
- Added a dedicated sustainability initiative layout branch in `themes/qfield-theme-v3/layouts/_default/single.html` for QGIS sustainability slugs, including hero banner rendering, intro/quote extraction, icon-section parsing, and support CTA extraction from markdown content.
- Added sustainability page styling in `assets/sass/styles.scss` (desktop/mobile + dark mode) to match the legacy look with the social-distancing hero, emphasized quote block, and icon/text section layout.
- Added a dedicated `qgis-support` page layout branch in `themes/qfield-theme-v3/layouts/_default/single.html` (EN/DE/FR/IT slugs), rendering the requested support-plan and SLA card sections from markdown content.
- Added support-page Sass in `assets/sass/styles.scss` to match the target design (tier cards, featured tier borders, slanted green SLA separator), with responsive behavior and dark-mode parity.
- Fixed support-page parser edge cases by correctly splitting one-line quote+author entries ending in `CEO` and by excluding trailing `* ...` VAT footnotes from SLA card details so the footnote is rendered only once.
- Replaced the custom-development service-page fallback rendering with a dedicated parser/layout in `_default/single.html` for EN/DE/FR/IT slugs, reproducing the legacy page structure (hero banner, quote, 3x2 icon cards, CTA), and added matching light/dark responsive styles plus the missing `social_distancing.png` hero asset in `static/wp-content/uploads/2020/04/`.
- Enforced `80%` content width for all service pages (multilingual service slugs from navigation) by tagging service pages in `_default/single.html` and overriding the legacy `860px` content cap for those pages.
- Switched the blog list default view to cards and improved blog card image fallback to use the first image found in post HTML/Markdown content when no front-matter cover/image is defined.
- Corrected blog single width logic so header and body now both resolve to the same centered `80%` content width (removed the accidental double 80% constraint on the header block).
- Aligned the active site Sass override (`assets/sass/styles.scss`) with the restored v2 blog templates by adding blog list/single/related styles and blog-specific content resets so blog pages match the previous v2 visual layout in light and dark mode.
- Ported the QField v2 blog list and post layouts into the v3 theme, including card/list toggles, share buttons, and related post styling with dark mode adjustments.
- Limited share button icon imagery to a 50px maximum width in the blog post footer.
- Expanded share button sizing to enforce 50px icon limits.
- Set share button box and icon sizing to 44px for the blog post footer and moved the rules into the site-level Sass bundle.
- Added navbar offset padding for non-home pages to prevent fixed headers from covering content.
- Ensured the navbar offset script targets fixed headers and provided a fallback padding value for content.
- Applied the `--navbar-offset` value to non-home `#content` to prevent fixed-navbar overlap on page content (including blog posts).
- Increased the landing page hero top padding to account for the fixed navbar height.
- Updated blog list image selection to avoid falling back to global site images and to resolve static paths correctly.
- Reorganized `Services` menu entries (EN/DE/FR/IT) into nested submenu groups for Support, Consulting, and Courses.
- Updated the header dropdown markup and Sass to support second-level submenu rendering in Bootstrap 5, including mobile-friendly submenu layout.
- Fixed a Blog active-state condition in the header partial that compared section values incorrectly.
- Added optional per-menu-entry icon rendering in the header and assigned Bootstrap icon classes to multilingual Services/About/QField submenu items.
- Replaced `themes/qfield-theme-v3/layouts/blog/list.html` and `themes/qfield-theme-v3/layouts/blog/single.html` with the v2 blog templates from `qfield_hugo_v2`.
- Added dark-mode compatibility tweaks for the restored v2 blog templates (`blog-list-hero` and `blog-related` backgrounds plus `text-dark` overrides).
- Replaced the legacy contact block with a fully responsive, localized `opg-contact` section that mirrors the provided artwork and surface all key touch points (call, email, office locations, VAT).
- Crafted a new `opg-footer` that highlights recent blog posts, social profiles, and the Swiss Made badge while preserving the scroll-to-top button and overall dark-mode styling.
- Added `data/social.toml` to centralize the footer icon links and updated the Sass definitions for both contact and footer sections.
- Fine-tuned contact/footer styling for alignment, green accent links, and improved footer list spacing.
- Increased contact section height, reduced overlay darkness, and removed contact-to-footer spacing.
- Matched the legacy layout: simplified contact blocks, adjusted overlay, centered footer social row, and restored the 2022 footer year.
- Increased the contact section height (~40%) and removed the remaining gap between contact and footer.
