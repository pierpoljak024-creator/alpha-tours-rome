# HERMES AGENT v0.12.0 — Reference Manual

> Full technical reference for the Alpha Tours Rome Hermes deployment.
> Based on source code analysis of installed Hermes v0.12.0 (pip package),
> local config files, and the Modal deploy setup.

---

## 1. ARCHITECTURE OVERVIEW

```
┌─────────────────────────────────────────────────────┐
│                  USER (Telegram)                     │
└──────────────────────┬──────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────┐
│              GATEWAY (gateway/run.py)                │
│  ┌────────────┐ ┌──────────┐ ┌──────────────────┐   │
│  │ Telegram   │ │ WhatsApp  │ │ Discord / others  │   │
│  │ platform   │ │ platform  │ │ platforms         │   │
│  └─────┬──────┘ └──────────┘ └──────────────────┘   │
│        │                                              │
│  ┌─────▼────────────────────────────────────────────┐ │
│  │           Session Manager (session.py)            │ │
│  │  - Context tracking, persistence, reset policy   │ │
│  └─────────────────────┬────────────────────────────┘ │
└────────────────────────┼──────────────────────────────┘
                         │
┌────────────────────────▼──────────────────────────────┐
│              AGENT ENGINE (agent/)                     │
│  ┌──────────────┐  ┌──────────────┐  ┌────────────┐   │
│  │ Prompt       │  │ Tool Runner  │  │ Memory     │   │
│  │ Builder      │  │ (tools_config│  │ Provider   │   │
│  │ (reads SOUL) │  │  + hooks)    │  │            │   │
│  └──────┬───────┘  └──────┬───────┘  └────────────┘   │
│         │                 │                             │
│  ┌──────▼─────────────────▼──────────────────────────┐ │
│  │          TRANSPORT (transports/)                   │ │
│  │  chat_completions.py (OpenRouter/gemini via API)  │ │
│  │  anthropic.py (for Claude API)                    │ │
│  └─────────────────────┬────────────────────────────┘ │
└────────────────────────┼──────────────────────────────┘
                         │
┌────────────────────────▼──────────────────────────────┐
│          LLM PROVIDER (OpenRouter → Gemini API)        │
│          Model: google/gemini-2.0-flash-001            │
└───────────────────────────────────────────────────────┘
```

### Directory Layout

| Path | Purpose |
|------|---------|
| `hermes_cli/` | CLI entry point, config, gateway management |
| `gateway/` | Messaging platform adapters + run loop |
| `agent/` | Core AI agent (prompts, tools, shell hooks, transports) |
| `~/.hermes/` | User config: `config.yaml`, `SOUL.md`, `.env` |
| `$CWD/AGENTS.md` | Project-level context (auto-loaded) |

---

## 2. THE TOOLSET SYSTEM (Core for CEO Powers)

Hermes has **configurable toolsets** defined in `hermes_cli/tools_config.py`. The critical ones:

| Toolset | Tools | What it lets the AI do |
|---------|-------|----------------------|
| `terminal` | `terminal`, `process` | **Run shell commands** — THIS IS THE KEY ONE |
| `file` | `read`, `write`, `patch`, `search` | Read/write files directly |
| `code_execution` | `execute_code` | Run Python/JS snippets |
| `web` | `web_search`, `web_extract` | Browse the web |
| `browser` | `navigate`, `click`, `type`, `scroll` | Browser automation |

### ⚠️ KEY INSIGHT: How the "terminal tool" works

When the `terminal` toolset is **enabled** (as it should be for our setup), here's the flow:

1. The LLM is told it has a "terminal" tool available
2. In its response, the LLM **calls the terminal tool** with a command
3. The gateway/Runner sees this tool call → runs it via `subprocess.run()` with `shell=True`
4. The stdout+stderr output is returned to the LLM as a tool result
5. The LLM continues its response, interpreting the output

**This is NOT the same as "EXECUTE this Python code".** The correct mechanism is:
- The LLM **calls a tool** named "terminal" with parameter "command"
- Or: The LLM writes a code block and the **shell_hooks** module intercepts it

### How shell_hooks.py works (agent/shell_hooks.py)

This is the lower-level mechanism:
1. Pre-registered hooks match certain patterns (e.g. "run shell command")
2. When triggered, the hook runs the command via `subprocess.run()`
3. Output is captured and returned
4. Uses `--accept-hooks` flag to auto-approve (no TTY prompt needed in gateway mode)

---

## 3. SOUL.md — THE CORRECT WAY TO WRITE IT

### ❌ WRONG — What we have now

```
### POWER 3: Edit Website
EXECUTE this Python code to edit an HTML file:

```python
import subprocess, os
...
```
```

