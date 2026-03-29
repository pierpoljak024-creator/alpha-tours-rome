# Alpha Tours Website Project

## Brand Identity
- Company: **Alpha Tours** – Rome-based boutique tour company
- Official website: alphatoursrome.com (also www.rome-tourguide.com)
- Phone / WhatsApp: +39 375 829 7864
- Instagram: @alphatoursrome
- Facebook: Rome-Tour-guide-104817567778940
- Based in: Rome, Italy

### Taglines & Slogans (from brochures)
- "Your Local Experts for Unforgettable Experiences!"
- "Discover Rome Your Way!"
- "Live the Dolce Vita!"
- "Let us take the lead"
- "Eat Like a Roman!" (food tours)

### Brand Voice
- Warm, knowledgeable, proud Roman locals
- Emphasise: private, personalised, no group buses, no rushing
- Key differentiators: 20+ years experience, all licensed guides, skip-the-line VIP access
- Tagline adjectives: authentic, unforgettable, local, exclusive

### Footer tagline trio (used in brochures)
- "Local Guides · Authentic Tours · Memorable Moments"

## Color Palette
- Primary Green: #324e2c
- Primary Red: #a71b20
- Cream Background: #fcefe6
- Accent Orange: #f5b35d

## Logo
- **`alpha-logo.svg`** (root, 1.2MB) — full-colour logo with white background, embedded JPEG inside SVG (Canva AI export). Used ONLY in the footer with `loading="lazy"`. Do NOT use as favicon — it is too large.
- **`alpha-logo.png`** (root, 69KB) — web-optimised PNG extracted from the SVG, 200×200px, white background. Use for any light-background contexts.
- **`favicon.png`** (root, 8.7KB) — 64×64px favicon used via `<link rel="icon" href="favicon.png">` on all root pages, `<link rel="icon" href="../favicon.png">` on pages in `tours/`.
- All SVGs in `Branding/` are also 1.2MB Canva JPEG-in-SVG exports — same issue. Do not use them directly in HTML.
- **Logo is NOT shown in the header** (removed by user request). Footer only.

## Brand Assets
```
Branding/
  brand_assets/
    logos/          ← LOGO ALPHA.svg (full branded logo)
      variants/     ← 4.svg (official logo)
    brochures/      ← brochure & marketing photos (jpeg)
      brochure-food-transfer.jpeg   ← food tour + van transfer brochure
      brochure-tours.jpeg           ← golf cart, vespa, fiat 500 brochure
      logo-colosseum.jpeg           ← Colosseum illustration logo
    guidelines/     ← colour-palette.md
    Images/
      Untitled (740 x 416 px) (2)/  ← service card images (740×416, 16:9)
        card-golf-cart-tours.jpg        ← Golf Cart Tours card
        card-vespa-sidecar-tours.jpg    ← Vespa Sidecar card
        card-fiat500-vintage-tour.jpg   ← FIAT 500 Vintage Tour card
        card-food-tours-rome.jpg        ← Food Tours card
        card-private-day-trips.jpg      ← Private Day Trips card
        card-airport-van-transfers.jpg  ← Airport & Hotel Transfers card
      golf-cart-roman-temple-tour-group.jpg  ← golf cart at temple columns with group
      golf-cart-guide-rome-street.jpg        ← guide with golf cart in Rome street
      golf-cart-romes-highlights-private.jpg ← (if exists)
      guests-laughing-pantheon-rome.jpg      ← guests at Pantheon fountain
      guests-inside-golf-cart-rome.jpg       ← guests chatting inside golf cart
      guests-pointing-colosseum-tour.jpg     ← excited guests pointing at Colosseum
      vespa-sidecar-green-colosseum.jpg      ← green Vespa sidecar at Colosseum
      vespa-sidecar-green-trevi-fountain.jpg ← green Vespa sidecar at Trevi Fountain
      fiat500-orange-girls-colosseum.jpg     ← orange Fiat 500, girls at Colosseum
      fiat500-colosseum-two-men.jpg          ← Fiat 500 at Colosseum, two men
      fiat500-orange-church-dusk.jpg         ← orange Fiat 500 at church, dusk
      fiat500-orange-church-piazza-sunny.jpg ← orange Fiat 500 at church piazza, sunny
      wine-cheese-food-tour-rome.jpg         ← wine and charcuterie table
      food-tour-woman-eating-suppli.jpg      ← woman eating supplì on food tour
      van-transfer-colosseum-rome.webp       ← black Mercedes van at Colosseum
```
- Site photos: `hero.jpg` (hero/tours banner), `about.jpg` (food/services banner) — both in project root
- Service card images: `Branding/brand_assets/Images/Untitled (740 x 416 px) (2)/` — all cropped to 740×416px (16:9)
- Always check `Branding/brand_assets/` before using placeholders

