# design-system — Alpha Tours Frontend Design System

## Brand Identity
- **Company:** Alpha Tours Rome
- **Website:** https://alphatoursrome.com
- **Taglines:** "Discover Rome Your Way!", "Local Guides · Authentic Tours · Memorable Moments", "Live the Dolce Vita!"

## Color Palette
| Role | Hex | Usage |
|------|-----|-------|
| Primary Green | `#324e2c` | Headers, footer, buttons, primary accents |
| Primary Red | `#a71b20` | "Book Now" buttons, badges, accent elements |
| Cream Background | `#fcefe6` | Page backgrounds, sections |
| Accent Orange | `#f5b35d` | Highlights, hover states, secondary accents |

### CSS Custom Properties (in styles.css)
```css
--color-primary: #324e2c;
--color-primary-dark: #1e3019;
--color-accent: #f5b35d;
--color-accent-hover: #e8a040;
--color-red: #a71b20;
--color-cream: #fcefe6;
--color-cream-light: #fef7f2;
--color-text: #1a1a1a;
--color-text-light: #555;
--color-white: #ffffff;
--color-bg: #fcefe6;
--font-heading: 'Playfair Display', serif;
--font-body: 'Inter', sans-serif;
```

## Typography
- **Headings:** `'Playfair Display', serif` — weights 600, 700
- **Body:** `'Inter', sans-serif` — weights 400, 500, 600, 700
- **Large headings:** Tight tracking `-0.03em`
- **Body text:** Generous line-height `1.7`
- **Fonts loaded via Google Fonts:** `https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Inter:wght@400;500;600;700&display=swap`

## Shadow System
```css
/* Base shadow */
box-shadow: 0 1px 3px rgba(0,0,0,0.08);

/* Elevated card */
box-shadow: 0 4px 20px rgba(0,0,0,0.08), 0 1px 3px rgba(0,0,0,0.05);

/* Floating element (modals, dropdowns) */
box-shadow: 0 12px 40px rgba(0,0,0,0.12), 0 4px 12px rgba(0,0,0,0.08);
```

Never use flat `shadow-md` or `shadow-lg` — always use layered color-tinted shadows.

## Animation Easing
```css
/* Spring-like easing — use for ALL animations */
transition: transform 0.3s cubic-bezier(0.22, 1, 0.36, 1), opacity 0.3s ease;

/* Only animate transform and opacity — NEVER transition-all */
/* Exceptions: background-color on buttons, color on links */
```

## Spacing Tokens
Use consistent spacing — no random values:
- `0.25rem` (4px) — micro
- `0.5rem` (8px) — tight
- `1rem` (16px) — base
- `1.5rem` (24px) — medium
- `2rem` (32px) — large
- `3rem` (48px) — section
- `4rem+` (64px+) — hero/sections

## Gradients
```css
/* Hero gradient (green to dark green) */
background: linear-gradient(135deg, var(--color-primary) 0%, #1e3019 100%);

/* Card overlays */
background: linear-gradient(to top, rgba(0,0,0,0.7) 0%, rgba(0,0,0,0.1) 60%, rgba(0,0,0,0) 100%);
```

## Interactive States
Every clickable element needs:
- `:hover` — slight lift/color change
- `:focus-visible` — visible outline ring
- `:active` — press effect (scale down or darker bg)

## Header Structure
- **3 rows:** TripAdvisor strip → Social strip → Navigation
- **Desktop:** `position: relative` (scrolls with page)
- **Mobile:** `position: fixed; top: 0`, hides on scroll down, reveals on scroll up
- **Height:** `--header-height: 175px` (desktop), `145px` (mobile ≤768px)

## Layout
- **Container:** max-width 1200px, centered with auto margins
- **Grid:** CSS Grid for service cards, footer, gallery
- **Responsive breakpoints:** 480px (mobile), 768px (tablet), 1024px (desktop)
- **Mobile-first** approach

## Component Reference
| Component | File | Notes |
|-----------|------|-------|
| Hero | `index.html` | Full-width photo bg, gradient overlay, left-aligned text |
| Service card | `index.html` | Gradient image-banner card with overlay text |
| Header | All files | 3-row white header |
| Footer | All files | 4-column grid + copyright |

## Images
- **Favicon:** `assets/images/favicon.png` (8.7KB, 64x64px)
- **Logo (header):** `assets/images/logos/logo-ufficiale-header.png` (52KB, 300x200px)
- **Logo (footer):** `assets/images/logos/alpha-logo.png` (69KB, 200x200px) OR `alpha-logo.svg` (1.2MB — use PNG for perf)
- **Hero:** `assets/images/hero.jpg`
- **Card images:** `design/brand/brand_assets/Images/Untitled (740 x 416 px) (2)/` (local only)
- **Always compress:** Use FFmpeg `scale=1400:-2 -q:v 4` for web images
- **WhatsApp float:** Green pill (`#25d366`), bottom-right, collapses to icon on mobile
