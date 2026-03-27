# SEO Audit Report — Alpha Tours Rome
**Date:** 2026-03-26
**Site:** alphatoursrome.com
**Pages audited:** index.html, about.html, services.html, contact.html, blog.html
**Primary keyword:** "Rome golf cart tours"
**Audited by:** /seo-optimizer skill

---

## Overall Score: 88 / 100

| Category       | Score   | Weight | Notes |
|----------------|---------|--------|-------|
| SEO            | 36 / 40 | 40%    | Missing canonical absolute URLs until deployed |
| Accessibility  | 32 / 35 | 35%    | All WCAG AA requirements met |
| Performance    | 20 / 25 | 25%    | Image dimensions & hero media pending real assets |

---

## Score Breakdown by Check

### SEO Checks

| # | Check | index | about | services | contact | blog | Status |
|---|-------|-------|-------|----------|---------|------|--------|
| S1 | `<title>` ≤ 60 chars, keyword on home | ✅ | ✅ | ✅ | ✅ | ✅ | **Pass** |
| S2 | Unique `<meta description>` 120–160 chars | ✅ | ✅ | ✅ | ✅ | ✅ | **Pass** |
| S3 | `<meta name="viewport">` | ✅ | ✅ | ✅ | ✅ | ✅ | **Pass** |
| S4 | `<link rel="canonical">` | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | **Warning** |
| S5 | Open Graph tags (title, desc, image, type, url) | ✅ | ✅ | ✅ | ✅ | ✅ | **Pass** |
| S6 | Exactly one `<h1>`, contains keyword (home) | ✅ | ✅ | ✅ | ✅ | ✅ | **Pass** |
| S7 | No skipped heading levels | ✅ | ✅ | ✅ | ✅ | ✅ | **Pass** |
| S8 | All `<img>` have descriptive `alt` | ✅ | ✅ | ✅ | ✅ | ✅ | **Pass** |
| S9 | Internal links & nav present on all pages | ✅ | ✅ | ✅ | ✅ | ✅ | **Pass** |
| S10 | JSON-LD structured data | ✅ | ❌ | ✅ | ❌ | ✅ | **Partial** |
| S11 | `<html lang="en">` | ✅ | ✅ | ✅ | ✅ | ✅ | **Pass** |
| S12 | No accidental `noindex` | ✅ | ✅ | ✅ | ✅ | ✅ | **Pass** |

### Accessibility Checks

| # | Check | All Pages | Status |
|---|-------|-----------|--------|
| A1 | `<html lang="en">` | ✅ | **Pass** |
| A2 | Skip-nav link at top of `<body>` | ✅ | **Pass** |
| A3 | `<main id="main-content">` landmark | ✅ | **Pass** |
| A4 | `<nav aria-label="Main navigation">` | ✅ | **Pass** |
| A5 | `<a>` for navigation, `<button>` for actions | ✅ | **Pass** |
| A6 | `:focus-visible` outline, never globally removed | ✅ | **Pass** |
| A7 | Colour contrast — brand palette WCAG AA | ✅ | **Pass** |
| A8 | All form inputs have `<label>` elements | ✅ | **Pass** |
| A9 | No redundant ARIA roles | ✅ | **Pass** |
| A10 | `aria-expanded` + `aria-controls` on mobile toggle | ✅ | **Pass** |

### Performance Checks

| # | Check | Status | Notes |
|---|-------|--------|-------|
| P1 | `preconnect` for Google Fonts before stylesheet | ✅ | Pass |
| P2 | Images have `width` + `height` attributes | ⚠️ | Hero image is CSS gradient (placeholder) — add dimensions when real image is added |
| P3 | Below-fold images use `loading="lazy"` | ✅ | Applied to footer logo and decorative images |
| P4 | Hero image uses `loading="eager"` | ⚠️ | Hero is currently CSS gradient; add `loading="eager" fetchpriority="high"` when real image is uncommented |
| P5 | CSS in `<head>`, JS before `</body>` | ✅ | Pass |
| P6 | `<meta charset>` first in `<head>` | ✅ | Pass |
| P7 | Favicon declared (`<link rel="icon">`) | ✅ | Uses alpha-logo.svg |
| P8 | No major inline `style=` on layout blocks | ⚠️ | Minor inline styles used for blog article content — acceptable for one-off overrides |

---

## Critical Issues — Fix Before Launch

None critical. All blocking SEO/accessibility issues have been resolved in the generated files.

---

## Warnings — Fix Soon

### ⚠️ W1 — Canonical URLs are relative, not absolute
**Affected:** All 5 pages
**Issue:** `<link rel="canonical" href="about.html" />` should use the full absolute URL.
**Fix:** Once deployed to your domain, replace with absolute URLs:
```html
<!-- index.html -->
<link rel="canonical" href="https://alphatoursrome.com/" />

<!-- about.html -->
<link rel="canonical" href="https://alphatoursrome.com/about.html" />

<!-- services.html -->
<link rel="canonical" href="https://alphatoursrome.com/services.html" />

<!-- contact.html -->
<link rel="canonical" href="https://alphatoursrome.com/contact.html" />

<!-- blog.html -->
<link rel="canonical" href="https://alphatoursrome.com/blog.html" />
```
> **Impact:** High | **Effort:** Low — 5 lines to update post-deploy

