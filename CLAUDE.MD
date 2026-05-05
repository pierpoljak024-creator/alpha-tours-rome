della modifica del sito we# Alpha Tours Website Project

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
- **`assets/images/logos/alpha-logo.svg`** (1.2MB) — full-colour logo with white background, embedded JPEG inside SVG (Canva AI export). Used ONLY in the footer with `loading="lazy"`. Do NOT use as favicon — it is too large.
- **`assets/images/logos/alpha-logo.png`** (69KB) — web-optimised PNG extracted from the SVG, 200×200px, white background. Use for any light-background contexts.
- **`assets/images/logos/logo-ufficiale-header.png`** (52KB, 300×200px) — full-colour official logo extracted from `design/brand/brand_assets/logos/logo ufficiale.svg` and processed with FFmpeg (`colorkey` to remove black BG, white fill, scale=300). Shows Italian flag, sun, Colosseum illustration. Used in the header TA strip at `height: 62px`.
- **`assets/images/favicon.png`** (8.7KB) — 64×64px favicon used via `<link rel="icon" href="assets/images/favicon.png">` on all root pages, `<link rel="icon" href="../assets/images/favicon.png">` on pages in `tours/`.
- All SVGs in `design/brand/` are also 1.2MB Canva JPEG-in-SVG exports — same issue. Do not use them directly in HTML.
- **Logo shown in header TA strip** (left of TripAdvisor badges, separated by a divider). Hidden on mobile (`display:none`). Footer also shows logo.

## Brand Assets
> **Note:** `design/` is gitignored — these files exist locally only, not deployed to Netlify.
```
design/brand/
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
      catacomb-appian-way-rome.jpg           ← Appian Way/catacomb photo (228KB, from _DSC0090, 1400px wide) — card image for Ancient Catacomb & Appian Way
      food-tour-testaccio-rome.jpg           ← Testaccio food tour photo (87KB, from IMG_2169, 1400px wide) — card image for Walking Food Tour — Testaccio
      food-tour-walking-tastings-rome.jpg    ← Food tour with tastings photo (129KB, from DSCF3613, 1400px wide) — card image for Walking Food Tour with Tastings
      10f5bb64-7883-4128-9496-d5238dfb9568.webp ← Gladiators/Colosseum arena photo (77KB) — card image for Gladiators — Colosseum Arena Floor
      4beafc2b-c554-46f7-b917-08f5be7fb4cc.webp ← VIP van tour photo (72KB) — card image for Discover Rome by Van — VIP
```
- Site photos: `assets/images/hero.jpg` (hero/tours banner), `assets/images/about.jpg` (food/services banner)
- Service card images: `design/brand/brand_assets/Images/Untitled (740 x 416 px) (2)/` — all cropped to 740×416px (16:9) — **local only, not in git**
- Always check `design/brand/brand_assets/` before using placeholders

## TripAdvisor Assets
```
assets/images/tripadvisor/
  tchotel_2025_L.png  ← Travelers' Choice 2025
  tchotel_2024_L.png  ← Travelers' Choice 2024
  tchotel_2023_L.png  ← Travelers' Choice 2023
  2019_en-bk.png      ← Certificate of Excellence 2019 (black)
  2018_en-bk.png      ← Certificate of Excellence 2018 (black)
  2017_en-bk.png      ← Certificate of Excellence 2017 (black)
```
- All 6 badges displayed in the header's top strip across all pages
- Root pages use `assets/images/tripadvisor/`, tours/ pages use `../assets/images/tripadvisor/`

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

## Contact Form
- **Status: LIVE** — Netlify Forms handling all submissions
- Form is in `contact.html` — fields: name, email, phone, tour, date, guests, message
- Submissions stored in Netlify dashboard: app.netlify.com → Sites → alphatoursrome → Forms → contact
- Email notifications configured to: `Waleedzsc@gmail.com` and `Mahyinarahmed@gmail.com`
- Honeypot spam protection enabled (`data-netlify-honeypot="bot-field"`)
- JS in `script.js` does a real `fetch()` POST to Netlify — no fake simulation

