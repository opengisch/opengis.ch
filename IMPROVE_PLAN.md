# Hugo & Bootstrap Improvement Plan

> Based on comprehensive analysis completed on March 13, 2026  
> See [HUGO_BOOTSTRAP_ANALYSIS.md](HUGO_BOOTSTRAP_ANALYSIS.md) for detailed findings

## Progress Overview

- **Status:** 0/17 items completed
- **High Priority:** 0/3 completed
- **Medium Priority:** 0/6 completed  
- **Low Priority:** 0/8 completed

---

## High Priority 🔴

### Performance & Optimization

- [ ] **Enable PostCSS with Autoprefixer**
  - Location: `themes/qfield-theme-v3/layouts/partials/head/stylesheet.html`
  - Action: Uncomment and configure PostCSS options
  - Expected Impact: Better browser compatibility, automated vendor prefixing
  - Effort: Low (1-2 hours)

- [ ] **Optimize Bootstrap Bundle (CSS)**
  - Location: `themes/qfield-theme-v3/assets/sass/main.scss`
  - Action: Import only needed Bootstrap components instead of full bundle
  - Expected Impact: 30-50% reduction in CSS bundle size
  - Effort: Medium (3-4 hours)
  - Components to evaluate:
    - [ ] Functions (required)
    - [ ] Variables (required)
    - [ ] Mixins (required)
    - [ ] Utilities (required)
    - [ ] Root (required)
    - [ ] Reboot (required)
    - [ ] Grid system (required)
    - [ ] Buttons (required)
    - [ ] Navbar (required)
    - [ ] Dropdown (required)
    - [ ] Cards (required)
    - [ ] Alerts (evaluate if needed)
    - [ ] Carousel (evaluate if needed)
    - [ ] Other components (audit usage)

### Accessibility

- [ ] **Add Skip Navigation Link**
  - Location: `themes/qfield-theme-v3/layouts/_default/baseof.html`
  - Action: Add skip link before header for keyboard users
  - Expected Impact: Critical accessibility improvement
  - Effort: Low (30 minutes)
  ```html
  <a href="#content" class="skip-link visually-hidden-focusable">Skip to main content</a>
  ```

---

## Medium Priority 🟡

### Performance

- [ ] **Improve Font Loading Strategy**
  - Location: `assets/sass/styles.scss`
  - Current: Google Fonts loaded via CSS @import
  - Actions:
    - [ ] Add preconnect links to `<head>`
    - [ ] Consider self-hosting fonts for better control
    - [ ] Use font-display: swap for better perceived performance
  - Expected Impact: Improved LCP (Largest Contentful Paint)
  - Effort: Medium (2-3 hours)

- [ ] **Implement Critical CSS Extraction**
  - Action: Extract above-the-fold CSS and inline it
  - Tools to consider: Hugo's `resources.PostCSS` with PurgeCSS
  - Expected Impact: Faster FCP (First Contentful Paint)
  - Effort: Medium (4-6 hours)

- [ ] **Optimize Bootstrap JavaScript Bundle**
  - Location: `themes/qfield-theme-v3/assets/js/`
  - Action: Import only needed Bootstrap JS modules
  - Expected Impact: Reduced JavaScript bundle size
  - Effort: Medium (2-3 hours)

### Security

- [ ] **Enhance Content Security Policy**
  - Location: `themes/qfield-theme-v3/layouts/partials/head/content-security-policy.html`
  - Current Issue: `style-src 'unsafe-inline'` allowed
  - Actions:
    - [ ] Move inline styles to external stylesheet
    - [ ] Or implement nonce-based CSP for inline styles
    - [ ] Update CSP header to remove 'unsafe-inline'
  - Expected Impact: Enhanced XSS protection
  - Effort: Medium (3-4 hours)

- [ ] **Add SRI Hashes for Font Awesome**
  - Location: `themes/qfield-theme-v3/layouts/partials/head/stylesheet.html`
  - Current: Loading from static folder without integrity hashes
  - Action: Add fingerprinting and integrity attributes
  - Expected Impact: Better security validation
  - Effort: Low (1 hour)

### SEO & Content

- [ ] **Audit All Images for Alt Text**
  - Action: Review all images across the site
  - Tools: Use automated accessibility scanner
  - Expected Impact: Better SEO and accessibility
  - Effort: High (depends on image count)
  - Deliverable: Create spreadsheet of images needing alt text

---

## Low Priority 🟢

### Code Quality & Maintainability

