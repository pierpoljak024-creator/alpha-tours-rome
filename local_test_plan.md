# 🧪 Local Test Plan — Alpha Tours Rome Bot

## Setup
- `hermes doctor` ✅ — tutto OK
- Config yaml ✅ — aggiornata
- API keys in `~/.hermes/.env` ✅
- Hermes v0.12.0 ✅

## Test Suite

### [x] T1: Risposta base customer
- **Comando:** `hermes -z "Ciao! What tours do you offer?"`
- **Risultato:** ✅ Risposta calda con categorie tour + emoji + domande follow-up

### [ ] T2: Gateway Telegram locale
- **Azione:** Avviare gateway con `python start_telegram_gateway.py`
- **Verifica:** Bot risponde a messaggi su Telegram

### [ ] T3: CEO Power 1 — Check Reviews
- **Azione:** Mandare "check reviews" su Telegram (da account CEO)
- **Verifica:** Hermes esegue `python tools/check_reviews.py` e mostra risultati

### [ ] T4: CEO Power 2 — Post Replies
- **Azione:** Mandare "post replies" su Telegram (dopo aver generato draft)
- **Verifica:** Hermes esegue `python tools/post_review_reply.py`

### [ ] T5: CEO Power 3 — Web Editing
- **Azione:** Mandare "change price golf cart" su Telegram
- **Verifica:** Hermes legge file HTML, chiede conferma, fa replace + git push

### [ ] T6: Test strumenti locali (senza Telegram)
- **Azione:** `python tools/check_reviews.py`
- **Verifica:** Script funziona con le credenziali Google OAuth

---

## Come eseguire
1. `python start_telegram_gateway.py` → avvia bot locale
2. Da Telegram (@AlphaToursRomeBot): mandare messaggi di test
3. Controllare output nel terminale del gateway