## WhatsApp Floating Button
- **Status: LIVE** — present on all 30 HTML pages (root + tours/)
- CSS in `styles.css` under `/* ── WhatsApp Floating Button ── */`
- HTML injected before `</body>` on every page — class `.whatsapp-float`
- Links to `https://wa.me/393758297864` with pre-filled message
- Desktop: green pill with "Chat with us!" label, bottom-right corner
- Mobile (<480px): collapses to icon-only circle
- Pulse ring animation draws attention without being intrusive

## Bokun Booking Integration
- Alpha Tours has an **existing Bokun seller account** (currently live on rome-tourguide.com)
- Integration method: **Bokun Booking Widgets** (embeddable iframes/JS from the Bokun dashboard) — NOT the Channel Manager API
- Full implementation plan: `docs/BOKUN-INTEGRATION.md`
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
- **Row 1 — TripAdvisor strip**: Logo (`logo-ufficiale-header.png`) on left with divider, then 6 award badges in chronological order (2017→2025). Logo hidden on mobile.
- **Row 2 — Social strip**: "Follow us" + Instagram/Facebook/WhatsApp icons left, WhatsApp phone number right
- **Row 3 — Navigation**: Full-width nav bar, ALL CAPS links with `|` dividers, green "BOOK NOW" block at far right
- **Desktop**: `position: relative` — header scrolls away naturally with the page (NOT sticky/fixed)
- **Mobile**: `position: fixed; top: 0` — sticky, hides on scroll down (after 60px), reveals on scroll up
- `--header-height: 175px` (desktop), `145px` (mobile ≤768px)
- Badge and logo height: `62px` desktop, `46px` mobile
- To update the header across all pages: write a Node.js script similar to `update-header.mjs` (deleted after use) that replaces from `<a href="#main-content" class="skip-link">` to `</header>` in every HTML file
- **Path prefix**: root files use `assets/images/tripadvisor/` and `assets/images/logos/logo-ufficiale-header.png`; `tours/` files use `../assets/images/tripadvisor/` and `../assets/images/logos/logo-ufficiale-header.png`

## Homepage Sections (in order)
1. Hero (full-width, photo bg, chips linking to category pages)
2. Product Showcase (`#book-now`) — 4 category sections with Bokun Button cards
3. Contact Strip (`#contact-strip`) — green section, 4 contact cards
4. Services Grid — 6 service cards linking to category pages
5. Fiat 500 scroll-driven video
6. FAQ accordion
7. Newsletter form
8. Footer

## Folder Reorganisation Status

### Phase 1 — DONE (2026-03-30)
- `Branding/` → `design/brand/` (gitignored, local only)
- `temporary screenshots/` → `design/screenshots/` (gitignored)
- `bokun codes/` → `design/bokun-codes/` (gitignored, duplicate xlsx deleted)
- `BOKUN-INTEGRATION.md`, `seo-audit.md`, `asset-prompts.md` → `docs/` (gitignored)
- Deleted: `logo-ultimato.svg`, `view-logo.mjs`, `www.rome-tourguide.com.*.md`
- `.gitignore` updated to exclude `design/` and `docs/`

### Phase 2 — DONE (2026-04-02)
Goal: consolidate all web-served images under `assets/images/` and rename `Tripadvisor/` to lowercase.

**Completed:**
- `Tripadvisor/*.png` → `assets/images/tripadvisor/`
- `hero.jpg`, `about.jpg` → `assets/images/`
- `favicon.png` → `assets/images/`
- `alpha-logo.png`, `alpha-logo.svg`, `logo-ufficiale-header.png` → `assets/images/logos/`
- All 29 HTML files updated with new paths
- JSON-LD logo URL updated in `index.html`

### Phase 3 — DONE (2026-04-02)
Goal: tidy root folder clutter and fix security issues.

**Completed:**
- Deleted: `tmp-img-0.png`, `tmp-img-1.png` (temp AI generation files)
- Moved: `reviews format missing qrcode.png` → `design/marketing/`
- Moved: `qrcode google/` → `design/marketing/`
- Moved: `client secret gabrieledadej/` credentials → `tools/` (gitignored)
- Moved: `widget-test.html` (Bokun dev page) → `design/`
- Moved: 28 ChatGPT PNGs from `assets/images/` → `design/ai-generated/`
- Updated `.gitignore`: added `sale reports/`, `qrcode google/`

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
- Output folder: `design/screenshots/` (git-ignored)
- Command: `node -e "const p = require('puppeteer'); ..."` using the path above

