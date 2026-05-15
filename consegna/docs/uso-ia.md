# Uso dell'IA nel progetto

> Questa pagina serve a dichiarare **in modo onesto e granulare** come avete usato assistenti IA (ChatGPT, Claude, Copilot, Gemini, ecc.) durante lo sviluppo. È obbligatoria. Va scritta **da voi**, non dall'IA.

---

### Template

**Dove**: `generator.py`, funzione `generate_trial` (righe 8-17)

**Cosa abbiamo chiesto**: copilot ci ha aiutate a completare la funzione poichè inizialmente non funzionava, ci ha corretto l'errore.

**Cosa ci ha suggerito**: di fare un controllo per le lettere vocali e consonanti
---
**Dove**: `rules.py`, funzione `compute_expected_answer` (righe 8-17)

**Cosa abbiamo chiesto**: abbiamo chiesto a chat di corregerci la funzione

**Cosa ci ha suggerito**: inizialmente avevamo messo position == letter ci ha detto di mettere  top e bottom
---
**Dove**: `ui.py`, funzione 

**Cosa abbiamo chiesto**: abbiamo chiesto a copilot di migliorare la grafica del gioco di riordinarla e ferla più comprensibile

**Cosa ci ha suggerito**: inizialmente avevamo messo position == letter ci ha detto di mettere  top e bottom
---
**Dove**: `architettura.py`

**Cosa abbiamo chiesto**: abbiamo chiesto a gemini di aiutarci a mappare l'architettura partendo dai nostri file
---

## Cosa non abbiamo chiesto all'IA

- per adesso non abbiamo chiesto nulla nei file models, scoring, ui
- tutti i file di docs
- la logica del generatore
- La struttura del devlog.md e la stesura dei commenti nel codice.

---
