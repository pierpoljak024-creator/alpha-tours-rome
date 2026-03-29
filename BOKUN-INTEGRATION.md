# Bokun Integration Plan — Alpha Tours Rome

**Status:** Awaiting widget embed codes from Bokun dashboard
**Goal:** Embed the existing Alpha Tours Bokun booking account into the new alphatoursrome.com website gracefully, replacing the current contact form with a real booking flow.

---

## Background

Alpha Tours has an existing Bokun seller account currently used on the old site (rome-tourguide.com / WordPress). The new site is a custom multi-page HTML/CSS/JS build hosted on Netlify. Bokun provides embeddable booking widgets (iframes + JS) that work on any website — no server-side code needed.

The Bokun Channel Manager API (bokun.dev/inventory-service-api) is **not** needed here. The right integration method is **Bokun Booking Widgets** generated from the Bokun seller dashboard.

---

## Phase 1 — Collect Widget Codes (USER task)

> Complete this phase before asking Claude to write any code.

### Step 1.1 — Log into Bokun dashboard
- Go to [bokun.io](https://bokun.io) and log in with the Alpha Tours account

### Step 1.2 — Navigate to Sales Channels / Widgets
- In the left menu go to: **Sales Channels → Marketplace** (or **Website Integration** / **Booking Widgets** depending on your plan)
- You should see a list of your active products/experiences

### Step 1.3 — Get embed code for each product
For each of the 6 services below, click **Get Embed Code** (or "Widget Code"):

| Service | Bokun Product Name (check dashboard) | Slug to use |
|---|---|---|
| Golf Cart Tours | _(confirm in dashboard)_ | `golf-cart` |
| Vespa Sidecar | _(confirm in dashboard)_ | `vespa` |
| FIAT 500 Vintage Tour | _(confirm in dashboard)_ | `fiat500` |
| Food Tours | _(confirm in dashboard)_ | `food-tour` |
| Airport & Hotel Transfers (Van) | _(confirm in dashboard)_ | `transfers` |
| Private Day Trips | _(confirm in dashboard)_ | `day-trips` |

Each embed code will look like one of these two formats:

**Format A — Script + div (preferred):**
```html
<script src="https://widgets.bokun.io/assets/javascripts/apps/booking-widget/iframe-loader.js?v=1" charset="utf-8"></script>
<div class="bokunWidget" data-src="https://widgets.bokun.io/online-sales/[CHANNEL-ID]/experience/[PRODUCT-ID]?skin=1"></div>
```

**Format B — Plain iframe:**
```html
<iframe src="https://widgets.bokun.io/online-sales/[CHANNEL-ID]/experience/[PRODUCT-ID]" width="100%" height="600" frameborder="0"></iframe>
```

### Step 1.4 — Note your Channel ID
- The Channel ID appears in every widget URL: `.../online-sales/[CHANNEL-ID]/experience/...`
- Note it down — it's the same for all products on the same sales channel

### Step 1.5 — Hand codes to Claude
Paste all 6 embed codes into the chat. Label each one clearly:
```
GOLF CART WIDGET:
<script ...></script>
<div class="bokunWidget" ...></div>

VESPA WIDGET:
...
```

---

## Phase 2 — Code Implementation (Claude task)

> Claude completes this once Phase 1 is done.

### Step 2.1 — Update `contact.html`

**Current state:** Hand-rolled HTML contact form with WhatsApp/phone links
**Target state:** Branded booking hub with:
- Service selector tabs at the top (one per tour type)
- Bokun widget loads below when a tab is selected (lazy: only the active tab's widget loads)
- Phone / WhatsApp / Instagram contact details remain visible in a sidebar or below
- Mobile-first layout, full-width widget on small screens

**Layout structure:**
```
[Page Hero — "Book Your Tour"]
[Contact info strip — phone, WhatsApp, Instagram]
[Service tabs: Golf Cart | Vespa | Fiat 500 | Food Tour | Transfers | Day Trips]
[Active Bokun widget — full width, scrollable on mobile]
[FAQ accordion — existing, keep below]
```

**Anchor IDs to add** (so "Book Now" buttons on other pages can deep-link):
- `#book` — top of booking section
- `#book-golf-cart`
- `#book-vespa`
- `#book-fiat500`
- `#book-food-tour`
- `#book-transfers`
- `#book-day-trips`

### Step 2.2 — Update `services.html`

- Each service card's "Book Now" button → `contact.html#book-[slug]`
- No widget embedded on services page (keep it clean, one booking hub)

### Step 2.3 — Update `index.html`

- Hero "Book Now" → `contact.html#book`
- Any other CTA buttons → `contact.html#book`

### Step 2.4 — Update `about.html` and `blog.html`

- Any "Book Now" / "Start Planning" CTAs → `contact.html#book`

### Step 2.5 — Style the widget wrapper

Add to `styles.css`:
```css
/* Bokun widget container — brand-styled wrapper */
.bokun-widget-wrap {
  background: var(--cream);
  border: 2px solid var(--green);
  border-radius: 1rem;
  overflow: hidden;
  min-height: 520px;
}

/* Tab selector for booking service choice */
.booking-tabs {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 1.5rem;
}

.booking-tab {
  padding: 0.6rem 1.2rem;
  border: 2px solid var(--green);
  border-radius: 2rem;
  background: transparent;
  color: var(--green);
  font-family: 'Inter', sans-serif;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.2s cubic-bezier(0.22,1,0.36,1),
              color 0.2s cubic-bezier(0.22,1,0.36,1);
}

.booking-tab.active,
.booking-tab:hover {
  background: var(--green);
  color: #fff;
}
```

### Step 2.6 — Lazy-load widgets in `script.js`

Only inject the Bokun `<script>` tag and activate the widget for whichever tab is currently selected — avoid loading all 6 widgets on page load:

```js
// Pseudo-code — Claude will implement fully
const tabs = document.querySelectorAll('.booking-tab');
const panels = document.querySelectorAll('.bokun-panel');

tabs.forEach(tab => {
  tab.addEventListener('click', () => {
    tabs.forEach(t => t.classList.remove('active'));
    panels.forEach(p => p.hidden = true);
    tab.classList.add('active');
    const target = document.getElementById(tab.dataset.target);
    target.hidden = false;
    // inject bokun widget script if not already loaded
    if (!target.dataset.loaded) {
      target.dataset.loaded = 'true';
      // append iframe / activate bokunWidget here
    }
  });
});
```

### Step 2.7 — Test checklist

- [ ] All 6 widgets load correctly in desktop Chrome
- [ ] Mobile (375px): widgets scroll correctly, no horizontal overflow
- [ ] Deep links work: `contact.html#book-golf-cart` opens Golf Cart tab
- [ ] "Book Now" buttons on all other pages point to correct anchors
- [ ] Bokun checkout flow completes to payment (test with a test date)
- [ ] Contact info (phone, WhatsApp) is still visible alongside widgets
- [ ] No `console.log` or debugging artifacts

### Step 2.8 — Deploy

```bash
git add contact.html services.html index.html about.html blog.html styles.css script.js
git commit -m "feat: integrate Bokun booking widgets into contact page"
git push origin main
```

Netlify auto-deploys within ~1 minute.

---

## Phase 3 — Optional Enhancements (future)

These are nice-to-haves, implement after Phase 2 is working:

- **Bokun reviews widget**: embed Bokun/Viator review scores on service cards
- **Live availability badge**: use Bokun REST API to show "Next available: [date]" on each card
- **Booking confirmation redirect**: after successful Bokun booking, redirect to a custom thank-you page (`thank-you.html`) with brand styling
- **Google Analytics / GTM**: track Bokun widget interactions as conversion events

---

## Key URLs & References

| Resource | URL |
|---|---|
| Bokun seller dashboard | https://bokun.io |
| Bokun widget docs | https://support.bokun.com (search "booking widget") |
| Bokun developer docs | https://bokun.dev |
| Live site | https://alphatoursrome.com |
| GitHub repo | https://github.com/pierpoljak024-creator/alpha-tours-rome |
| Old site (reference) | https://www.rome-tourguide.com |

---

## Current Status Log

| Date | Action | Notes |
|---|---|---|
| 2026-03-27 | Plan created | Awaiting widget embed codes from Bokun dashboard |
| | Widget codes received | _(fill in when done)_ |
| | Phase 2 implemented | _(fill in when done)_ |
| | Tested & deployed | _(fill in when done)_ |