## TripAdvisor Assets
```
Tripadvisor/
  tchotel_2025_L.png  ← Travelers' Choice 2025
  tchotel_2024_L.png  ← Travelers' Choice 2024
  tchotel_2023_L.png  ← Travelers' Choice 2023
  2019_en-bk.png      ← Certificate of Excellence 2019 (black)
  2018_en-bk.png      ← Certificate of Excellence 2018 (black)
  2017_en-bk.png      ← Certificate of Excellence 2017 (black)
```
- All 6 badges displayed in the header's top strip across all pages
- Root pages use `Tripadvisor/`, pages in `tours/` use `../Tripadvisor/`

## Services (from brochures — use these exact descriptions)
- **Golf Cart Tours** — Shared & Private. Comfortable & Eco-Friendly. See All Top Landmarks. Flexible & Fun for Everyone. Up to 7 guests.
- **Vespa Sidecar** — Romantic & Unique Ride. Feel the Real Rome. Perfect for Photos & Memories.
- **FIAT 500 Vintage Tour** — Classic Italian Style. Drive Through Iconic Streets. A True Dolce Vita Experience.
- **Food Tours** — "Eat Like a Roman!" Taste Local Specialties. Visit Hidden Trattorias. Wine, Pizza & Gelato. Real Roman Recipes.
- **Van Transfer** — Airport Pick-Up & Drop-Off. Hotel Transfers. Private Day Trips. Comfort & Safety.
- **Private Day Trips** — Tailored escapes to Tivoli, Ostia Antica, Castelli Romani and beyond.

## Content from existing site
- About: Over 20 years of experience, licensed guides
- Contact: +39 375 829 7864, @alphatoursrome, alphatoursrome.com
- FAQ: golf cart capacity (7), cancellation policy, etc.

