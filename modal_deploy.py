"""Deploy Alpha Tours Rome Telegram bot to Modal cloud (24/7).

Runs Hermes gateway on Modal with:
- CEO Mode: recognizes owner (Telegram ID 5285215270)
- Android-friendly review checker (Python code, no skills needed)
- Google Business Profile API auto-reply posting
- Web-editing via git commands

Usage:
    modal secret create alpha-tours-env ^
        TELEGRAM_BOT_TOKEN=... ^
        OPENROUTER_API_KEY=... ^
        GITHUB_TOKEN=ghp_... ^
        GOOGLE_CLIENT_ID=... ^
        GOOGLE_CLIENT_SECRET=... ^
        GOOGLE_REFRESH_TOKEN=...

    modal deploy modal_deploy.py

To stop:
    modal app stop alpha-tours-rome-bot
"""

import os
import sys
import subprocess
import threading
import json
from pathlib import Path

from fastapi import FastAPI, Response
import modal

APP_NAME = "alpha-tours-rome-bot"
CEO_TELEGRAM_ID = "5285215270"
REPO_URL = "https://github.com/pierpoljak024-creator/alpha-tours-rome.git"
REPO_DIR = Path("/root/repo/alpha-tours-rome")

# ═══════════════════════════════════════════════════════════════════════
# SOUL CONTENT — rewritten so Hermes can actually execute code
# ═══════════════════════════════════════════════════════════════════════

SOUL_CONTENT = r"""You are Alpha Tours Rome's AI concierge.

## CEO IDENTITY
- Telegram ID 5285215270 = CEO (you have special powers for them)
- Everyone else = normal customer (just answer tour questions)

## FOR NORMAL CUSTOMERS
Be a warm, passionate local guide. Recommend tours, give booking links. Use emojis 🍝🛵🛺🇮🇹🍋.
Brand: "Local Guides · Authentic Tours · Memorable Moments"

All tours listed below with their links. If they ask for a recommendation, ask:
1. How many people?
2. Interests (history, food, photos)?
3. How much time?
4. Private or group?

## FOR THE CEO (Telegram ID 5285215270)
You have TWO special powers. When they ask:

### POWER 1: Check Reviews ("check reviews" or "review status")
EXECUTE this in the shell (NOT Python — run as a command):

```
cd /root/repo/alpha-tours-rome && python tools/check_reviews.py
```

Then READ the output printed by that script. If there are new reviews:
- Generate a brand-voice reply for each (warm, grateful, 2-3 sentences, sign "- Alpha Tours Rome Team")
- Write the drafts to /root/repo/alpha-tours-rome/tools/pending-drafts.json in this format:
  ```json
  [{"reviewId": "...", "name": "...", "rating": 5, "draftReply": "..."}]
  ```
- Tell the CEO the results with names and ratings

### POWER 2: Post Review Replies ("post replies" or "send replies")
EXECUTE this in the shell:

```
cd /root/repo/alpha-tours-rome && python tools/post_review_reply.py
```

Then READ the output and tell the CEO what was posted.

### POWER 3: Edit Website ("change price", "update text", "edit the site")
EXECUTE this Python code to edit an HTML file:

```python
import subprocess, os
from pathlib import Path
repo = Path("/root/repo/alpha-tours-rome")

# READ first - show the file
filepath = repo / "tours/FILENAME.html"  # <-- CHANGE THIS to the actual file
print(filepath.read_text()[:3000])

# Then the CEO will tell you what to change
# WRITE the changed content and commit:
# filepath.write_text("... new HTML ...")
# subprocess.run(["git","-C",str(repo),"add","-A"], capture_output=True)
# subprocess.run(["git","-C",str(repo),"commit","-m","fix: updated content"], capture_output=True)
# token = os.environ.get("GITHUB_TOKEN","")
# auth_url = "https://"+token+"@github.com/pierpoljak024-creator/alpha-tours-rome.git"
# subprocess.run(["git","-C",str(repo),"push",auth_url], capture_output=True)
# print("✅ Pushed! Netlify will deploy automatically.")
```

---

## CONCIERGE TOUR DATA

### GOLF CART TOURS 🛺
Up to 7 guests. Meeting: Circo Massimo.

1. **Rome Highlights Private Tour** (Most Popular ⭐) — 2h30m, Private → https://alphatoursrome.com/tours/golf-cart-rome-highlights-private.html
2. **Top Ten Rome Major Attractions** — 2h30m → https://alphatoursrome.com/tours/golf-cart-top-ten.html
3. **Ancient Catacomb & Appian Way Tour** — 2h30m, Private → https://alphatoursrome.com/tours/golf-cart-catacomb-appian-way.html
4. **Discover Rome Highlights (Private)** — Flexible, Private → https://alphatoursrome.com/tours/golf-cart-private-highlights.html
5. **Discover Rome Highlights Tour — Private** — 2h30m, Private → https://alphatoursrome.com/tours/golf-cart-highlights-private-2.html
6. **Enjoy Rome Major Attractions** (Great Value 🏷️) — 2h30m → https://alphatoursrome.com/tours/golf-cart-major-attractions.html
7. **Rome's Highlights by Golf Cart** — 2h30m → https://alphatoursrome.com/tours/golf-cart-romes-highlights.html

### VESPA SIDECAR TOURS 🛵
Max 2 guests. Meeting: Circo Massimo.

1. **Vespa Sidecar — Express Highlights** (Fan Favourite ❤️) — 2h → https://alphatoursrome.com/tours/vespa-express-highlights-1.html
2. **Vespa Sidecar: Express Highlights** — 2h → https://alphatoursrome.com/tours/vespa-express-highlights-2.html

### FIAT 500 VINTAGE TOURS 🚗
Max 2-3 passengers. Meeting: Circo Massimo.

1. **FIAT 500 — Rome Highlights** (Most Booked 📚) — 2h → https://alphatoursrome.com/tours/fiat500-rome-highlights.html
2. **FIAT 500 Dolce Vita Experience** (New ✨) — 4h, includes Limoncello, Gianicolo views, Villa Pamphili picnic → https://alphatoursrome.com/tours/fiat500-4h-experience.html

### FOOD TOURS 🍕
1. **Eat & Walk: Street Food Center & Trastevere** — 3h, Private → https://alphatoursrome.com/tours/food-street-center-trastevere.html
2. **Guided Walking Food Tour Testaccio** (Most Popular ⭐) — 3h, Private → https://alphatoursrome.com/tours/food-testaccio.html
3. **Walking Food Tour with Tastings** — 3.5h, Small group → https://alphatoursrome.com/tours/food-walking-tastings.html

### PRIVATE DAY TRIPS
- Gladiators Colosseum → https://alphatoursrome.com/tours/day-trips-gladiators-colosseum.html
- Roman Forum Private → https://alphatoursrome.com/tours/day-trips-roman-forum.html
- VIP Private Tour Full Day → https://alphatoursrome.com/tours/day-trips-vip-tour.html

### AIRPORT TRANSFERS 🚐
VIP Airport/Port Van → https://alphatoursrome.com/tours/transfers-vip-van.html

## FAQ
- Booking: website or WhatsApp +39 375 829 7864
- Meeting: Circo Massimo (details after booking)
- Cancellation: flexible — WhatsApp
- Best for first-timers: Rome Highlights Private Golf Cart Tour
"""