- [ ] **Add Partial Documentation**
  - Location: All files in `themes/qfield-theme-v3/layouts/partials/`
  - Action: Add JSDoc-style comments explaining parameters and usage
  - Expected Impact: Better maintainability and team onboarding
  - Effort: Medium (3-4 hours)
  - Example format:
  ```html
  {{/*
    Partial: image.html
    Description: Renders responsive images with srcset
    Parameters:
      - src (string, required): Path to image
      - alt (string, required): Alt text
      - class (string, optional): CSS classes
      - loading (string, optional, default: "lazy"): Loading strategy
    Usage: {{ partial "image.html" (dict "src" "path/to/image.jpg" "alt" "Description") }}
  */}}
  ```

- [ ] **Implement JavaScript Build Process**
  - Action: Set up modern bundler (esbuild, rollup, or webpack)
  - Benefits:
    - [ ] Tree shaking for unused code
    - [ ] Code splitting for better caching
    - [ ] Better optimization
    - [ ] TypeScript support (optional)
  - Expected Impact: Smaller, more optimized JavaScript
  - Effort: High (6-8 hours)

- [ ] **Remove Console Logs in Production**
  - Location: `themes/qfield-theme-v3/assets/js/main.js`
  - Action: Strip console.log statements in production build
  - Expected Impact: Cleaner production code, slightly smaller file size
  - Effort: Low (1 hour if using build process)

- [ ] **Convert Configuration to TOML**
  - Location: `config/_default/hugo.yaml` and environment configs
  - Action: Convert YAML files to TOML format
  - Expected Impact: Minor performance improvement in Hugo
  - Effort: Low (1-2 hours)
  - Note: This is subjective; YAML is also fine

- [ ] **Enhance Image Processing with Hugo's Page Resources**
  - Location: `themes/qfield-theme-v3/layouts/partials/image.html`
  - Action: Refactor to use `.Page.Resources` for better integration
  - Expected Impact: Better integration with Hugo's asset pipeline
  - Effort: Medium (3-4 hours)

### Testing & Quality Assurance

- [ ] **Integrate Tests into CI/CD Pipeline**
  - Location: Create `.github/workflows/` or similar
  - Action: Set up automated testing on pull requests
  - Tests to run:
    - [ ] Python tests (existing test files)
    - [ ] HTML validation
    - [ ] Accessibility audit (axe-core, pa11y)
    - [ ] Lighthouse CI
  - Expected Impact: Catch regressions early
  - Effort: Medium (4-6 hours)

- [ ] **Set Up Automated Accessibility Testing**
  - Tools to consider:
    - [ ] axe-core (automated)
    - [ ] pa11y (automated)
    - [ ] Lighthouse (automated)
    - [ ] Manual WCAG 2.1 AA audit (comprehensive)
  - Expected Impact: Ensure ongoing accessibility compliance
  - Effort: Medium (3-4 hours setup + ongoing)

- [ ] **Monitor Core Web Vitals**
  - Action: Set up monitoring for:
    - [ ] LCP (Largest Contentful Paint) - Target: < 2.5s
    - [ ] FID (First Input Delay) - Target: < 100ms
    - [ ] CLS (Cumulative Layout Shift) - Target: < 0.1
  - Tools: Google Search Console, WebPageTest, Lighthouse
  - Expected Impact: Data-driven performance improvements
  - Effort: Low (1-2 hours setup)

---

## Optional Enhancements 🔵

### Nice to Have

- [ ] **Implement Service Worker for Offline Support**
  - Action: Add PWA capabilities
  - Effort: High (8-10 hours)

- [ ] **Add WebP/AVIF Image Format Support**
  - Action: Generate modern image formats with fallbacks
  - Effort: Medium (2-3 hours)

- [ ] **Implement Resource Hints**
  - Action: Add dns-prefetch, preconnect, preload where appropriate
  - Effort: Low (1-2 hours)

- [ ] **Set Up Automated Dependency Updates**
  - Tool: Dependabot or Renovate
  - Effort: Low (1 hour)

---

## Completed Items ✅

_Items will be moved here as they are completed_

---

## Notes

- **Effort Estimates:** Based on developer with moderate Hugo/Bootstrap experience
- **Testing Required:** All changes should be tested locally before deployment
- **Dark Mode:** Ensure all improvements maintain dark mode functionality
- **Multilingual:** All changes must work across all 4 languages (en, de, fr, it)

---

## Next Steps

1. **Review and prioritize** items based on business needs
2. **Assign owners** to each task
3. **Set deadlines** for high priority items
4. **Create branches** for each major improvement
5. **Test thoroughly** before merging to main

---

## Resources

- [Hugo Documentation](https://gohugo.io/documentation/)
- [Bootstrap 5.3 Documentation](https://getbootstrap.com/docs/5.3/)
- [Web.dev Performance](https://web.dev/performance/)
- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [MDN Web Docs](https://developer.mozilla.org/)

---

**Last Updated:** March 13, 2026  
**Status:** Ready for implementation