## Bokun Booking Integration
- Alpha Tours has an **existing Bokun seller account** (currently live on rome-tourguide.com)
- Integration method: **Bokun Booking Widgets** (embeddable iframes/JS from the Bokun dashboard) — NOT the Channel Manager API
- Full implementation plan: `BOKUN-INTEGRATION.md` in the project root
- **Status:** Phase 1 (collecting widget codes) — user must retrieve embed codes from [bokun.io](https://bokun.io) dashboard first
- Booking hub page: `contact.html` — will host all 6 service widgets behind a tab selector
- Anchor convention: `contact.html#book-[slug]` where slugs are: `golf-cart`, `vespa`, `fiat500`, `food-tour`, `transfers`, `day-trips`
- All "Book Now" buttons site-wide must point to `contact.html#book` (or a specific `#book-[slug]`)
- Widget CSS wrapper class: `.bokun-widget-wrap` (brand-styled, green border, cream bg)
- **Do not implement any Bokun code until the user provides the widget embed codes**

## Site Structure (multi-page, already built)
- `index.html` — Home (product showcase, contact strip, services grid, FAQ)
- `about.html` — About
- `services.html` — Services & pricing
- `contact.html` — Booking form
- `blog.html` — Travel tips & stories
- `golf-cart.html`, `vespa.html`, `fiat500.html`, `food-tours.html`, `transfers.html`, `day-trips.html` — 6 category pages
- `tours/*.html` — 18 individual experience pages
- `styles.css` — All brand CSS (custom properties, grid, animations)
- `script.js` — Nav toggle, IntersectionObserver, FAQ accordion, smooth scroll

## Header Structure (3-row white header, applied to all 29 HTML files)
- **Row 1 — TripAdvisor strip**: 6 award badges centered on white background
- **Row 2 — Social strip**: "Follow us" + Instagram/Facebook/WhatsApp icons left, WhatsApp phone number right
- **Row 3 — Navigation**: Full-width nav bar, ALL CAPS links with `|` dividers, green "BOOK NOW" block at far right
- Header is always white (no transparent/scrolled-dark state)
- `--header-height: 175px` (desktop), `145px` (mobile ≤768px)
- No logo in header — logo removed by user request
- To update the header across all pages: write a Node.js script similar to `update-header.mjs` (deleted after use) that replaces from `<a href="#main-content" class="skip-link">` to `</header>` in every HTML file
- **Path prefix**: root files use `Tripadvisor/` and `index.html`; `tours/` files use `../Tripadvisor/` and `../index.html`

## Homepage Sections (in order)
1. Hero (full-width, photo bg, chips linking to category pages)
2. Product Showcase (`#book-now`) — 4 category sections with Bokun Button cards
3. Contact Strip (`#contact-strip`) — green section, 4 contact cards
4. Services Grid — 6 service cards linking to category pages
5. Fiat 500 scroll-driven video
6. FAQ accordion
7. Newsletter form
8. Footer

## Deployment
- **GitHub repo:** https://github.com/pierpoljak024-creator/alpha-tours-rome
- **Branch:** `main`
- **Hosting:** Netlify — auto-deploys on every push to `main`
- To deploy: `git push origin main` (Netlify picks it up automatically, no manual step needed)

### Netlify Configuration (Recommended)
Add a `netlify.toml` file in the project root to optimise caching, redirects, and 404 handling:

```toml
[build]
  publish = "."

[[headers]]
  for = "/*.css"
  [headers.values]
    Cache-Control = "public, max-age=31536000, immutable"

[[headers]]
  for = "/*.js"
  [headers.values]
    Cache-Control = "public, max-age=31536000, immutable"

[[headers]]
  for = "/assets/*"
  [headers.values]
    Cache-Control = "public, max-age=31536000, immutable"

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
```
Also include a `robots.txt` and `sitemap.xml` in the root for SEO.

## Local Dev Server
- Start: `node serve.mjs` (serves project root at `http://localhost:3000`)
- Supports HTTP range requests (required for video scrubbing)
- `serve.mjs` lives in the project root

## Screenshots (local only, not committed)
- Puppeteer: `C:/Users/pierf/.cache/puppeteer/chrome/win64-146.0.7680.153/chrome-win64/chrome.exe`
- Output folder: `temporary screenshots/` (git-ignored)
- Command: `node -e "const p = require('puppeteer'); ..."` using the path above

## Video Assets
- Scroll-driven video: `assets/videos/fiat500-scrub.mp4`
- Source (original): `Branding/brand_assets/Videos/b18b6f51-2e30-42e9-98f0-abb17f5e2e95.mp4`
- Converted with FFmpeg: `-g 1` (keyframe every frame) for smooth scroll scrubbing
- FFmpeg binary: `C:/Users/pierf/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe/ffmpeg-8.1-full_build/bin/ffmpeg.exe`
- To re-convert any video for scroll scrubbing:
  ```
  ffmpeg -i INPUT.mp4 -vf "scale=1920:-2" -c:v libx264 -g 1 -crf 26 -preset slow -an -movflags faststart OUTPUT.mp4 -y
  ```
- **Video optimisation:** For better performance on Netlify free tier, keep the final video under ~5–10 MB. Use `-crf 26` (already set) and consider lowering resolution further if needed (e.g., `scale=1280:-2`). Test file size and playback smoothness.

## Performance & SEO

### Image compression rules
- All images added to `Branding/brand_assets/Images/` MUST be compressed before use.
- DSC/camera photos are typically 19–28MB raw — **always compress with FFmpeg first**:
  ```
  ffmpeg -i INPUT.jpg -vf "scale=900:-2" -q:v 4 OUTPUT.jpg -y
  ```
- Target: 100–300KB per image for web use.
- Never commit raw camera photos to the repo.
- `alpha-logo.svg` is a known 1.2MB file — do not use as `<img>` in performance-sensitive contexts. Use `alpha-logo.png` (69KB) for light backgrounds.

### Caching
- `netlify.toml` is in the project root with `Cache-Control: public, max-age=31536000, immutable` for all static assets.
- HTML files are set to `max-age=0, must-revalidate` so deploys take effect immediately.
- First visit loads all assets; repeat visits use browser cache — no re-download.

### Other SEO
- **Structured data:** JSON-LD for local business present in index.html.
- **Meta tags:** Each page has a unique `<title>` and `<meta name="description">`.
- **Favicon:** `favicon.png` (8.7KB) — used on all pages. Root pages: `favicon.png`, tours/ pages: `../favicon.png`.
- **Accessibility:** Skip links, ARIA labels, semantic HTML, lazy loading on all below-fold images.

## Requirements
- Fully responsive (mobile, tablet, desktop)
- Hero with photo bg, left-aligned text, tour-type filter chips
- Services grid with per-tour gradient image-banner cards
- Scroll-driven Fiat 500 exploded-view video section (homepage)
- "Book Now" button linking to contact page
- Multi-page: Home, About, Services, Contact, Blog
- SEO: meta descriptions, title tags, structured data

---

# Frontend Development Rules

## Skills — Invoke Before Any Frontend Work
- **`frontend-design`** skill: invoke before writing any frontend code, every session, no exceptions
- **`asset-generation`** skill: use to produce image/video prompts for any new visual assets needed
- **`3d-website-builder`** skill: use when scaffolding new pages or major sections
- **`seo-optimizer`** skill: use to audit and fix SEO/accessibility after major changes

> Install the `frontend-design` skill if not present:
> ```
> /plugin marketplace add anthropics/claude-code
> /plugin install frontend-design@claude-code-plugins
> ```

## Reference Images
- If a reference image is provided: match layout, spacing, typography, and color **exactly**. Use placeholder content where real assets are missing (`https://placehold.co/WIDTHxHEIGHT`). Do not improve or add to the design.
- If no reference image: design from scratch with high craft (see guardrails below).
- Screenshot output, compare against reference, fix mismatches, re-screenshot. Do **at least 2 comparison rounds**. Stop only when no visible differences remain or user says so.

## Local Server
- **Always serve on localhost** — never screenshot a `file:///` URL.
- Start the dev server: `node serve.mjs` (serves the project root at `http://localhost:3000`)
- `serve.mjs` lives in the project root. Start it in the background before taking any screenshots.
- If the server is already running, do not start a second instance.

## Screenshot Workflow
- Puppeteer module: `C:/Users/pierf/node_modules/puppeteer`
- Chrome executable: `C:/Users/pierf/.cache/puppeteer/chrome/win64-146.0.7680.153/chrome-win64/chrome.exe`
- **Always screenshot from localhost** — never from `file:///`
- Use inline node script (no `screenshot.mjs`):
  ```js
  node -e "
  const puppeteer = require('C:/Users/pierf/node_modules/puppeteer');
  (async () => {
    const browser = await puppeteer.launch({ executablePath: 'C:/Users/pierf/.cache/puppeteer/chrome/win64-146.0.7680.153/chrome-win64/chrome.exe', headless: true });
    const page = await browser.newPage();
    await page.setViewport({ width: 1400, height: 900 });
    await page.goto('http://localhost:3000', { waitUntil: 'networkidle2' });
    await page.screenshot({ path: 'temporary screenshots/screenshot.png' });
    await browser.close();
  })();
  "
  ```
- Output folder: `temporary screenshots/` (git-ignored)
- After screenshotting, read the PNG with the Read tool
- When comparing, be specific: "heading is 32px but reference shows ~24px", "card gap is 16px but should be 24px"
- Check: spacing/padding, font size/weight/line-height, colors (exact hex), alignment, border-radius, shadows, image sizing

## Output Defaults
- Multi-page site: separate HTML files sharing `styles.css` and `script.js` (already established)
- Tailwind CSS via CDN is acceptable for new standalone prototypes
- Placeholder images: `https://placehold.co/WIDTHxHEIGHT`
- Mobile-first responsive

## Anti-Generic Guardrails
- **Colors:** Always use brand palette (`#324e2c`, `#a71b20`, `#fcefe6`, `#f5b35d`). Never use default Tailwind indigo/blue.
- **Shadows:** Use layered, color-tinted shadows with low opacity — never flat `shadow-md`.
- **Typography:** Pair Playfair Display (headings) with Inter (body). Tight tracking (`-0.03em`) on large headings, generous line-height (`1.7`) on body.
- **Gradients:** Layer multiple radial gradients. Add grain/texture via SVG noise filter for depth.
- **Animations:** Only animate `transform` and `opacity`. Never use `transition-all`. Use spring-style easing (`cubic-bezier(0.22,1,0.36,1)`).
- **Interactive states:** Every clickable element needs hover, focus-visible, and active states. No exceptions.
- **Images:** Add a gradient overlay (`from-black/60`) and optional color treatment with `mix-blend-multiply`.
- **Spacing:** Use CSS custom properties / Tailwind spacing tokens consistently — no random values.
- **Depth:** Use a layering system (base → elevated → floating) — not everything at the same z-plane.

## Hard Rules
- Do not add sections, features, or content not requested
- Do not "improve" a reference design — match it
- Do not stop after one screenshot pass
- Do not use `transition-all`
- Do not use default Tailwind blue/indigo as primary color
- Do not commit files with console.log, TODO comments, or debugging artifacts
- Always test on mobile viewport (375px) before committing
