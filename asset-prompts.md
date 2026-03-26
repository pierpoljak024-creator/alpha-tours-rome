# Alpha Tours — Asset Prompts
> Generated via /asset-generation skill
> Company: Alpha Tours | Rome, Italy
> Brand colors: #324e2c · #a71b20 · #fcefe6 · #f5b35d
> Logo: alpha-logo.svg

---

## Image Prompt 1 — Fiat 500 with Couple in a Roman Piazza (Hero)

```
A gleaming pastel-cream vintage Fiat 500 parked in a sun-drenched Roman piazza at golden hour,
a laughing couple beside the open door — woman in a floral sundress, man in a linen shirt —
terracotta building facades glowing warm amber behind them, long shadows stretching across worn
cobblestones, deep olive-green (#324e2c) shutters and cascading bougainvillea framing the scene,
sun-gold (#f5b35d) light raking across the car's curved body, warm cream (#fcefe6) walls catching
the light, romantic travel lifestyle mood, low wide-angle shot with cinematic bokeh background,
rule-of-thirds composition, photorealistic, travel editorial photography style,
16:9 aspect ratio, 2560x1440px, ultra-sharp foreground, soft background depth,
[alpha-logo.svg composited bottom-left corner, semi-transparent white, subtle drop shadow]
```
> **Best for:** Midjourney v6 (`--ar 16:9 --style raw --q 2`), DALL·E 3 (`size: "1792x1024"`)
> **Usage:** Primary hero image for index.html — replace CSS gradient placeholder

---

## Image Prompt 2 — Golf Cart at the Colosseum, Golden Hour

```
An open-top golf cart carrying a smiling couple and a local guide gliding along the Via Sacra
with the Colosseum towering in the background at magic-hour sunset, sky blazing in shades of
burnt orange and deep crimson fading to warm cream (#fcefe6), ancient stone lit in amber and
terracotta, deep olive-green (#324e2c) cypress trees flanking the road, Roman red (#a71b20)
poppies scattered across the grass verge, sun-gold (#f5b35d) light flooding the scene from the
right, passengers pointing and laughing, wind-blown hair, local guide in a linen shirt smiling,
low-angle wide shot looking up toward the Colosseum, cinematic travel photography atmosphere,
sharp foreground golf cart, soft monumental background, photorealistic, 16:9, 2560x1440px,
[alpha-logo.svg bottom-left corner, semi-transparent, 10% white opacity]
```
> **Best for:** Midjourney v6, Adobe Firefly (strong architectural detail rendering)
> **Usage:** Services page hero / Golf Cart Tours section feature image

---

## Image Prompt 3 — Roman Food Scene: Wine, Pizza & Cobblestones

```
An intimate outdoor trattoria table on a sun-warmed Roman cobblestone alley, a wood-fired
margherita pizza in the foreground with a crisp charred crust, two glasses of deep ruby red
wine catching golden afternoon light, a relaxed laughing couple toasting in soft focus behind —
summer-dressed, at ease, surrounded by the glow of late afternoon Rome — terracotta walls
draped with ivy and small herb pots, sun-gold (#f5b35d) light streaming down the narrow alley,
deep olive-green (#324e2c) shutters overhead, cream linen napkins, espresso cups to the side,
wide cinematic shot with foreground food razor-sharp and background scene beautifully bokeh'd,
food and travel photography fusion, magazine editorial quality, photorealistic,
16:9 aspect ratio, 2560x1440px,
[alpha-logo.svg bottom-left corner, semi-transparent white]
```
> **Best for:** Midjourney v6 (best food textures), Stable Diffusion XL + food LoRA
> **Usage:** Food Tours section feature image / About page visual accent

---

## Video Transition Prompt — Hero Loop (3–5 sec)

```
START FRAME:
  Wide static shot of a sun-drenched Roman piazza — a pastel-cream vintage Fiat 500 parked
  center-left, a smiling couple standing beside it, the Colosseum or a classical fountain
  visible in soft focus in the distance. Late golden-hour light, deep olive-green shadows,
  warm cream and terracotta tones throughout. Scene is still; gentle heat-shimmer visible
  in the background. Alpha Tours logo faintly visible bottom-left.

TRANSITION:
  Smooth ground-level dolly-in: camera glides forward at 0.5x speed, slowly accelerating.
  As it closes the distance, the couple turns toward camera and laughs — man opens the Fiat
  door. Gentle rack-focus pulls from cobblestones to couple's faces, then widens to reveal
  the full piazza. Speed ramps from 0.5x → 1x over last 1.5 seconds. Warm golden particles
  (dust motes in sunlight) drift across frame.

END FRAME:
  Fiat 500 fills 55% of frame, couple seated inside, arm out the window waving.
  Alpha Tours logo (alpha-logo.svg) fades in bottom-left over 0.4s — semi-transparent
  on a thin dark-green (#324e2c) bar. Tagline "Discover Your Way!" appears center-bottom
  in cream (#fcefe6), Playfair Display font, gentle fade-in over 0.6s. Scene holds 0.8s
  then cross-dissolves back to START FRAME for a seamless loop.

DURATION: 4–5 seconds
LOOP: Yes — end frame cross-dissolves to start frame (no hard cut)
COLOR GRADE: Warm golden LUT, lifted blacks, slight film grain overlay (5–8%)
ASPECT RATIO: 16:9 master at 2560×1440px; export 1920×1080 for web hero
AUDIO (optional): Soft fingerpicked classical guitar or light accordion, no percussion
```
> **Best for:** Runway ML Gen-3 Alpha (keyframe mode), Pika 1.5, Kling 1.6
> **Workflow:** Generate Prompts 1 & 3 as static keyframes first → use as start/end in Runway

---

## How to Use These Prompts

| Step | Action |
|---|---|
| 1. Generate statics | Run Prompts 1–3 in Midjourney or DALL·E 3 |
| 2. Pick your hero | Strongest image becomes `hero.jpg` in the project root |
| 3. Activate hero | In `index.html`, uncomment `<img class="hero-bg-img">` and set `src="hero.jpg"` |
| 4. Keyframe video | Use Prompt 1 (start) + Prompt 3 (end) as keyframes in Runway or Pika |
| 5. Add logo overlay | Composite `alpha-logo.svg` in Figma/Canva/After Effects (AI cannot reliably embed SVGs) |
| 6. Color grade | Apply warm golden LUT in DaVinci Resolve (free) or CapCut for the video |
| 7. Add video hero | Save as `hero.mp4`, replace `<img>` with `<video>` tag in `index.html` |

> **Midjourney tip:** Append `--ar 16:9 --style raw --q 2` to every prompt.
> **DALL·E 3 tip:** Use `size: "1792x1024"` in the API — closest to 2K 16:9.