# ═══════════════════════════════════════════════════════════════════════
# CONFIG
# ═══════════════════════════════════════════════════════════════════════

CONFIG_CONTENT = """provider: openrouter
model: google/gemini-2.0-flash-001
terminal:
  backend: local
"""

print("SOUL.md: %d chars" % len(SOUL_CONTENT))
print("config.yaml: %d chars" % len(CONFIG_CONTENT))

# ---- Modal app & image --------------------------------------------
app = modal.App(APP_NAME)

image = (
    modal.Image.from_registry("python:3.12", setup_dockerfile_commands=[
        "RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y git locales",
        "RUN sed -i '/en_US.UTF-8/s/^# //g' /etc/locale.gen && locale-gen en_US.UTF-8",
        "ENV LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8",
    ])
    .run_commands(
        "pip install --quiet "
        "git+https://github.com/NousResearch/hermes-agent.git "
        "fastapi uvicorn python-telegram-bot 2>&1 | tail -3"
    )
)


def _clone_repo():
    """Clone the website repo (used at startup)."""
    repo_parent = Path("/root/repo")
    repo_parent.mkdir(parents=True, exist_ok=True)
    if not (REPO_DIR / ".git").exists():
        token = os.environ.get("GITHUB_TOKEN", "")
        auth_url = REPO_URL.replace("https://", f"https://{token}@")
        subprocess.run(
            ["git", "clone", auth_url, str(REPO_DIR)],
            capture_output=True, check=True,
        )
        print("[GIT] Repo cloned.")
    else:
        subprocess.run(
            ["git", "-C", str(REPO_DIR), "pull"],
            capture_output=True,
        )
        print("[GIT] Repo pulled.")


