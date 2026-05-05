# 📋 Alpha Tours Rome — Project Plan

## ✅ Completato
- [x] Bot deployato su Modal (24/7, non si ferma più)
- [x] **CEO Mode**: SOUL.md riconosce l'owner (Telegram ID 5285215270)
- [x] **web-editor skill**: Hermes modifica HTML del sito e fa git push
- [x] **review-manager skill**: Hermes controlla recensioni Google e posta risposte automaticamente
- [x] **Google Business Profile API**: OAuth 2.0 configurato (refresh token)
- [x] **GitHub token** aggiunto al Modal secret
- [x] **Google OAuth credentials** aggiunte al Modal secret

## 🛠️ Fix applicati (maggio 2026)
- [x] **FIX: `tools/post_review_reply.py`** — rimosso stub "TBD in v2", ora fa la vera POST API di Google
- [x] **FIX: `tools/check_reviews.py`** — aggiunto `cache.json` con validazione null-safe (an/ln non più None)
- [x] **FIX: `modal_deploy.py` inline scripts** — idem, script aggiornati con posting reale + cache sicura
- [x] **FIX: `skills/review-manager.md`** — comandi cambiati da `node tools/...` a `python tools/...`
- [x] **FIX: `../.hermes/SOUL.md`** — aggiunti CEO powers (check reviews, post replies, edit website)
- [x] **Deploy su Modal** — `modal deploy modal_deploy.py` riuscito
- [x] **FIX: POWER 3 nella SOUL.md** — da `EXECUTE Python code` a `python -c one-liner`
- [x] **FIX: Config Hermes locale** — config.yaml aggiornato (model: provider: ...)
- [x] **FIX: API keys in `~/.hermes/.env`** — aggiunte OPENROUTER_API_KEY, TELEGRAM_BOT_TOKEN, etc.

## 🧪 Test Locali (5 maggio 2026)
### Test Eseguiti
- [x] **T1: Customer query (one-shot)** — `hermes -z "Ciao! What tours do you offer?"`
  - ✅ Risposta: guida locale, emoji, categorie tour, domande follow-up
- [x] **T2: Hermes doctor** — configurazione locale OK
  - ✅ API key configurata
  - ✅ Config validata
  - ✅ OpenRouter API funzionante
  - ✅ Terminal tool disponibile
  - ✅ File tool disponibile
- [ ] **T3: Google OAuth test** — `python test_gmb.py`
  - ✅ Access token ottenuto con refresh token
  - ❌ HTTP 429 (Too Many Requests) — rate limit Google My Business API
  - ⏳ Riprovare dopo 5-10 minuti
- [ ] **T4: Google OAuth con credenziali corrette in check_reviews.py**
  - ❌ Non testato (usato client_secret sbagliato nel primo tentativo)
  - 📝 Usare client_secret dal file JSON: `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`
- [ ] **T5: Gateway Telegram locale** — avviare `python start_telegram_gateway.py`
- [ ] **T6: CEO Power 1 — "check reviews" su Telegram**
- [ ] **T7: CEO Power 2 — "post replies" su Telegram**
- [ ] **T8: CEO Power 3 — "change price golf cart" su Telegram**

## 📝 Note Importanti
- **Client secret corretto**: `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` (da `google-business-oauth-token.json`)
- **Refresh token corretto**: `1//096WoECPUC0v5CgYIARAAGAkSNwF-L9Ir7d7_gstTSuEvDMWSXgGvWkZ8M__UYMMhBDXy5T8VyiO5x7RW2B3_wuYDsTh436QAmC0`
- **Google My Business API rate limit**: 429 dopo troppe chiamate — aspettare prima di riprovare
- **Obiettivo finale**: Deploy su Modal solo dopo TUTTI i test locali passati

## 📁 File creati/modificati
- `modal_deploy.py` — Main deploy script (CEO SOUL + inline tools + clone repo)
- `skills/review-manager.md` — Skill per recensioni (sync con python tools)
- `../.hermes/SOUL.md` — SOUL aggiornata con CEO powers **+ POWER 3 fixato**
- `../.hermes/config.yaml` — Config aggiornata (formato corretto con `model:`)
- `../.hermes/.env` — API keys aggiunte
- `tools/check_reviews.py` — Script fixato (cache null-safe, backoff)
- `tools/post_review_reply.py` — Script fixato (vera posting API, non stub)
- `tools/post-review-reply.mjs` — Versione Node.js alternativa (funzionante, ma non usata su Modal)
- `auth_google_business.py` — Script one-time per generare refresh token (già eseguito)
- `hermes-reference.md` — Documentazione tecnica Hermes (15 sezioni, ~350 righe)
- `CLAUDE.MD` — Aggiornato con sezione "Architecture insight" + Hermes fix docs
- `local_test_plan.md` — Piano di test locale creato con checklist