LLM doesn't have an "EXECUTE" command. It will either:
- Ignore the instruction
- Try to output Python code that gets treated as a normal message
- Get confused

### ✅ CORRECT — What we should use

For the LLM to **actually run a command**, the SOUL.md should say:

```
### POWER 3: Edit Website
You have the ability to run shell commands to edit the website.
When the CEO tells you what to change, run shell commands to:
1. Read the HTML file
2. Show the content to the CEO
3. Wait for the CEO to specify the exact change
4. Write the modified content
5. Git commit and push

To run a command, use the terminal tool with the command parameter.
Example of what you can do:
- cat tours/some-tour.html  (read a file)
- python -c "..."  (run Python one-liner to edit files)
- git add/commit/push
```

### Template for CEO powers

```
### POWER Name
When the CEO says "trigger phrase", follow these steps:
1. Run this shell command: `cd /path && command`
   (The system will execute it and show you the output)
2. Read the output and analyze it
3. Tell the CEO what you found
4. If more actions needed, run more commands

IMPORTANT: Write commands as inline code blocks (with backticks), 
not as fenced code blocks. The system interprets fenced code 
blocks as tool calls.
```

---

## 4. GATEWAY DEEP DIVE

### Gateway Architecture (gateway/run.py)

The main loop in `run.py`:
1. **Connects** to platform adapters (Telegram, etc.)
2. **Receives** messages from users
3. **Creates/resumes** sessions (session.py)
4. **Runs** the AI agent for each message
5. **Delivers** response back via platform adapter

### Key Parameters

| Parameter | Effect |
|-----------|--------|
| `--accept-hooks` | Auto-approve shell commands without TTY prompt |
| `--reset-policy` | Controls session freshness |
| `GATEWAY_ALLOW_ALL_USERS=true` | Allow all Telegram users (not just whitelist) |

### Platform Adapters (gateway/platforms/)

| Platform | Directory | Description |
|----------|-----------|-------------|
| Telegram | `gateway/platforms/telegram/` | Polling-based bot |
| WhatsApp | `gateway/platforms/whatsapp/` | Business API |
| Discord | `gateway/platforms/discord/` | Bot integration |
| Slack | `gateway/platforms/slack/` | Workspace integration |

### How Telegram works (our setup)

1. `start_telegram_gateway.py` sets env vars and calls `hermes gateway run`
2. Alternatively, on Modal: `_start_hermes()` runs `hermes gateway run --accept-hooks`
3. The Telegram platform polls Telegram API for new messages
4. Each message creates a session → feeds to AI agent → response sent back

---

## 5. CONFIGURATION

### ~/.hermes/config.yaml (our setup)

```yaml
provider: openrouter
model: google/gemini-2.0-flash-001
terminal:
  backend: local
```

### Important config keys (from hermes_cli/config.py)

| Key | Example | Effect |
|-----|---------|--------|
| `provider` | `openrouter` | Which LLM provider to use |
| `model` | `google/gemini-2.0-flash-001` | Which model to call |
| `terminal.backend` | `local` | Run commands locally (vs modal) |
| `agent.gateway_timeout` | `1800` | Max seconds per turn (default 30min) |
| `toolsets` | `["terminal", "file"]` | Which tool groups are enabled |

### Environment Variables

```bash
OPENROUTER_API_KEY=sk-or-...      # Required for OpenRouter
TELEGRAM_BOT_TOKEN=...            # Required for Telegram gateway
GITHUB_TOKEN=ghp_...              # For web editing (git push)
GATEWAY_ALLOW_ALL_USERS=true      # Allow all Telegram users
GOOGLE_CLIENT_ID=...              # For Google Business Profile API
GOOGLE_CLIENT_SECRET=...          # For Google OAuth
GOOGLE_REFRESH_TOKEN=...          # For Google OAuth token refresh
```

---

## 6. SKILLS SYSTEM (skills/)

Hermes has a skills system at `agent/skill_*.py`:

| File | Purpose |
|------|---------|
| `skill_commands.py` | Skill lifecycle (list, view, install) |
| `skill_preprocessing.py` | Pre-process SOUL prompts |
| `skill_utils.py` | Common utilities |

Skills are AGENTS.md files loaded from `~/.hermes/skills/` and `$CWD/skills/`.

Our `skills/review-manager.md` is loaded by Hermes automatically when present.

### How skills work

1. Hermes scans `~/.hermes/skills/` and `$CWD/skills/` for `.md` files
2. Each file is appended to the system prompt as additional context
3. This is additive to SOUL.md (which is the primary identity)

---

## 7. HOW COMMAND EXECUTION WORKS IN PRACTICE

### In chat mode (terminal)

