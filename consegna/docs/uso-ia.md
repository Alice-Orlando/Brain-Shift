# Uso dell'IA nel progetto

> Questa pagina serve a dichiarare **in modo onesto e granulare** come avete usato assistenti IA (ChatGPT, Claude, Copilot, Gemini, ecc.) durante lo sviluppo. È obbligatoria. Va scritta **da voi**, non dall'IA.

---

## Politica del progetto

L'IA è consentita come assistente (spiegazioni, suggerimenti, debug, codice di dettaglio ben compreso) ma non come risolutore automatico (generazione e consegna di codice non compreso). Le parti di **documentazione e metacognizione** (questa pagina inclusa, `devlog.md`, `scelte.md`) vanno scritte senza IA.

---

## Strumenti usati

Elencate gli strumenti IA che il gruppo ha effettivamente usato durante il progetto:

- [ ] ChatGPT 
- [ ] Claude 
- [ ] GitHub Copilot
- [ ] Gemini 

Se non avete usato IA, dichiaratelo esplicitamente.

---

## Uso granulare per modulo / parte

Per **ogni parte del codice** in cui avete usato l'IA, una entry strutturata. Copiate il template sottostante quante volte serve.

### Template

**Dove**: `generator.py`, funzione `generate_trial` (righe 8-17)

**Cosa abbiamo chiesto**: copilot ci ha aiutate a completare la funzione poichè inizialmente non funzionava, ci ha corretto l'errore.

**Cosa ci ha suggerito**: di fare un controllo per le lettere vocali e consonanti


**Dove**: `rules.py`, funzione `compute_expected_answer` (righe 8-17)

**Cosa abbiamo chiesto**: abbiamo chiesto a chat di corregerci la funzione

**Cosa ci ha suggerito**: inizialmente avevamo messo position == letter ci ha detto di mettere  top e bottom


**Dove**: `ui.py`, funzione 

**Cosa abbiamo chiesto**: abbiamo chiesto a copilot di migliorare la grafica del gioco di riordinarla e ferla più comprensibile

**Cosa ci ha suggerito**: inizialmente avevamo messo position == letter ci ha detto di mettere  top e bottom


**Cosa abbiamo fatto**:
- [ ] accettato integralmente
- [ ] modificato adattandolo al nostro codice
- [ ] preso solo l'idea e riscritto
- [ ] rifiutato, perché…

**Perché**: se avete modificato o rifiutato, spiegate cosa non andava. Se avete accettato integralmente, spiegate come avete verificato che il codice fosse corretto.

---

## Verifiche di comprensione

Dopo ogni uso dell'IA su parti di codice non banali, fatevi questa domanda: «Se il docente mi chiede di spiegare questa riga all'orale, so farlo?». Se la risposta è no, fermatevi e chiedete all'IA di *spiegare*, non di *scrivere*.

All'orale, ogni membro del gruppo deve saper spiegare ogni parte del codice. Se avete usato l'IA senza capire, all'orale si vede immediatamente.

---

## Cosa non abbiamo chiesto all'IA

Elencate esplicitamente le parti che avete scritto **senza** assistenza IA. Serve a voi per esercitare la consapevolezza, e al docente per avere un confronto.

Esempi:
- tutti i test pytest
- per adesso non abbiamo chiesto nulla nei file models, scoring, ui
- tutti i file di docs
- la logica del generatore
-

---

### Domande-guida

1. La dichiarazione è **granulare** (modulo per modulo, funzione per funzione) o generica («abbiamo usato ChatGPT qualche volta»)?
2. Per ogni uso dell'IA sapreste rispondere se il docente vi chiedesse «spiegami perché questa riga fa così»?
3. Avete distinto fra *chiedere spiegazioni* e *far scrivere codice*?
4. Questa pagina è coerente con quello che il docente vedrà leggendo il codice?