## Video Assets
- Scroll-driven video: `assets/videos/fiat500-scrub.mp4`
- Source (original): `design/brand/brand_assets/Videos/b18b6f51-2e30-42e9-98f0-abb17f5e2e95.mp4`
- Converted with FFmpeg: `-g 1` (keyframe every frame) for smooth scroll scrubbing
- FFmpeg binary: `C:/Users/pierf/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe/ffmpeg-8.1-full_build/bin/ffmpeg.exe`
- To re-convert any video for scroll scrubbing:
  ```
  ffmpeg -i INPUT.mp4 -vf "scale=1920:-2" -c:v libx264 -g 1 -crf 26 -preset slow -an -movflags faststart OUTPUT.mp4 -y
  ```
- **Video optimisation:** For better performance on Netlify free tier, keep the final video under ~5–10 MB. Use `-crf 26` (already set) and consider lowering resolution further if needed (e.g., `scale=1280:-2`). Test file size and playback smoothness.

## Performance & SEO

### Image compression rules
- All images added to `design/brand/brand_assets/Images/` MUST be compressed before use.
- DSC/camera photos are typically 4–28MB raw — **always compress with FFmpeg first**:
  ```
  ffmpeg -i INPUT.jpg -vf "scale=1400:-2" -q:v 4 OUTPUT.jpg -y
  ```
- Target: 100–300KB per image for web use. Use `scale=1400:-2` for card/hero images (wider = better quality on large screens).
- Never commit raw camera photos to the repo (e.g. `_DSC*.jpg`, `IMG_*.JPG`, `DSCF*.JPG`).
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

## AI Image Generation

### How to generate images (when user says "generate an image")
Use the Hugging Face Inference API directly via Node.js — no MCP tool call needed.

**Model:** `black-forest-labs/FLUX.1-schnell`
**Endpoint:** `https://router.huggingface.co/hf-inference/models/black-forest-labs/FLUX.1-schnell`
**Auth:** `Bearer YOUR_HF_TOKEN_HERE` (ask user for token)
**Output folder:** `design/ai-generated/` (gitignored, local only — never use screenshots/ or root)

### Script template
```js
node -e "
const https = require('https');
const fs = require('fs');
const prompt = \`YOUR PROMPT HERE\`;
const body = JSON.stringify({ inputs: prompt });
const options = {
  hostname: 'router.huggingface.co',
  path: '/hf-inference/models/black-forest-labs/FLUX.1-schnell',
  method: 'POST',
  headers: {
    'Authorization': 'Bearer YOUR_HF_TOKEN_HERE',
    'Content-Type': 'application/json',
    'Content-Length': Buffer.byteLength(body)
  }
};
const req = https.request(options, (res) => {
  const chunks = [];
  res.on('data', c => chunks.push(c));
  res.on('end', () => {
    const buf = Buffer.concat(chunks);
    if ((res.headers['content-type'] || '').includes('image')) {
      fs.writeFileSync('design/ai-generated/FILENAME.png', buf);
      console.log('Saved', buf.length, 'bytes');
    } else {
      console.log(res.statusCode, buf.toString().slice(0,400));
    }
  });
});
req.on('error', e => console.error(e.message));
req.write(body);
req.end();
"
```

### Prompt tips for Alpha Tours brand
- Always include: `cream background, flat vector illustration, deep forest green (#324e2c) and crimson red (#a71b20)`
- Roman elements that work well: Colosseum silhouette, Roman arch, laurel wreath, Vespa, Fiat 500
- Say `no text` — AI-generated text is always garbled
- Generate 2–3 variants per request so user can choose
- After generating, always read the image with the Read tool to show it inline

### Known working variants (saved in design/ai-generated/)
- `alpha-tours-logo-gen.png` — Colosseum flat line art, green on cream (V1, strongest)
- `alpha-logo-v2.png` — Circular badge / emblem with laurel wreath
- `alpha-logo-v3.png` — Green Vespa under Roman arch (most distinctive)

