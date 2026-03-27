# Alpha Tours — Brand Guide

**Version:** 1.0 · March 2026
**Website:** alphatoursrome.com | www.rome-tourguide.com

---

## 1. Brand Foundations

### Who We Are
Alpha Tours is Rome's premier boutique tour company — 20+ years of experience, fully licensed local guides, and an obsession with making every experience private, personal, and unforgettable.

### Mission
To share the real Rome — its hidden streets, living history, authentic flavours, and secret stories — with travellers who want more than a group bus tour.

### Brand Personality
- **Warm** — passionate Romans who love their city
- **Expert** — 20+ years deep knowledge, all officially licensed
- **Exclusive** — every tour is private, never shared with strangers
- **Authentic** — real local experiences, not tourist traps
- **Confident** — we know Rome better than anyone

---

## 2. Taglines & Slogans

| Use | Tagline |
|-----|---------|
| Primary | **"Discover Rome Your Way!"** |
| Hero / hero-level | **"Your Local Experts for Unforgettable Experiences"** |
| Secondary | **"Live the Dolce Vita!"** |
| Lead-in | **"Let us take the lead"** |
| Food tours | **"Eat Like a Roman!"** |
| Footer trio | **"Local Guides · Authentic Tours · Memorable Moments"** |

---

## 3. Color Palette

### Primary Colors

| Name | Hex | Usage |
|------|-----|-------|
| **Forest Green** | `#324e2c` | Primary brand color · Nav · Feature sections · Buttons |
| **Deep Red** | `#a71b20` | Accent · CTA banners · Highlights · Tags |
| **Cream** | `#fcefe6` | Section backgrounds · About · Blog |
| **Amber Gold** | `#f5b35d` | CTAs · Hover states · Stats · Highlights |

### Extended Palette

| Name | Hex | Usage |
|------|-----|-------|
| Dark Green | `#1e3518` | Darker variant of primary (contact section bg) |
| Light Green | `#3d6035` | Lighter variant for gradients |
| Dark Red | `#8a1519` | Hover state for accent buttons |
| Dark Gold | `#e0a04e` | Hover state for primary buttons |
| Near-black | `#111111` | Footer background |
| Body text | `#1a1a1a` | Main body copy |
| Muted text | `#6b6b6b` | Secondary body copy, captions |
| White | `#ffffff` | Card backgrounds, text on dark |
| Surface | `#f9f9f9` | Subtle card/FAQ backgrounds |

### Do Not Use
- Default Bootstrap blue (`#0d6efd`) or any blue tone as primary
- Pure black (`#000`) — use `#111111` or `#1a1a1a` instead
- Any grey as a primary action color

---

## 4. Typography

### Typefaces

| Role | Font | Weights | Source |
|------|------|---------|--------|
| **Headings** | Playfair Display | 600, 700 | Google Fonts |
| **Body / UI** | Inter | 400, 500, 600, 700 | Google Fonts |

```html
<!-- Always load in this order -->
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
```

### Type Scale

| Element | Size | Weight | Tracking |
|---------|------|--------|---------|
| Hero H1 | `clamp(3rem, 7.5vw, 5.8rem)` | 700 (Playfair) | `-0.03em` |
| Section H2 | `clamp(2rem, 4.5vw, 3rem)` | 600 (Playfair) | `-0.025em` |
| Card H3 | `1.18rem` | 600 (Playfair) | normal |
| Section label | `0.68rem` | 700 (Inter) | `0.22em` UPPERCASE |
| Body | `1rem` | 400 (Inter) | normal |
| Small / meta | `0.875rem` | 400–500 (Inter) | normal |
| Tag | `0.65rem` | 700 (Inter) | `0.10em` UPPERCASE |

### Typography Rules
- Section labels: ALL CAPS, 0.22em letter-spacing, pill-shaped background, accent red color
- Large headings: tight tracking (`-0.025em`), line-height `1.10–1.15`
- Body copy: generous line-height `1.72–1.85`
- Never use Italic for body copy; use it selectively for the `<em>` highlight in H1 (`color: #f5b35d`)

---

## 5. Logo Usage

### Files

| File | Location | Use |
|------|----------|-----|
| `alpha-logo.svg` | Project root | **Production logo** — used in all HTML nav & footer (white contour, works on dark backgrounds) |
| `LOGO ALPHA.svg` | `Branding/brand_assets/logos/` | Full branded logo with text, for print/marketing |
| `4.svg` | `Branding/brand_assets/logos/variants/` | **Official canonical logo** — master source |

### Rules
- Always use `alpha-logo.svg` in HTML on dark backgrounds (nav, footer)
- Minimum clear space: equal to the height of the "A" in "ALPHA" on all sides
- Never stretch, recolor, add drop shadows, or place on busy backgrounds without a contrast overlay
- Never substitute a different logo or create new logo variations without updating this guide

---

## 6. Buttons

All buttons use `border-radius: 9999px` (pill shape). No exceptions.

### Button Types

| Class | Background | Text | Border | Use |
|-------|-----------|------|--------|-----|
| `.btn-primary` | `#f5b35d` | `#324e2c` | transparent | Primary CTA (Book Now, Book Tour) |
| `.btn-secondary` | `#a71b20` | white | transparent | Secondary CTA, pricing actions |
| `.btn-outline` | transparent | white | `rgba(255,255,255,0.45)` | On dark/photo backgrounds |
| `.btn-outline-dark` | transparent | `#324e2c` | `#324e2c` | On light/white backgrounds |
| `.btn-sm` | — | — | — | Small modifier, `0.48rem 1.1rem` padding |

### Hover States
- Lift: `transform: translateY(-2px)`
- Shadow: colored shadow matching button (`rgba(245,179,93,0.40)` for primary)
- All hover transitions: `0.3s cubic-bezier(0.4,0,0.2,1)`

