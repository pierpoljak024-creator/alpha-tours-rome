# self-improve — Auto-apprendimento e Aggiornamento Skills

## Quando usare questa skill
Quando il CEO dice: "impara questo comando", "aggiorna le tue skills", "aggiungi questa capacità", "ricordati di fare [X] quando ti chiedo [Y]".

## Workflow

### 1. Identifica cosa deve imparare
Chiedi al CEO di specificare:
- **Trigger** — cosa deve dire il CEO per attivare la nuova capacità?
- **Azione** — cosa deve fare Hermes?
- **File da modificare** — va in SOUL.md o in una nuova skill?

### 2. Scegli dove metterlo

| Se... | Allora... |
|-------|-----------|
| È una regola generale di comportamento | Aggiorna `SOUL.md` |
| È un workflow complesso (+5 passi) | Crea nuova skill in `skills/NOME.md` |
| È una regola di design | Aggiorna `skills/design-system.md` |
| È una modifica al workflow di web editing | Aggiorna `skills/web-editor.md` |

### 3. Crea o aggiorna il file
Usa il file toolset (read/write) o python -c per modificare il file.

### 4. Aggiorna skills/index.md (se nuova skill)
Aggiungi una riga alla tabella in `skills/index.md`.

### 5. Conferma al CEO
```
✅ Skill aggiornata! Ora quando mi dirai "[TRIGGER]", farò [AZIONE]."
```

## Esempi

### Esempio 1: Nuova regola semplice
```
CEO: "Quando ti dico 'pulisci la cache', cancella i file .pyc dalla cartella tools/"
HERMES: Aggiunge regola a SOUL.md → "✅ Fatto! Ora quando dici 'pulisci la cache', cancello i .pyc."
```

### Esempio 2: Nuova skill complessa
```
CEO: "Voglio che quando ti dico 'genera report', leggi le recensioni, fai un'analisi e salvi un file markdown"
HERMES: Crea skills/report-generator.md + aggiorna index.md → "✅ Nuova skill 'report-generator' creata!"
```

## Importante
- **Leggi sempre il file prima di modificarlo** — non sovrascrivere senza vedere il contenuto attuale
- **Chiedi conferma** al CEO prima di applicare modifiche
- **Non creare skill duplicate** — controlla skills/index.md prima di crearne una nuova
