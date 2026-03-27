# Alpha Tours Website Project

## Brand Identity
- Company: Alpha Tours – Rome tour company
- Tagline: "Your Local Experts for Unforgettable Experiences!"
- New tagline from brochure: "Discover Your Way!" / "Live the Dolce Vita!"

## Color Palette
- Primary Green: #324e2c
- Primary Red: #a71b20
- Cream Background: #fcefe6
- Accent Orange: #f5b35d

## Logo
- File: alpha-logo.svg (white-contour version for use on dark backgrounds)
- Always use `alpha-logo.svg` from the project root — never invent or substitute logos

## Brand Assets
- All logos and source SVGs live in `Branding/` and `Branding/logo bg/`
- Photos: `hero.jpg` (tours banner), `about.jpg` (services/food banner) — both in project root
- Always check the project root and `Branding/` before using placeholders

## Services (from brochure)
- Golf Cart Tours
- Vespa Sidecar
- FIAT 500 Vintage Tour
- Food Tours (Wine, Pizza, Gelato, Hidden Trattorias)
- Private Day Trips
- Airport & Hotel Transfers

## Content from existing site
- About: Over 20 years of experience, licensed guides
- Contact: +39 375 829 7864, @alphatoursrome, alphatoursrome.com
- FAQ: golf cart capacity (7), cancellation policy, etc.

## Site Structure (multi-page, already built)
- `index.html` — Home
- `about.html` — About
- `services.html` — Services & pricing
- `contact.html` — Booking form
- `blog.html` — Travel tips & stories
- `styles.css` — All brand CSS (custom properties, grid, animations)
- `script.js` — Nav toggle, IntersectionObserver, FAQ accordion, smooth scroll

## Requirements
- Fully responsive (mobile, tablet, desktop)
- Hero section with a beautiful image of a vintage car or golf cart in Rome
- Services grid with icons
- "Book Now" button linking to contact page
- Scroll-triggered animation (e.g., a car sliding in)
- Multi-page: Home, About, Services, Contact
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
- Puppeteer is installed at `C:/Users/nateh/AppData/Local/Temp/puppeteer-test/`. Chrome cache is at `C:/Users/nateh/.cache/puppeteer/`.
- **Always screenshot from localhost:** `node screenshot.mjs http://localhost:3000`
- Screenshots are saved automatically to `./temporary screenshots/screenshot-N.png` (auto-incremented, never overwritten).
- Optional label suffix: `node screenshot.mjs http://localhost:3000 label` → saves as `screenshot-N-label.png`
- `screenshot.mjs` lives in the project root. Use it as-is.
- After screenshotting, read the PNG from `temporary screenshots/` with the Read tool.
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
