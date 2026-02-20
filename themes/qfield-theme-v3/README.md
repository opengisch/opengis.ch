# Hugo Bootstrap Theme

[![Build and Deploy to gh-pages branch](https://github.com/filipecarneiro/hugo-bootstrap-theme/actions/workflows/gh-pages.yml/badge.svg)](https://github.com/filipecarneiro/hugo-bootstrap-theme/actions/workflows/gh-pages.yml) [![Publish to GitHub Pages](https://github.com/filipecarneiro/hugo-bootstrap-theme/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/filipecarneiro/hugo-bootstrap-theme/actions/workflows/pages/pages-build-deployment)

Theme for a blazing fast static website and/or blog using bootstrap 5.

![Screenshot](https://github.com/filipecarneiro/hugo-bootstrap-theme/blob/main/images/tn.png)

## Local customizations

- Set the site default theme to light via `config/_default/params.toml` (`defaultTheme = "light"`), while keeping dark mode available as a user toggle.
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
