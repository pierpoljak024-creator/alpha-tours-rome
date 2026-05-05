# web-editor — Modifica il sito con preview visiva

## Quando usare questa skill
Quando il CEO dice: "cambia il prezzo", "aggiorna il testo", "modifica la pagina", "edit the site", "cambia [X] in [Y] sulla pagina [Z]".

## Workflow Completo (Visual Loop Check)

### Passo 1: Identifica il file
Usa la mappa dei tour in SOUL.md per trovare il file HTML corretto.

Esempi:
- "Rome Highlights Private Tour by Golf Cart" → `tours/golf-cart-rome-highlights-private.html`
- "Homepage" → `index.html`
- "Golf Cart category page" → `golf-cart.html`

### Passo 2: Screenshot PRIMA
Se sul server locale (`http://localhost:3000`):
```
node -e "
const p = require('c:/Users/pierf/node_modules/puppeteer');
(async()=>{
  const b = await p.launch({
    executablePath: 'c:/Users/pierf/.cache/puppeteer/chrome/win64-146.0.7680.153/chrome-win64/chrome.exe',
    headless: true,
    args: ['--no-sandbox']
  });
  const page = await b.newPage();
  await page.setViewport({width:1400,height:900});
  await page.goto('http://localhost:3000/tours/golf-cart-rome-highlights-private.html', {waitUntil:'networkidle2'});
  await page.screenshot({path:'design/screenshots/before-mod.png',fullPage:true});
  await b.close();
  console.log('Screenshot saved: design/screenshots/before-mod.png');
})();
"
```

Se il server NON è attivo, avviarlo prima:
```
start /B node serve.mjs
```

### Passo 3: Mostra screenshot al CEO
Leggi il file PNG con il Read tool e mostra il risultato al CEO.
Chiedi: "È questa la parte che vuoi modificare?"

### Passo 4: Modifica locale (NON committare ancora!)
Usa il `file` toolset di Hermes (read, write, patch, search) OPPURE python -c:

**Opzione A — file toolset (se disponibile):**
Usa `read` per leggere il file, `patch` per fare la sostituzione.

**Opzione B — python -c (fallback sicuro):**
```
python -c "
p = __import__('pathlib').Path('tours/FILENAME.html')
c = p.read_text()
c = c.replace('TESTO VECCHIO', 'TESTO NUOVO')
p.write_text(c)
print('✅ File modificato localmente!')
"
```

### Passo 5: Screenshot DOPO
Stesso comando del Passo 2, ma salva in `design/screenshots/after-mod.png`.

### Passo 6: Mostra PRIMA/DOPO al CEO
Leggi entrambi i PNG e mostra le differenze.
Chiedi: "Confermi la modifica? (Sì/No/Annulla)"

### Passo 7: Commit (se approvato)
```
git add -A
git commit -m 'fix: [breve descrizione della modifica]'
git push
```
Poi: "✅ Fatto! Netlify deploy in ~1 minuto."

### Passo 8: Rollback (se "annulla")
```
git checkout -- tours/FILENAME.html
```
Oppure se già committato:
```
git revert HEAD --no-edit && git push
```
Poi: "↩️ Modifica annullata."

## Regole importanti
- **MAI committare senza approvazione del CEO** — sempre chiedere conferma prima
- **MAI modificare senza screenshot PRIMA** — il CEO deve vedere cosa stai per cambiare
- **Mostra sempre PRIMA/DOPO** dopo la modifica
- **Se il CEO dice "annulla"**, fai rollback immediatamente
- **Usa `fullPage: true`** negli screenshot per catturare tutta la pagina
- **Se il CEO non specifica il file**, usa la mappa tour in SOUL.md per capire quale pagina

## Comandi rapidi
```bash
# Avviare server locale
start /B node serve.mjs

# Screenshot
node -e "const p=require('c:/Users/pierf/node_modules/puppeteer');(async()=>{const b=await p.launch({executablePath:'c:/Users/pierf/.cache/puppeteer/chrome/win64-146.0.7680.153/chrome-win64/chrome.exe',headless:true,args:['--no-sandbox']});const page=await b.newPage();await page.setViewport({width:1400,height:900});await page.goto('http://localhost:3000/PAGINA',{waitUntil:'networkidle2'});await page.screenshot({path:'design/screenshots/FILE.png',fullPage:true});await b.close();console.log('OK')})()"

# Rollback locale (se non ancora committato)
git checkout -- tours/FILENAME.html

# Rollback remoto (se già committato e pushato)
git revert HEAD --no-edit && git push
```