## Requirements
- Fully responsive (mobile, tablet, desktop)
- Hero with photo bg, left-aligned text, tour-type filter chips
- Services grid with per-tour gradient image-banner cards
- Scroll-driven Fiat 500 exploded-view video section (homepage)
- "Book Now" button linking to contact page
- Multi-page: Home, About, Services, Contact, Blog
- SEO: meta descriptions, title tags, structured data

---

## Paperclip AI Setup

> **Full reference:** `tools/paperclip-reference.md` — authoritative source for all Paperclip details, UUIDs, adapter config, AGENTS.md format, troubleshooting, and cheat sheet. Read that file before building or debugging any agent.

### What is Paperclip
Open-source AI agent orchestration platform — runs AI agents as autonomous "employees" on a schedule.
- Repo: https://github.com/paperclipai/paperclip | Docs: https://docs.paperclip.ing
- Stack: Node.js + React + embedded PostgreSQL | License: MIT

### How to Start
```bash
npx paperclipai run
# Dashboard: http://127.0.0.1:3100
```

### Instance
- **Data dir:** `C:/Users/pierf/.paperclip/instances/default/`
- **Company:** Alpha Tours Rome — ID: `dfc61b86-0984-49ec-8286-075554c17f5b` — prefix: `ALP`

### Live Agents (all use `claude_local` adapter, 60-min heartbeat, wake-on-demand)

| Agent | ID | Purpose |
|---|---|---|
| Content & SEO Writer | `18a98588-8db3-40c7-a39f-3264804019ea` | SEO blog posts & marketing copy |
| Image Generator | `63da2341-d00f-45bd-8af5-5f3c78bb3c9d` | Brand images via HuggingFace FLUX.1 |
| Review Response Agent | `6af56602-9755-431b-bc5d-b2c5234d9826` | Google review drafts → email to owner |
| Strategy & Proposals Agent | `d6b754cb-5f63-41f1-b04f-d481a4f29c43` | Expands business ideas into team-ready proposal docs |

### Completed Tasks
- **ALP-1** ✅ — "The Best Way to See Rome: A Private Golf Cart Tour" — published to `blog.html`
- **ALP-4** ✅ — First Alpha Tours ideas & proposals document generated → `proposals/`

### How to Trigger an Agent
1. `npx paperclipai run` → open http://127.0.0.1:3100
2. New Issue → write a specific title/brief → assign to agent → status: `todo`
3. Agent picks it up within the heartbeat interval (or immediately with wake-on-demand)

**Good issue title examples:**
- Content & SEO Writer: `"Write a 600-word SEO blog post targeting 'vespa sidecar tour Rome'. Alpha Tours brand voice. CTA to alphatoursrome.com"`
- Image Generator: `"Generate flat vector illustration: orange Fiat 500 at the Pantheon, golden hour. Save as fiat500-pantheon.png"`
- Review Response Agent: `"Check for new Google reviews and send draft replies"`
- Strategy & Proposals Agent: `"Generate updated Alpha Tours ideas & proposals document"` (re-run whenever ideas list changes)

### Review Response Agent — Key Details
- Fetches Google Places API → drafts replies → emails to `gabrieledadej@gmail.com`
- Credentials: `tools/review-config.json` (gitignored) — contains `placesApiKey`, `placeId`, `gmail.user`, `gmail.pass`
- Google Place ID: `ChIJHcAuWLqLJRMR-nD81t9OlAk`
- Scripts: `tools/check-reviews.mjs`, `tools/send-draft-email.mjs`
- State files: `tools/seen-reviews.json`, `tools/new-reviews.json`, `tools/pending-drafts.json` (all gitignored)
- **Bug fixed 2026-04-08:** Type mismatch in `seen-reviews.json` — IDs now always compared as strings. Also added `HEARTBEAT.md` so the agent runs automatically without needing a manual issue.

### Strategy & Proposals Agent — Key Details
- Input: reads ideas from `proposals/ideas.md` (or uses master list embedded in AGENTS.md)
- Output: writes `proposals/alpha-tours-ideas-YYYY-MM-DD.md` — one combined document per run
- Heartbeat: disabled (on-demand only) — create a new issue when the ideas list changes
- Re-trigger: create a new issue assigned to `strategy-proposals-agent` with title "Generate updated Alpha Tours ideas & proposals document"
- To update ideas: edit `proposals/ideas.md` or update the master list in the agent's AGENTS.md

