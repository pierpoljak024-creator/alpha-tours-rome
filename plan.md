# 📋 Alpha Tours Rome — Project Plan

## ✅ Completato
- [x] Bot deployato su Modal (24/7)
- [x] **CEO Mode**: SOUL.md riconosce owner (Telegram ID 5285215270)
- [x] **web-editor skill**: Hermes modifica HTML + git push (base)
- [x] **review-manager skill**: Hermes gestisce recensioni Google
- [x] **Google Business Profile API**: OAuth 2.0 configurato
- [x] **GitHub token** + **Google OAuth** su Modal secret
- [x] `hermes doctor` ✅ — config locale OK
- [x] **T1**: One-shot customer query test ✅

## 🔍 Scoperte Chiave (May 5, 2026)
- [x] Hermes ha **browser toolset** (`navigate`, `click`, `type`, `scroll`) — può fare screenshot!
- [x] Hermes ha **file toolset** (`read`, `write`, `patch`, `search`) — meglio di `python -c`
- [x] Puppeteer già installato (`C:/Users/pierf/node_modules/puppeteer`)
- [x] `serve.mjs` già pronto (server locale su localhost:3000)
- [x] SOUL.md attuale ha problemi: dice "EXECUTE" (non esiste), path hardcoded per Modal, nessun visual loop, nessun rollback, nessun skills index

## 🚀 Fase 1 — Skills System (da implementare)
- [ ] Creare `skills/index.md` — registry skills
- [ ] Creare `skills/web-editor.md` — skill modifica sito con preview visiva
- [ ] Creare `skills/design-system.md` — regole frontend (colori, font, componenti)
- [ ] Creare `skills/self-improve.md` — auto-miglioramento Hermes

## 🚀 Fase 2 — SOUL.md 2.0 (da implementare)
- [ ] Riscrivere `~/.hermes/SOUL.md` con:
  - Fix: "EXECUTE" → shell commands reali
  - Fix: percorsi locali + Modal (dual mode)
  - Nuovo: browser toolset per screenshot visivi
  - Nuovo: visual loop check (screenshot PRIMA → conferma → modifica → screenshot DOPO → approvazione → commit)
  - Nuovo: rollback (`git revert HEAD --no-edit && git push`)
  - Nuovo: skills index reference
  - Nuovo: self-improvement section
  - Mantenuto: brand voice, tour data, FAQ
- [ ] Aggiornare `modal_deploy.py` con stessa SOUL 2.0 inline

## 🚀 Fase 3 — TEST LIVE (da eseguire)
- [ ] **Test A**: Hermes fa screenshot di una pagina e lo mostra ✅
- [ ] **Test B**: Modifica semplice + screenshot PRIMA/DOPO + conferma CEO → commit
- [ ] **Test C**: Rollback ("annulla")
- [ ] **Test D**: Self-improvement — "Impara questo comando"
- [ ] Deploy su Modal dopo test passati

## 📐 Protocollo Comunicazione (CEO → Hermes)
```
TU: "Sulla pagina [TOUR NAME], cambia [TESTO VECCHIO] con [TESTO NUOVO]"
HERMES: 📸 Screenshot PRIMA + "Intendi questa parte?"
TU: "Sì" / "No, l'altra"
HERMES: Modifica + 📸 Screenshot DOPO
HERMES: "Confermi la modifica?"
TU: "Sì" → commit + push ✅
TU: "No" / "Annulla" → git revert + restore
```

## 📁 Skills Registry (nuovo)
| Skill | File | Scopo |
|-------|------|-------|
| review-manager | `skills/review-manager.md` | Recensioni Google |
| web-editor | `skills/web-editor.md` | Modifica sito con preview |
| design-system | `skills/design-system.md` | Linee guida frontend |
| self-improve | `skills/self-improve.md` | Auto-apprendimento |

## 📝 Note
- **Client secret corretto**: `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`
- **Refresh token corretto**: `1//096WoECPUC0v5CgYIARAAGAkSNwF-L9Ir7d7_gstTSuEvDMWSXgGvWkZ8M__UYMMhBDXy5T8VyiO5x7RW2B3_wuYDsTh436QAmC0`
- **Google API**: 429 rate limit colpito — aspettare prima di testare recensioni
