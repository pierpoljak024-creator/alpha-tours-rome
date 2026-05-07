# Piano: Sistema Gestione Recensioni — COPY/PASTE ONLY ✅

> **⚠️ DECISIONE (06/05/2026): Solo copia/incolla**
> Hermes NON posta automaticamente le reply via OAuth.
> Workflow: Hermes genera draft → CEO copia/incolla su business.google.com → CEO conferma ("fatto") → Hermes aggiorna tracking (`replied --all`).
> Il comando `post` in `tools/review-manager.mjs` è DISABLED.

## Stato attuale ✅
- `tools/review-manager.mjs` — funziona: `fetch`, `draft`, `show`, `list`, `approve`, `replied`
- Tracking: 3 replied (Niedziela) · 21 awaiting reply (nel file replied-reviews.json)

## Obiettivo
Far sì che quando il CEO dice "check reviews" o "recensioni in attesa", Hermes:
1. Esegue `fetch` per trovare nuove recensioni
2. Genera draft brand-voice con `draft`
3. Mostra i draft con `show` (CEO copia/incolla su business.google.com)
4. Quando CEO conferma, esegue `replied --all` per aggiornare tracking

---

## Workflow finale

### Per il CEO
1. **"check reviews"** → Hermes fa `fetch` → mostra nuove recensioni
2. **"recensioni in attesa"** → Hermes fa `list` → mostra tutte con ✅/❌
3. **"mostrami i draft"** → Hermes fa `show` → mostra drafts da copiare
4. **"mostra le reply pronte"** → Hermes fa `show` → mostra i draft pronti
5. **CEO copia/incolla su business.google.com manualmente**
6. **"fatto" / "ho postato"** → Hermes fa `replied --all` → aggiorna tracking

### Comandi Hermes
| CEO dice | Hermes esegue |
|----------|---------------|
| "check reviews" | `fetch` → mostra nuove |
| "recensioni in attesa" | `list` → mostra tutte con ✅/❌ |
| "mostrami i draft" | `show` → mostra drafts pending |
| "fatto" / "ho postato" | `replied --all` → aggiorna tracking |

---

## Struttura dati
- `tools/all-reviews.json` — Archivio cumulativo di tutte le 23 recensioni
- `tools/seen-reviews.json` — IDs recensioni già processate
- `tools/new-reviews.json` — Nuove recensioni non ancora draftate
- `tools/pending-drafts.json` — Draft pronti per copia/incolla
- `tools/replied-reviews.json` — IDs recensioni a cui è stata data reply
- `tools/seed-reviews.mjs` — Script one-time per seed iniziale

## Seed data
- 23 recensioni totali (tutte ⭐5)
- 9 con reply già postata su Google (da seed: hasReply=true)
- 14 in attesa di reply
- Le 5 più recenti arrivano da Places API, il resto è seedato
