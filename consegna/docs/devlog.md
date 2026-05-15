# Devlog — Brain Shift

> Diario di bordo del gruppo. Una entry alla settimana (minimo tre, una per settimana di lavoro). Scritto **da voi**, non dall'IA.

---

## Entry

### Settimana 1 (22-28 aprile 2026)
Abbiamo definito la struttura dati Trial e implementato la logica di gioco in rules.py, che valida numeri pari o vocali in base alla posizione "TOP" o "BOTTOM". Abbiamo inoltre scritto il generatore casuale degli stimoli, il sistema di calcolo del punteggio e una prima funzione per il rendering grafico delle carte su Pygame. Fortunatamente non abbiamo perso tempo, abbiamo lavorato bene. Abbiamo imparato a usare le dataclasses per gestire i dati del gioco in modo pulito. Tecnicamente, abbiamo approfondito l'integrazione tra la logica pura di Python e il ciclo di rendering di Pygame per separare i dati dalla UI. Abbiamo scartato l'idea di input complessi, optando per una risposta booleana (True/False) basata sulle regole prefissate. Pianifichiamo di implementare la gestione degli eventi della tastiera nel loop principale di main.py. Vogliamo inoltre aggiungere un timer per limitare il tempo di risposta e dei feedback visivi immediati per indicare se la risposta data dall'utente è corretta o errata. Per quanto riguarda la suddivisone del lavoro non ci siamo oragnizzate effettivamente, ma stiamo cercando di fare tutto insieme cos' da capire bene cosa facciamo. Dobbiamo solo organizzarci meglio ma per il resto siamo soddisfatte.


### Settimana 2 (29 aprile - 5 maggio 2026)

In questa settimana siamo andate avanti con le fasi e siamo arrivate fino alla fase 9, abbiamo fatto principalmente correzzioni delle fasi precedenti.
Non abbiamo perso tempo, abbiamo lavorato bene. Principalmente abbiamo imparato a usarre pygame anche grazie all'AI che ci ha spiegato come proseguire il progetto. Per la prossima settimana pianifichiamo di finire il progetto quindi di finire le fasi mancanti la 10 e la 11 e di integrare le ultime cose.
Purtroppo la suddivisione è ancora da pianifcare meglio, dato che martedì Alice non c'era allora mi sono occupata io di fare l fase 7 mentre oggi (mercoledì) abbiamo lavorato insieme.

### Settimana 3 (6-12 maggio 2026)

In questa settimana ci siamo concentrate sulla rifinitura del sistema di scoring e sulla gestione del tempo. Abbiamo implementato il timer decrescente in main.py e collegato il feedback visivo (colore verde/rosso) alla risposta dell'utente. Abbiamo affrontato un bug fastidioso: il punteggio aumentava anche tenendo premuto il tasto, quindi abbiamo dovuto modificare l' input_handler.py per leggere solo il singolo evento KEYDOWN invece della pressione continua. Abbiamo anche iniziato a scrivere i primi test per le regole di base.

### Settimana finale (13-17 maggio 2026)

Abbiamo rifinito l'interfaccia utente in ui.py per assicurarci che il feedback visivo (colore rosso/verde per le risposte) fosse immediato e fluido. Abbiamo verificato la riproducibilità delle partite testando diversi seed nel generatore, assicurandoci che il bilanciamento tra risposte "SÌ" e "NO" fosse equo per non favorire l'utente. Infine, abbiamo completato la documentazione tecnica e i diagrammi Mermaid per l'architettura. .

---

## Bilancio finale

Siamo soddisfatte di come il gioco gestisce la fluidità tra i vari stati (Intro, Gioco, Risultati). La cosa più difficile è stata separare la logica pura (il calcolo del risultato) dalla parte grafica di Pygame, ma questo ci ha permesso di scrivere test più facili. Abbiamo capito che lavorare in coppia richiede molta comunicazione, specialmente quando si usa l'IA per generare parti di codice, per evitare che una delle due non capisca cosa faccia una funzione. Se avessimo avuto un'altra settimana, avremmo aggiunto completato tutti gli obiettivi avanzati. Voto onesto: 8/10.

---