### Planned Agents (not yet built)
- **Customer Support Agent** — reads Netlify Forms webhook, drafts replies, sends via email API
- **Sales Report Analyst** — reads `sale reports/report.xlsx`, surfaces booking insights per channel/tour
- **Social Media Agent** — generates weekly Instagram/Facebook posts for review queue

### Always-On Deployment
Paperclip only runs while your PC is on. For 24/7: Hetzner CX22 VPS (~€3.79/mo) + pm2. Full steps in `tools/paperclip-reference.md`.

### Strategy & Discussion
`tools/paperclip-strategy.md` — agent roadmap, cost estimates, open questions

---

## OTA Listing Optimization Project

### Status (2026-04-01)
- **Phase 1 — Audit: COMPLETE**
- **Phase 2 — CEO approval: IN PROGRESS** — messages drafted, awaiting CEO review
- **Phase 3 — Listing rewrites: PENDING** — full copy ready in CEO message appendices
- **Phase 4 — Implementation: PENDING** — requires Viator + GYG supplier dashboard access

### Listings Audited
| Platform | Product | URL | Reviews | Rating | Price |
|---|---|---|---|---|---|
| Viator | Discover Rome Highlights by Golf Cart Tour (private) | d511-195084P2 | 198 | 5.0 | €140/person |
| GYG | Rome's Highlights by golf cart (Polaroid Touch) | t1098177 | 7 | 5.0 | €53/person |

### Competitor Benchmarks
| Platform | Competitor listing | Reviews | Key differentiator |
|---|---|---|---|
| Viator | Rome: City Sightseeing Private Customized Golf Cart Tour (d511-7377P1) | 4,420 | Hotel pickup in title, night tour variant, named guides |
| GYG | Rome: Golf Cart Tour with Artisanal Gelato Tasting (t653524, City Walkers Tours) | 1,554 | Artisanal gelato included, €39/person, 9-stop itinerary, 3 languages |

### Key Findings per Platform

**Viator — top 3 issues:**
1. Title buries "private" at end — needs to lead with it + add "Hotel Pickup"
2. Colosseum admission listed as an inclusion when it's actually excluded — misleads guests
3. Description opens negatively ("stuffy bus tours") and undersells the experience

**GYG — top 3 issues:**
1. Meeting point has wrong postcode (00148 instead of 00185) — guests sent to wrong part of Rome
2. Only 7 reviews from 34 bookings — guides must use the Canva review card (QR code) after every tour
3. Polaroid photo keepsake is the unique differentiator but appears nowhere in title, copy, or inclusions

### The Polaroid Strategy
Alpha Tours offers a Polaroid photo keepsake — unique in Rome golf cart market. Currently only in the GYG URL slug, invisible to guests and algorithm. Must be:
- In the GYG title: `Rome: Golf Cart City Tour — Small Group with Polaroid Photo Keepsake`
- In highlights, inclusions, and description on GYG
- Gelato stop is a future option to add on top (not yet offered)

### Review Growth Strategy
- **GYG**: Guides hand the Canva review card (restaurant tips + QR code) to every guest at end of tour — already built, just not being used consistently
- **Viator**: Post-tour WhatsApp/message with direct review link
- **Review Response Agent** ✅ LIVE — runs every hour automatically; or create a Paperclip issue assigned to `review-response-agent` for an on-demand check. Emails draft reply to gabrieledadej@gmail.com.

### Files
```
tools/
  audit-viator-golf-cart.md     ← full Viator audit with issues + scoring
  audit-gyg-golf-cart.md        ← full GYG audit with competitor analysis
  ceo-message-viator.md         ← CEO message + full updated copy appendix (ready to paste)
  ceo-message-gyg.md            ← CEO message + full updated copy appendix (ready to paste)
  viator-gyg-optimization-plan.md ← original plan + phase tracker
sale reports/
  analysis.md                   ← Bokun 523-booking sales analysis
```

### When Resuming Implementation (Phase 3+)
- All updated copy (title, description, highlights, inclusions, itinerary) is in the appendix of each CEO message file — ready to paste directly into the supplier dashboards
- Do NOT rewrite from scratch — use the approved copy in those files
- Viator DataDome CAPTCHA blocks Puppeteer scraping — user must paste content manually if re-audit needed
- GYG can be scraped with Puppeteer (works reliably)

