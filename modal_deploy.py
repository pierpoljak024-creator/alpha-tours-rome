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
You can edit HTML files and commit/push to GitHub. This is how it works:

1. **Show the file to the CEO first** — run this command (replace FILENAME.html with the actual file):
   ```
   python -c "from pathlib import Path; f = Path('/root/repo/alpha-tours-rome/tours/FILENAME.html'); print(f.read_text()[:3000])"
   ```

2. **Wait for the CEO to tell you exactly what to change** (e.g. "change €140 to €150")

3. **Make the change** using a Python one-liner:
   ```
   python -c "from pathlib import Path; f = Path('/root/repo/alpha-tours-rome/tours/FILENAME.html'); c = f.read_text(); c = c.replace('OLD_TEXT', 'NEW_TEXT'); f.write_text(c); print('✅ File updated!')"
   ```

4. **Commit and push to GitHub**:
   ```
   cd /root/repo/alpha-tours-rome && git add -A && git commit -m 'fix: updated content' && git push
   ```

5. Tell the CEO: "✅ Updated! Netlify will deploy automatically in ~1 minute."

IMPORTANT: Always run these as shell commands (the system will execute them and show you the output). Never write Python code blocks — use python -c one-liners instead.

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


def _init_tools():
    """Write Python scripts + seen-reviews.json + cache.json to tools/."""
    tools_dir = REPO_DIR / "tools"
    tools_dir.mkdir(parents=True, exist_ok=True)

    # Write check_reviews.py (with caching of account/location names + null-safe cache)
    (tools_dir / "check_reviews.py").write_text(r"""#!/usr/bin/env python3
import json, os, sys, time
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from urllib.parse import urlencode
from pathlib import Path
H = Path(__file__).parent
SF = H / "seen-reviews.json"
OF = H / "new-reviews.json"
CF = H / "cache.json"
CID = os.environ.get("GOOGLE_CLIENT_ID")
CSEC = os.environ.get("GOOGLE_CLIENT_SECRET")
REF = os.environ.get("GOOGLE_REFRESH_TOKEN")
if not all([CID, CSEC, REF]):
    print("Google OAuth not configured."); sys.exit(1)
def ac(u, data=None, headers=None, r=4):
    for a in range(r):
        try:
            req = Request(u, data=data, headers=headers or {})
            return json.loads(urlopen(req).read())
        except HTTPError as e:
            if e.code == 429 and a < r - 1:
                w = (2 ** a) * 2; print(f"  RL. Wait {w}s..."); time.sleep(w); continue
            raise
body = urlencode({"client_id": CID, "client_secret": CSEC, "refresh_token": REF, "grant_type": "refresh_token"}).encode()
t = ac("https://oauth2.googleapis.com/token", data=body, headers={"Content-Type": "application/x-www-form-urlencoded"}).get("access_token")
print("Token.")
hdrs = {"Authorization": f"Bearer {t}"}
if CF.exists():
    try:
        c = json.loads(CF.read_text()); an = c.get("an"); ln = c.get("ln")
        if an and ln:
            print(f"Cache: {an} / {ln}")
        else:
            raise ValueError("empty cache")
    except Exception:
        an = ln = None
if not an or not ln:
    accts = ac("https://mybusinessaccountmanagement.googleapis.com/v1/accounts", headers=hdrs).get("accounts", [])
    print(f"Accounts: {len(accts)}")
    if not accts: print("No accounts."); sys.exit(1)
    an = accts[0]["name"]; locs = []; time.sleep(1)
    for b in ["mybusinessbusinessinformation.googleapis.com/v1", "mybusiness.googleapis.com/v4"]:
        try:
            r = ac(f"https://{b}/{an}/locations", headers=hdrs); locs = r.get("locations", [])
            locs = [l for l in locs if l.get("name")]; break
        except HTTPError as e:
            if e.code != 404: print(f"  {b}: {e.code}")
    if not locs: print("No locations."); sys.exit(1)
    ln = locs[0]["name"]
    CF.write_text(json.dumps({"an": an, "ln": ln})); print(f"Cached: {an} / {ln}")
seen = set(json.loads(SF.read_text())) if SF.exists() else set()
revs = []; time.sleep(1)
for b in ["mybusinessbusinessinformation.googleapis.com/v1", "mybusiness.googleapis.com/v4", "mybusiness.googleapis.com/v3"]:
    try:
        d = ac(f"https://{b}/{ln}/reviews", headers=hdrs); revs = d.get("reviews", []); break
    except HTTPError as e:
        if e.code != 404: print(f"  {b}: {e.code}")
nr = [r for r in revs if r.get("reviewId", "") not in seen]
lt = ln.split("/")[-1]
print(f"\\n{lt}: {len(revs)} total, {len(nr)} new")
for r in nr:
    n = r.get("reviewer", {}).get("displayName", "?")
    r2 = r.get("starRating", 5); t2 = r.get("comment", "")[:200]
    print(f"  {n} ({r2}*): {t2}")
OF.write_text(json.dumps(nr, indent=2) if nr else "[]")
print(f"\\n{len(nr)} new." if nr else "\\nNo new.")""", encoding="utf-8")

    # Write post_review_reply.py (REAL posting, not stub)
    (tools_dir / "post_review_reply.py").write_text(r"""#!/usr/bin/env python3
import json, os, sys, time
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from urllib.parse import urlencode
from pathlib import Path
H = Path(__file__).parent
DF = H / "pending-drafts.json"
SF = H / "seen-reviews.json"
CF = H / "cache.json"
if not DF.exists(): print("No drafts."); sys.exit(0)
drafts = json.loads(DF.read_text())
if not drafts: print("No drafts."); sys.exit(0)
print(f"{len(drafts)} draft(s).")
CID = os.environ.get("GOOGLE_CLIENT_ID")
CSEC = os.environ.get("GOOGLE_CLIENT_SECRET")
REF = os.environ.get("GOOGLE_REFRESH_TOKEN")
if not all([CID, CSEC, REF]): print("OAuth not configured."); sys.exit(0)
def ac(u, d=None, h=None, r=4):
    for a in range(r):
        try:
            req = Request(u, data=d, headers=h or {}); return json.loads(urlopen(req).read())
        except HTTPError as e:
            if e.code == 429 and a < r - 1:
                w = (2**a)*2; print(f"  RL. Wait {w}s..."); time.sleep(w); continue
            raise
body = urlencode({"client_id":CID,"client_secret":CSEC,"refresh_token":REF,"grant_type":"refresh_token"}).encode()
token = ac("https://oauth2.googleapis.com/token", d=body, h={"Content-Type":"application/x-www-form-urlencoded"}).get("access_token")
print("Token obtained.")
if CF.exists():
    try:
        c = json.loads(CF.read_text()); an = c.get("an"); ln = c.get("ln")
        if an and ln: print(f"Cache: {an} / {ln}")
        else: raise ValueError
    except Exception: an=ln=None
if not an or not ln:
    time.sleep(1); hd = {"Authorization":f"Bearer {token}"}
    accts = ac("https://mybusinessaccountmanagement.googleapis.com/v1/accounts", h=hd).get("accounts",[])
    if not accts: sys.exit(1)
    an = accts[0]["name"]; time.sleep(1)
    locs = ac(f"https://mybusinessbusinessinformation.googleapis.com/v1/{an}/locations", h=hd).get("locations",[])
    if not locs: sys.exit(1)
    ln = locs[0]["name"]
    CF.write_text(json.dumps({"an":an,"ln":ln})); print(f"Cached: {an} / {ln}")
time.sleep(1); hd = {"Authorization":f"Bearer {token}"}
revs = ac(f"https://mybusiness.googleapis.com/v4/{ln}/reviews", h=hd).get("reviews",[])
posted = 0
for d in drafts:
    match = next((r for r in revs if r.get("reviewId")==d.get("reviewId")), None)
    if not match: print(f"Skip {d.get('name','?')} — no match"); posted+=1; continue
    apiname = match["name"]; time.sleep(0.5)
    try:
        b = json.dumps({"comment":{"text":d.get("draftReply","Thanks!")}}).encode()
        urlopen(Request(f"https://mybusiness.googleapis.com/v4/{apiname}/reply", data=b, headers={"Authorization":f"Bearer {token}","Content-Type":"application/json"}))
        print(f"Posted to {d.get('name','?')} ({d.get('rating',5)}*)")
        posted+=1
    except HTTPError as e:
        eb = e.read().decode(); print(f"Fail {d.get('name','?')}: HTTP {e.code} {eb[:200]}")
    except Exception as ex: print(f"Fail {d.get('name','?')}: {ex}")
seen = set(json.loads(SF.read_text())) if SF.exists() else set()
seen.update(d["reviewId"] for d in drafts if d.get("reviewId"))
SF.write_text(json.dumps(list(seen))); DF.write_text("[]")
print(f"Done. {posted}/{len(drafts)} posted.")""", encoding="utf-8")

    # seen-reviews.json + cache.json placeholders
    seen_file = tools_dir / "seen-reviews.json"
    if not seen_file.exists():
        seen_file.write_text("[]")
        print("[TOOLS] seen-reviews.json initialized.")
    cache_file = tools_dir / "cache.json"
    if not cache_file.exists():
        cache_file.write_text("{}")
        print("[TOOLS] cache.json initialized (empty, will fetch on first use).")

    print("[TOOLS] check_reviews.py + post_review_reply.py written.")


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
            _init_tools()
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
