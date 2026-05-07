# Hermes Environment Sync Plan

## Obiettivo
Sincronizzare l'ambiente **Locale (Windows)** e **Modal (Cloud)** in modo che entrambi funzionino con la stessa configurazione e gli stessi script di review management.

---

## Diagnosi — Cosa non va

### 1. I file `.mjs` non esistono su disco
Nella cartella `tools/`, i file `.mjs` sono aperti in VS Code ma **non sono mai stati salvati fisicamente**:
- ❌ `tools/review-manager.mjs` → NON esiste su disco
- ❌ `tools/seed-reviews.mjs` → NON esiste su disco
- ❌ `tools/review-watchdog.mjs` → NON esiste su disco

Conferma: `Test-Path` restituisce `False` per tutti.

Di conseguenza `node tools/review-manager.mjs show` fallisce con `MODULE_NOT_FOUND`.

### 2. Modal ha solo Python, non Node.js
`modal_deploy.py` crea script Python (`check_reviews.py`, `post_review_reply.py`) ma:
- Non installa Node.js
- Non crea `review-manager.mjs`
- Il SOUL.md dice di usare `node tools/review-manager.mjs`

### 3. Percorsi Windows su Linux
Il `SOUL.md` (sia in `../.hermes/SOUL.md` locale che embeddato in `modal_deploy.py`) usa:
```
cd c:\Users\pierf\AlphaTours-Project && node tools/review-manager.mjs ...
```
Ma su Modal Linux il percorso è `/root/repo/alpha-tours-rome/`.

### 4. I file `.mjs` non sono tracciati da git
`git ls-files tools/*.mjs` non restituisce nulla. Servono nel repo perché Modal li clona.

---

## Stato attuale dei dati (OK)
I file JSON in `tools/` esistono e sono validi:
- `all-reviews.json` — 24 recensioni (23 seed + Danna Schwenk)
- `pending-drafts.json` — 1 draft pending (Danna Schwenk)
- `replied-reviews.json` — 3 replied (Katarzyna, Anna, Agnieszka Niedziela)
- `new-reviews.json` — Danna Schwenk
- `seen-reviews.json` — 29 IDs (5 vecchi Places API + 24 nuovi)

---

## Piano di esecuzione

### Passo 1 — Salvare i file `.mjs` su disco
Creare fisicamente in `tools/`:
- `review-manager.mjs` (566 linee — già letto da cache VS Code)
- `seed-reviews.mjs` (309 linee — già letto da cache VS Code)
- `review-watchdog.mjs` (da leggere e salvare)

### Passo 2 — Aggiornare `modal_deploy.py`
Modifiche necessarie:
- **Aggiungere Node.js** all'immagine Modal:
  ```python
  modal.Image.from_registry("python:3.12", setup_dockerfile_commands=[
      "RUN apt-get update && apt-get install -y nodejs npm git locales",
      ...
  ])
  ```
- **Aggiornare il SOUL embeddato**: tutti i percorsi `c:\Users\pierf\AlphaTours-Project` → `/root/repo/alpha-tours-rome/`
- **Rimuovere** la creazione di `check_reviews.py` e `post_review_reply.py` (obsoleti)
- Aggiungere `_init_mjs_tools()` che copia/verifica i file `.mjs`

### Passo 3 — Git commit + push
```bash
git add tools/review-manager.mjs tools/seed-reviews.mjs tools/review-watchdog.mjs
git add modal_deploy.py
git commit -m "fix: sync review-manager.mjs across local and Modal environments"
git push
```

### Passo 4 — Deploy su Modal
```bash
modal deploy modal_deploy.py
```

### Passo 5 — Test locale
```bash
node tools/review-manager.mjs show
```

---

## Architettura finale

| Componente | Locale (Windows) | Modal (Cloud) |
|-----------|-----------------|---------------|
| **Review script** | `review-manager.mjs` (Node.js) | `review-manager.mjs` (Node.js) |
| **API Reviews** | Places API v1 (API Key) | Places API v1 (API Key) |
| **Node.js** | v22.14.0 ✅ | Installato via apt ✅ |
| **Percorso** | `c:\Users\pierf\AlphaTours-Project` | `/root/repo/alpha-tours-rome` |
| **SOUL.md sorgente** | `../.hermes/SOUL.md` | Embeddato in `modal_deploy.py` |
| **Dati JSON** | Stessi file in `tools/` | Stessi file (clonati da git) |
| **Sync** | Stesso codice git | Stesso codice git |

---

## Comandi di verifica

```bash
# Mostra stato reviews
node tools/review-manager.mjs show

# Elenca tutte le recensioni
node tools/review-manager.mjs list

# Fetch nuove recensioni
node tools/review-manager.mjs fetch

# Genera draft
node tools/review-manager.mjs draft

# Approva draft (dopo copia/incolla su business.google.com)
node tools/review-manager.mjs approve

# Segna come replied
node tools/review-manager.mjs replied --all
```

---

## Note
- Il sistema rimane **copy/paste only** — le reply vanno postate manualmente su business.google.com
- Il watchdog (`review-watchdog.mjs`) può girare automaticamente ogni 6 ore
- I file JSON sensibili (`seen-reviews.json`, `all-reviews.json`, etc.) sono in `.gitignore` e non finiscono su git — solo i `.mjs` vanno tracciati