---

## 7. UI Components

### Section Labels
```html
<span class="section-label">What We Offer</span>
```
- ALL CAPS, 0.68rem, letter-spacing 0.22em
- Pill shape, red tint background (`rgba(167,27,32,0.09)`)
- Use `.section-label.light` on dark/colored backgrounds (gold tint)

### Service Cards
- White background, `border-radius: 20px`
- Colored image banner at top (160px, gradient per tour type)
- Content in `.service-card-body` with `1.6rem` padding
- Hover: lift `translateY(-8px)` + layered shadow

### Tour Category Chips
```html
<a href="services.html" class="hero-chip">
  <span class="hero-chip-icon">🛺</span> Golf Cart
</a>
```
- Used in hero section as tour-type filter links
- Semi-transparent, pill shape
- Hover: amber gold tint

### FAQ Accordion
- Single column, max-width 780px centered
- `<details>/<summary>` for native browser expand/collapse
- `+` indicator rotates to `×` on open

---

## 8. Photography & Imagery

### Current Site Photos
| File | Use |
|------|-----|
| `hero.jpg` | Homepage hero background (Rome tourism scene) |
| `about.jpg` | About section / food services banner |

### Photography Style
- **Golden hour** Rome: warm amber light, cobblestone streets
- **People-focused**: happy guests in carts, Vespas, Fiats — authentic moments
- **Architectural**: Colosseum, Pantheon, Trevi — iconic but shot from fresh angles
- Always apply gradient overlay on hero images: `rgba(15,28,12,0.90) → rgba(167,27,32,0.25)`
- Avoid stock-photo-looking generic tourism imagery

### When Photos Are Missing
- Use gradient placeholder matching the brand palette
- Reference: `Branding/brand_assets/brochures/` for approved marketing imagery

---

## 9. Spacing System

All spacing uses CSS custom properties via `rem`:

| Token | Value | Use |
|-------|-------|-----|
| Section padding | `5.5rem 1.5rem` | Standard sections (`.section-pad`) |
| Section padding sm | `3.5rem 1.5rem` | Tighter sections (`.section-pad-sm`) |
| Card padding | `1.6rem 1.75rem` | Card body (`.service-card-body`) |
| Grid gap | `1.75rem` | Card grids |
| Max width | `1200px` | Container max-width |

---

## 10. Shadows

| Token | Value | Use |
|-------|-------|-----|
| `--shadow` | `0 2px 16px rgba(0,0,0,0.06)` | Subtle card elevation |
| `--shadow-md` | `0 8px 32px rgba(0,0,0,0.10)` | Hover states, tour cards |
| `--shadow-lg` | `0 20px 60px rgba(0,0,0,0.14)` | Service cards on hover |
| `--shadow-green` | `0 8px 28px rgba(50,78,44,0.20)` | Green button hover |
| `--shadow-orange` | `0 8px 28px rgba(245,179,93,0.40)` | Primary button hover, badges |

Never use a flat `box-shadow: 0 2px 4px #000` — always use the layered, low-opacity tokens above.

---

## 11. Animation & Motion

| Rule | Value |
|------|-------|
| Standard transition | `0.3s cubic-bezier(0.4, 0, 0.2, 1)` |
| Spring/slide | `0.55s cubic-bezier(0.22, 1, 0.36, 1)` |
| Scroll reveal | Fade-up: `opacity 0 → 1`, `translateY(28px → 0)` |
| Feature slide | Slide-left: `translateX(-80px → 0)`, `opacity 0 → 1` |
| Card hover lift | `translateY(-8px)`, `0.55s spring` |

**Rules:**
- Only animate `transform` and `opacity` — never `width`, `height`, or `top/left`
- Never use `transition: all`
- Stagger card reveals with `data-delay` (85ms per card)

---

## 12. Voice & Tone

### Do
- Warm, knowledgeable, enthusiastic about Rome
- First-person plural: "we know every story, every shortcut"
- Specific: "Testaccio market", "Trastevere backstreets", "Appian Way"
- Emphasise exclusivity: "private", "just your group", "no strangers"
- Use Italian flavour sparingly: "Dolce Vita", "trattoria", "piazza"

### Don't
- Generic tourism clichés: "unforgettable journey" without specifics
- Hard sell language: "best price guaranteed", "limited time offer"
- Passive voice: "tours are provided by" → "we lead"
- Overpromise: always match content to actual services offered

### Key Phrases (from brochures)
- "Your Local Experts for Unforgettable Experiences"
- "Discover Rome Your Way"
- "Live the Dolce Vita"
- "Let us take the lead"
- "Eat Like a Roman" (food tours only)
- "Local Guides · Authentic Tours · Memorable Moments"
- "No groups. No rush. No compromises."

---

## 13. Contact & Social

| Channel | Handle / URL |
|---------|-------------|
| Phone / WhatsApp | +39 375 829 7864 |
| Instagram | @alphatoursrome |
| Facebook | Rome-Tour-guide-104817567778940 |
| Website | alphatoursrome.com |
| Alt website | www.rome-tourguide.com |

---

## 14. Section Color Map (Homepage)

| Section | Background |
|---------|-----------|
| Navigation | Transparent → Dark green `rgba(26,46,22,0.96)` on scroll |
| Hero | Photo + dark gradient overlay |
| Services grid | White `#ffffff` |
| Feature / CTA | Forest green `#324e2c` |
| About | Cream `#fcefe6` |
| FAQ | White `#ffffff` |
| Blog preview | Cream `#fcefe6` |
| Newsletter | Forest green `#324e2c` |
| Contact strip | Dark green `#1e3518` |
| Footer | Near-black `#111111` |