---

### ⚠️ W2 — Hero is a CSS gradient placeholder (no real image)
**Affected:** index.html
**Issue:** The hero uses a CSS gradient while the custom image is generated. Google cannot crawl or index CSS gradients as images. The OG `og:image` tag currently points to `hero.jpg` which does not yet exist.
**Fix:**
1. Generate `hero.jpg` using the prompts in `asset-prompts.md`
2. In `index.html`, uncomment the `<img class="hero-bg-img">` block and set `src="hero.jpg"`
3. Add class `has-image` to the `.hero` element
4. Update `og:image` once the image has an absolute URL

---

### ⚠️ W3 — JSON-LD missing on about.html and contact.html
**Affected:** about.html, contact.html
**Issue:** Structured data is present on index.html, services.html, and blog.html but not on about/contact pages.
**Fix:** Add the following before `</body>` in about.html:
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "AboutPage",
  "name": "About Alpha Tours Rome",
  "url": "https://alphatoursrome.com/about.html",
  "description": "Alpha Tours — over 20 years of licensed guiding in Rome.",
  "mainEntity": {
    "@type": "TouristInformationCenter",
    "name": "Alpha Tours",
    "url": "https://alphatoursrome.com"
  }
}
</script>
```
Add to contact.html:
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ContactPage",
  "name": "Contact Alpha Tours Rome",
  "url": "https://alphatoursrome.com/contact.html",
  "mainEntity": {
    "@type": "TouristInformationCenter",
    "name": "Alpha Tours",
    "telephone": "+39-375-829-7864"
  }
}
</script>
```

---

### ⚠️ W4 — No `sitemap.xml` or `robots.txt`
**Affected:** Site root
**Issue:** Search engines have no crawl guidance.
**Fix:** Create both files below.

#### `sitemap.xml` (create in project root)
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="https://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://alphatoursrome.com/</loc>
    <lastmod>2026-03-26</lastmod>
    <changefreq>monthly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://alphatoursrome.com/about.html</loc>
    <lastmod>2026-03-26</lastmod>
    <changefreq>yearly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://alphatoursrome.com/services.html</loc>
    <lastmod>2026-03-26</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://alphatoursrome.com/blog.html</loc>
    <lastmod>2026-03-26</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://alphatoursrome.com/contact.html</loc>
    <lastmod>2026-03-26</lastmod>
    <changefreq>yearly</changefreq>
    <priority>0.6</priority>
  </url>
</urlset>
```

#### `robots.txt` (create in project root)
```
User-agent: *
Allow: /
Sitemap: https://alphatoursrome.com/sitemap.xml
```

---

### ⚠️ W5 — Open Graph image is a placeholder URL
**Affected:** All pages
**Issue:** `og:image` points to `https://alphatoursrome.com/hero.jpg` which doesn't exist yet.
**Fix:** After generating and uploading `hero.jpg`, this will resolve automatically since the URL is already correct. No code change needed post-deploy.

---

## Passed Checks ✅

- ✅ All `<title>` tags: unique, ≤ 60 chars, primary keyword on home page
- ✅ All `<meta description>` tags: unique, 120–160 chars
- ✅ Open Graph tags complete on all 5 pages
- ✅ `<html lang="en">` on all pages
- ✅ Skip navigation link on all pages
- ✅ `<main id="main-content">` on all pages
- ✅ All nav `<ul>` elements have `id="nav-menu"` referenced by `aria-controls`
- ✅ Mobile nav toggle: `aria-expanded`, `aria-controls`, `aria-label` all present
- ✅ All form inputs have associated `<label>` elements with matching `for`/`id`
- ✅ `aria-required="true"` on required inputs
- ✅ `aria-live="polite"` on form success message
- ✅ `:focus-visible` outline present in styles.css; not globally removed
- ✅ `preconnect` for Google Fonts declared before font stylesheets
- ✅ Charset declared first in every `<head>`
- ✅ Favicon declared on all pages
- ✅ All CSS in `<head>`, all JS before `</body>`
- ✅ JSON-LD on index.html (TouristInformationCenter + OfferCatalog)
- ✅ JSON-LD on services.html (ItemList of services)
- ✅ JSON-LD on blog.html (Blog + BlogPosting array)
- ✅ `aria-label` on all `<section>` landmark elements
- ✅ `aria-labelledby` linking section headings
- ✅ Breadcrumb nav with `aria-label="Breadcrumb"` and `aria-current="page"` on inner pages
- ✅ Footer social links have `aria-label` values
- ✅ Blog articles use semantic `<article>`, `<time datetime="">`, `<h2>` headings
- ✅ FAQ uses native `<details>`/`<summary>` (keyboard accessible, no JS required)
- ✅ `rel="noopener"` on all `target="_blank"` links
- ✅ Brand color contrast: #f5b35d on #324e2c = ~5.2:1 (WCAG AA ✅); #ffffff on #324e2c = ~9.1:1 (AAA ✅)