---

---
# Telegram Bot on Modal — Alpha Tours (update: May 2026)

## Status
- **Bot**: 24/7 live on Modal at `https://pierpoljak024--alpha-tours-rome-bot-fastapi-app.modal.run`
- **Health check**: ✅ running (returns `{"status":"ok"}`)
- **CEO ID**: `5285215270` — recognized as CEO with special powers
- **Provider**: OpenRouter (`google/gemini-2.0-flash-001`)

## How to deploy
```bash
modal deploy modal_deploy.py
```
Stop: `modal app stop alpha-tours-rome-bot`

## CEO Powers (only for Telegram ID 5285215270)
1. **"check reviews"** → runs `python tools/check_reviews.py` — fetches Google reviews via My Business API OAuth
2. **"post replies"** → runs `python tools/post_review_reply.py` — posts draft replies to Google via API
3. **"edit the site" / web editing** → reads/writes HTML files + git push to GitHub (auto-deploys to Netlify)

## Fixes applied (May 4, 2026)

### Problem 1: `post_review_reply.py` was a stub
- Old code: `print("TBD in v2")` — never posted anything
- Fix: replaced with real POST to `https://mybusiness.googleapis.com/v4/{reviewName}/reply`
- Both `tools/post_review_reply.py` (local) and the inline version in `_init_tools()` in `modal_deploy.py` fixed

### Problem 2: `check_reviews.py` crashed with empty cache.json (`{}`)
- Old code: read `an: null, ln: null` from `cache.json`, called `https://.../None/reviews` → crash
- Fix: validate `an and ln` before using cache — if either is None/empty, fall back to fresh API fetch
- Both local and inline version fixed

### Problem 3: `skills/review-manager.md` used `node` commands
- Old: `node tools/check-reviews.mjs` and `node tools/post-review-reply.mjs`
- Fix: changed to `python tools/check_reviews.py` and `python tools/post_review_reply.py`
- `.mjs` script exists locally but is NOT written on Modal — only `.py` scripts are created by `_init_tools()`

### Problem 4: Local SOUL.md had no CEO powers
- Old `../.hermes/SOUL.md` = only basic tourism concierge, no review/website commands for CEO
- Fix: updated with full CEO powers (check reviews, post replies, edit website) + tour listing

### Problem 5: Google API quota exhausted
- Symptom: `HTTP 429 Too Many Requests` after multiple tests
- Fix: `cache.json` stores account name + location name after first fetch
  - Before: 4 calls (token + accounts + locations + reviews)
  - After cache populated: 2 calls (token + reviews)
  - Backoff reduced from 6 retries to 4 (max wait 16s vs 124s)

## Key files
- `modal_deploy.py` — main deploy script (SOUL inline + `_init_tools()` + `_start_hermes()`)
- `tools/check_reviews.py` — fetches Google reviews (OAuth, no Place ID)
- `tools/post_review_reply.py` — posts replies to Google reviews
- `tools/post-review-reply.mjs` — Node.js alternative (works but not deployed on Modal)
- `tools/cache.json` — cached account/location names (auto-created)
- `tools/seen-reviews.json` — set of seen review IDs
- `tools/pending-drafts.json` — draft replies generated by Hermes, ready to post
- `../.hermes/SOUL.md` — local soul (synced with Modal version)

## Secrets (Modal secret: `alpha-tours-env`)
- `TELEGRAM_BOT_TOKEN`, `OPENROUTER_API_KEY`, `GITHUB_TOKEN`
- `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`, `GOOGLE_REFRESH_TOKEN`

## SOUL.md 2.0 — Piano di Riscrittura (approvato)

### Problemi SOUL.md attuale
1. **"EXECUTE this"** — Hermes non ha un comando `EXECUTE`, deve usare shell commands
2. **No browser toolset** — Hermes HA il tool (navigate, click, type, scroll) ma non gli diciamo di usarlo
3. **Path solo per Modal** (`/root/repo/...`) — non funziona in locale
4. **No visual loop check** — modifica "al buio" senza screenshot prima/dopo
5. **No rollback** — se sbaglia, nessun "annulla"
6. **No skill index** — skills esistono ma Hermes non sa che sono lì