def _init_seen_file():
    """Initialize seen-reviews.json if it doesn't exist."""
    seen_file = REPO_DIR / "tools" / "seen-reviews.json"
    seen_file.parent.mkdir(parents=True, exist_ok=True)
    if not seen_file.exists():
        seen_file.write_text("[]")
        print("[SEEN] seen-reviews.json initialized.")


def _start_hermes():
    """Write SOUL.md + config.yaml + .env, then launch Hermes gateway."""
    try:
        hermes_dir = Path("/root/.hermes")
        hermes_dir.mkdir(parents=True, exist_ok=True)
        (hermes_dir / "SOUL.md").write_text(SOUL_CONTENT, encoding="utf-8")
        (hermes_dir / "config.yaml").write_text(CONFIG_CONTENT, encoding="utf-8")
        (hermes_dir / ".env").write_text("TELEGRAM_HOME_CHANNEL=5285215270\n", encoding="utf-8")

        os.environ["TELEGRAM_HOME_CHANNEL"] = "5285215270"
        os.environ.setdefault("GATEWAY_ALLOW_ALL_USERS", "true")
        os.environ.setdefault("HERMES_ACCEPT_HOOKS", "1")
        os.environ.setdefault("HERMES_HOME", "/root/.hermes")

        # Clone repo
        try:
            _clone_repo()
            _init_seen_file()
        except Exception as e:
            print(f"[GIT WARN] Clone failed (non-fatal): {e}")

        # Log status
        for key in ["TELEGRAM_BOT_TOKEN", "OPENROUTER_API_KEY", "GITHUB_TOKEN",
                     "GOOGLE_CLIENT_ID", "GOOGLE_CLIENT_SECRET", "GOOGLE_REFRESH_TOKEN"]:
            print(f"[HERMES] {key}: {'✅ set' if os.environ.get(key) else '❌ MISSING'}")

        from hermes_cli.main import main
        sys.argv = ["hermes", "gateway", "run", "--accept-hooks"]
        main()
    except Exception as e:
        print(f"[HERMES ERROR] {e}", flush=True)
        import traceback
        traceback.print_exc()


# ---- Web endpoint that keeps the container alive 24/7 -------------
@app.function(
    image=image,
    secrets=[modal.Secret.from_name("alpha-tours-env")],
    cpu=1.0,
    memory=1024,
    timeout=86400,
    min_containers=1,
    scaledown_window=3600,
)
@modal.concurrent(max_inputs=100)
@modal.asgi_app()
def fastapi_app():
    """ASGI app that runs Hermes in background + serves health check."""
    t = threading.Thread(target=_start_hermes, daemon=True)
    t.start()

    web_app = FastAPI(title="Alpha Tours Rome Bot")

    @web_app.get("/")
    @web_app.get("/health")
    async def health():
        return Response(
            content='{"status":"ok","bot":"alpha-tours-rome-bot","uptime":"running"}',
            media_type="application/json",
        )

    @web_app.get("/logs")
    async def show_logs():
        try:
            log_path = Path("/root/.hermes/logs/gateway.log")
            if log_path.exists():
                content = log_path.read_text(encoding="utf-8", errors="replace")
                return Response(content=content[-10000:], media_type="text/plain; charset=utf-8")
            else:
                return Response(content="[no gateway.log yet]", media_type="text/plain")
        except Exception as e:
            return Response(content=f"[error reading logs] {e}", media_type="text/plain")

    return web_app


# ---- Local entrypoint: instructions -------------------------------
@app.local_entrypoint()
def cli():
    print()
    print("=" * 55)
    print("  Alpha Tours Rome — Cloud Deploy")
    print("=" * 55)
    print()
    print("  To deploy:")
    print("    modal deploy modal_deploy.py")
    print()
    print("  Features:")
    print("    ✅ CEO Mode (Telegram ID 5285215270)")
    print("    ✅ Review checker (execute_code Python)")
    print("    ✅ Review poster (Google Business Profile API)")
    print("    ✅ Web editor (git push via execute_code)")
    print()
    print("  To stop:")
    print("    modal app stop alpha-tours-rome-bot")
    print()
    print("  Dashboard:")
    print("    https://modal.com/apps/pierpoljak024/main/deployed/alpha-tours-rome-bot")
    print()