```
User: "check reviews"
Hermes (LLM): [calls terminal tool with: cd /path && python tools/check_reviews.py]
Gateway: [executes command, captures output]
Gateway: [sends output back to LLM as tool result]
Hermes (LLM): "Results: Found 2 new reviews..."
```

### Via Telegram gateway

Same flow, except:
- Input comes from Telegram message
- Output is sent back to Telegram chat
- Tool calls are auto-approved (--accept-hooks)

### What the LLM sees

The LLM's system prompt includes:
1. **SOUL.md** content (identity, CEO powers, tour data)
2. **AGENTS.md** content (company info, brand voice)
3. **Skills** content (review-manager.md)
4. **Tool definitions** (terminal, file, etc. — generated from config)

The LLM's tool-use loop:
1. LLM decides to use a tool → outputs tool call
2. System intercepts → runs the tool → returns result
3. LLM continues reasoning with the result

---

## 8. CURRENT SETUP — Alpha Tours Rome

### Local (Windows)

| Component | Location |
|-----------|----------|
| Hermes config | `C:\Users\pierf\.hermes\config.yaml` |
| SOUL.md | `C:\Users\pierf\.hermes\SOUL.md` |
| AGENTS.md | `C:\Users\pierf\AlphaTours-Project\AGENTS.md` |
| Skills | `C:\Users\pierf\AlphaTours-Project\skills\review-manager.md` |
| Start script | `C:\Users\pierf\AlphaTours-Project\start_telegram_gateway.py` |

### Modal (Cloud)

| Component | Location |
|-----------|----------|
| SOUL inline | In `modal_deploy.py` as `SOUL_CONTENT` string |
| Repo | `/root/repo/alpha-tours-rome/` |
| Tools | `/root/repo/alpha-tours-rome/tools/check_reviews.py` (etc.) |
| Secret | Modal secret `alpha-tours-env` |

### How Modal deploy works

```
modal_deploy.py:
├── SOUL_CONTENT (inline string → written to SOUL.md at runtime)
├── _init_tools() → writes Python scripts to tools/ dir
├── _start_hermes() → launches "hermes gateway run --accept-hooks"
├── FastAPI app → serves /health endpoint + /webhook
└── Runs 24/7 on Modal with secrets from alpha-tours-env
```

---

## 9. TROUBLESHOOTING

### Problem: "EXECUTE" command not working

**Cause:** SOUL.md says "EXECUTE this Python code" but Hermes has no `execute_code` tool enabled for that.

**Fix:** Rewrite SOUL.md to use terminal tool commands instead:
- `cd /path && python tools/check_reviews.py`
- NOT `EXECUTE this Python code: ...`

### Problem: Terminal tool not available

**Cause:** The `terminal` toolset is not enabled in config.

**Fix:** Either:
1. `hermes tools` → enable "Terminal & Processes"
2. Or add to config.yaml: `toolsets: ["terminal", "file"]`

### Problem: Command runs but output shows nothing useful

**Cause:** stderr not captured, or command runs in wrong directory.

**Fix:** Use `cd /root/repo/alpha-tours-rome && command 2>&1` to capture all output.

### Problem: Git push fails

**Cause:** GITHUB_TOKEN not set or wrong remote URL.

**Fix:**
```bash
git remote set-url origin https://TOKEN@github.com/user/repo.git
# Or use auth_url approach:
git push https://TOKEN@github.com/user/repo.git main
```

### Problem: Google API quota exhausted (HTTP 429)

**Cause:** Too many API calls in short time.

**Fix:** Wait ~24h for quota reset. Cache is implemented in `check_reviews.py`.

### Problem: Hermes gateway won't start

**Check:** Run `hermes doctor` to verify config and dependencies.

---

## 10. CHEAT SHEET

### Quick Commands

```bash
# Start Telegram gateway locally
python start_telegram_gateway.py

# Deploy to Modal
modal deploy modal_deploy.py

# Stop Modal app
modal app stop alpha-tours-rome-bot

# Check health
curl https://pierpoljak024--alpha-tours-rome-bot-fastapi-app.modal.run/health

# View Modal logs
modal app logs alpha-tours-rome-bot

# Run Hermes interactively
hermes

# Run one-shot query
hermes -z "What tours do you offer?" --provider openrouter

# Gateway status (local)
hermes gateway status

# Doctor check
hermes doctor
```

### File Locations

| File | Path |
|------|------|
| Hermes config | `~/.hermes/config.yaml` |
| SOUL.md | `~/.hermes/SOUL.md` |
| Local env | `~/.hermes/.env` |
| Shell hooks allowlist | `~/.hermes/shell-hooks-allowlist.json` |
| Project AGENTS.md | `./AGENTS.md` |
| Skills directory | `./skills/` or `~/.hermes/skills/` |
| Hermes CLI source | `.../site-packages/hermes_cli/` |
| Gateway source | `.../site-packages/gateway/` |
| Agent engine | `.../site-packages/agent/` |