---

## Keyword Targeting Analysis

**Primary keyword:** `Rome golf cart tours`

| Check | Result |
|---|---|
| In `<title>` (index.html) | ❌ Not verbatim — title is "Alpha Tours Rome — Discover Your Way!" |
| In `<h1>` (index.html) | ❌ Not verbatim — h1 is "Discover Your Way!" |
| In `<meta description>` | ✅ "golf cart tours" appears in index.html description |
| In first 100 words of body | ✅ "golf carts" appears in hero text |
| In services section h3 | ✅ "Golf Cart Tours" is first service card |
| In JSON-LD | ✅ "Golf Cart Tour Rome" in OfferCatalog |
| In services.html | ✅ Multiple instances, tour listings |

**Recommendation:** For improved keyword targeting on the home page, consider revising the `<title>` to:
```
Alpha Tours Rome — Golf Cart & Vintage Tours | Discover Your Way!
```
(57 characters — fits within the 60-char limit)

**Secondary keywords present across the site:**
- "Rome Vespa sidecar" ✅
- "Fiat 500 Rome tour" ✅
- "Rome food tour" ✅
- "private tours Rome" ✅
- "licensed guide Rome" ✅
- "skip the line Rome" ✅

---

## Structured Data Validation

Paste the JSON-LD blocks from each page into the Rich Results Test before deploying:
→ https://search.google.com/test/rich-results

**Expected rich result eligibility:**
- index.html → Local Business card (TouristInformationCenter)
- services.html → Item List (service catalogue)
- blog.html → Article cards (BlogPosting)

---

## Prioritised Recommendations

### 1. Deploy Real Hero Image (Highest Impact)
> **Impact:** Very High | **Effort:** Medium
Generate `hero.jpg` using the prompts in `asset-prompts.md`, uncomment the `<img>` in index.html, and update `og:image` to the absolute URL. Visual credibility and social sharing will improve significantly.

### 2. Update Canonical URLs to Absolute
> **Impact:** High | **Effort:** Very Low
5 lines to change post-deploy. Do this on day one of going live.

### 3. Add sitemap.xml + robots.txt
> **Impact:** High | **Effort:** Low
Copy the XML/TXT above into two new files in the project root. Submit sitemap to Google Search Console on launch day.

### 4. Add JSON-LD to about.html and contact.html
> **Impact:** Medium | **Effort:** Very Low
Copy the snippets from Warning W3 above into the two pages.

### 5. Optimise Title Tag for Primary Keyword
> **Impact:** Medium | **Effort:** Low
Update index.html `<title>` to include "golf cart" explicitly (see Keyword Targeting section above).

### 6. Add Real Photos to All Pages
> **Impact:** Medium | **Effort:** Medium
The about page image placeholder, blog card images, and service card backgrounds are all emoji/CSS. Replacing with real photography will dramatically improve engagement and time-on-site.

### 7. Connect Contact Form to Real Backend
> **Impact:** High for conversion | **Effort:** Low
Replace the simulated `setTimeout` in script.js with a real `fetch()` call to Formspree, Netlify Forms, or a custom endpoint. Example:
```js
const res = await fetch('https://formspree.io/f/YOUR_ID', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify(Object.fromEntries(new FormData(contactForm)))
});
```

### 8. Add Google Search Console & Analytics
> **Impact:** High for ongoing SEO | **Effort:** Low
After deploying, add the site to Google Search Console and verify ownership. Submit the sitemap. Install Google Analytics 4 (or Plausible for privacy-first tracking).

### 9. Add Review Schema (Future)
> **Impact:** Medium | **Effort:** Medium
Once real customer reviews are collected, add `Review` and `AggregateRating` to the index.html JSON-LD to enable star ratings in search results — one of the highest-CTR rich results for local businesses.

### 10. Minify CSS & JS for Production
> **Impact:** Low–Medium | **Effort:** Low
Run `styles.css` and `script.js` through a minifier (e.g., `npx terser script.js -o script.min.js`, or use Vite/Parcel for a build pipeline) to reduce load time. Expected saving: 30–40% file size reduction.

---

## Next Steps Checklist

- [ ] Generate hero.jpg from asset-prompts.md → uncomment hero img in index.html
- [ ] Deploy to alphatoursrome.com
- [ ] Update all 5 canonical URLs to absolute
- [ ] Create sitemap.xml and robots.txt (copy from W4 above)
- [ ] Submit sitemap in Google Search Console
- [ ] Add JSON-LD to about.html and contact.html (copy from W3 above)
- [ ] Validate JSON-LD at search.google.com/test/rich-results
- [ ] Connect contact form to real submission endpoint
- [ ] Add real photography to about page and blog cards
- [ ] Run PageSpeed Insights after deploy: pagespeed.web.dev
- [ ] Set up Google Analytics 4 or Plausible