### Nuova SOUL.md 2.0 deve includere:
- Fix: shell commands reali (non "EXECUTE")
- Fix: dual paths (locale + Modal)
- Nuovo: browser toolset per screenshot visivi
- Nuovo: visual loop (screenshot PRIMA → conferma → modifica → screenshot DOPO → approvazione → commit)
- Nuovo: rollback (`git revert HEAD --no-edit && git push`)
- Nuovo: skills index reference
- Nuovo: self-improvement section

### Skills da creare
1. `skills/index.md` — registry skills
2. `skills/web-editor.md` — modifica sito con preview visiva
3. `skills/design-system.md` — regole frontend (colori #324e2c, #a71b20, #fcefe6, #f5b35d; font Playfair+Inter)
4. `skills/self-improve.md` — auto-apprendimento

## Local Test Progress (May 5, 2026) — Summary
- **Config locale fixata**: `~/.hermes/config.yaml` aggiornato (formato `model:` section corretto)
- **API keys**: aggiunte a `~/.hermes/.env` (OPENROUTER_API_KEY, TELEGRAM_BOT_TOKEN, TELEGRAM_HOME_CHANNEL, GATEWAY_ALLOW_ALL_USERS)
- **`hermes doctor`**: ✅ tutto OK (config valida, OpenRouter funzionante, terminal tool disponibile)
- **T1 - Customer query test**: ✅ `hermes -z "Ciao! What tours do you offer?"` → risposta perfetta con brand voice
- **Google OAuth test**: ✅ token ottenuto ma **HTTP 429** (rate limit colpito) — test rimandato a stasera
- **Credenziali Google**: Su Modal secret (`alpha-tours-env`) e in `.env` locale (gitignored)
- **File creato**: `local_test_plan.md` — piano di test completo con checklist
- **File aggiornato**: `plan.md` — riscritto con stato attuale e test rimanenti

### Test ancora da fare (stasera)
1. `python tools/check_reviews.py` con le credenziali giuste
2. Gateway Telegram locale (`python start_telegram_gateway.py`)
3. CEO Power 1: "check reviews"
4. CEO Power 2: "post replies"
5. CEO Power 3: "change price golf cart"
6. Deploy su Modal (solo dopo tutti i test passati)

## Architecture insight (May 5, 2026)
Hermes v0.12.0 uses the **terminal toolset** for running shell commands — NOT an "EXECUTE" command.

### How the terminal tool works:
1. SOUL.md instructs the LLM what to do
2. The LLM **calls the terminal tool** with a command string
3. The gateway/Runner executes it via `subprocess.run()` with shell=True
4. stdout+stderr is returned as tool result to the LLM

### ❌ WRONG SOUL.md syntax (was breaking POWER 3):
```
EXECUTE this Python code to edit an HTML file:
```python
import subprocess, os
...
```
```
Hermes has no "EXECUTE" command — the LLM ignores this.

### ✅ CORRECT SOUL.md syntax (now fixed):
```
1. Show file: python -c "from pathlib import Path; f = Path('/path/file.html'); print(f.read_text()[:3000])"
2. Wait for CEO instructions
3. Edit: python -c "... replacement logic ..."
4. Commit: cd /repo && git add -A && git commit -m 'fix: ...' && git push
```
Use `python -c "..."` one-liners — never Python code blocks.

### Key files created/updated:
- `hermes-reference.md` — Full technical reference (15 sections, ~350 lines)
- `~/.hermes/SOUL.md` — POWER 3 fixed with shell commands
- `modal_deploy.py` — POWER 3 fixed in SOUL_CONTENT

## Next steps
- [ ] Deploy fixato `modal_deploy.py` su Modal
- [ ] Test "check reviews" on Telegram (wait for Google API quota reset if getting 429)
- [ ] Test "post replies" after drafts exist
- [ ] Test web editor ("cambia prezzo")

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
    await page.screenshot({ path: 'design/screenshots/screenshot.png' });
    await browser.close();
  })();
  "
  ```
- Output folder: `design/screenshots/` (git-ignored)
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