### Important Config Keys

```yaml
# ~/.hermes/config.yaml
provider: openrouter
model: google/gemini-2.0-flash-001
terminal:
  backend: local
# Optional: enable specific toolsets
# toolsets:
#   - terminal
#   - file
#   - web
```

---

## 11. THE CORRECT POWER 3 (Web Editing) TEMPLATE

This is how POWER 3 should be written in SOUL.md:

```
### POWER 3: Edit Website
When the CEO says "change the price", "update text", or "edit the site":

1. First, show the relevant file by running:
   ```
   python -c "from pathlib import Path; f = Path('/root/repo/alpha-tours-rome/tours/FILENAME.html'); print(f.read_text()[:3000])"
   ```

2. Wait for the CEO to tell you exactly what to change.

3. After they specify the change, run:
   ```
   python -c "
   from pathlib import Path
   f = Path('/root/repo/alpha-tours-rome/tours/FILENAME.html')
   content = f.read_text()
   # Make the replacement
   content = content.replace('€140', '€150')
   f.write_text(content)
   print('Done! File updated.')
   "
   ```

4. Then commit and push:
   ```
   cd /root/repo/alpha-tours-rome && git add -A && git commit -m 'fix: updated price' && git push
   ```

5. Tell the CEO: "✅ Updated! Netlify will deploy automatically in ~1 minute."
```

### Web editing template for the local setup (Windows)

```
### POWER 3: Edit Website (LOCAL)
When CEO says "change the website":

1. Read the file and show first 3000 chars:
   ```
   python -c "p=__import__('pathlib').Path('tours/FILENAME.html'); print(p.read_text()[:3000])"
   ```

2. After CEO specifies changes, write the new content:
   ```
   python -c "
   p = __import__('pathlib').Path('tours/FILENAME.html')
   c = p.read_text()
   c = c.replace('OLD_TEXT', 'NEW_TEXT')
   p.write_text(c)
   print('Saved!')
   "
   ```

3. Commit and push:
   ```
   git add -A
   git commit -m 'fix: updated content'
   git push
   ```
```

---

## 12. HERMES UPDATE PROCEDURE

```bash
# Update Hermes to latest version
pip install --upgrade git+https://github.com/NousResearch/hermes-agent.git

# Or with pip directly (if package is on PyPI)
pip install --upgrade hermes-agent

# After update, check version
hermes --version

# Re-deploy on Modal after update
modal deploy modal_deploy.py
```

---

## 13. PLATFORM: OpenRouter + Gemini

Our config uses OpenRouter to access `google/gemini-2.0-flash-001`.

**OpenRouter features used:**
- Model: `google/gemini-2.0-flash-001`
- Base URL: `https://openrouter.ai/api/v1`
- API key format: `sk-or-v1-...`

**OpenRouter provider override:** If you want to force a specific provider:
```
OPENROUTER_PROVIDER=google  # Force Google's own infra
```

---

## 14. LOGS & DEBUGGING

### Where to find logs

| Context | Location |
|---------|----------|
| Local gateway | stdout (terminal where `start_telegram_gateway.py` runs) |
| Modal (stderr) | `modal app logs alpha-tours-rome-bot` |
| Modal stdout | Same command, look for `[stdout]` prefix |
| Telegram debug | Check `telegram_out.txt`, `telegram_err.txt` in project root |
| Hermes debug | Run `hermes doctor` for config diagnostics |

### Log collection for Modal

```bash
# Tail logs in real-time
modal app logs alpha-tours-rome-bot --follow

# Get recent logs (last 1000 lines)
modal app logs alpha-tours-rome-bot --tail 1000

# Filter for errors
modal app logs alpha-tours-rome-bot 2>&1 | findstr -i error
```

---

## 15. MIGRATION NOTES

### What changed from old setup

| Old | New | Reason |
|-----|-----|--------|
| `tools/check-reviews.mjs` (Node.js) | `tools/check_reviews.py` (Python) | Modal has Python, not Node |
| `.mjs` scripts with Place ID | `.py` scripts with OAuth | Place ID API deprecated |
| SOUL.md with "EXECUTE this Python code" | SOUL.md with shell commands | LLM doesn't have execute_code |
| `_init_seen_file()` | `_init_tools()` | Generate Python scripts at boot |
| Local only | Modal 24/7 | Always-on availability |
| Hermes config had model prefix | Plain model name | Correct format: `google/gemini-...` |

---

> **Last updated:** 2026-05-05
> **Hermes version installed:** 0.12.0
> **Project:** Alpha Tours Rome — https://alphatoursrome.com
