# Architettura

> Qui spiegate **come è fatto dentro** il progetto. Non ripetete il testo della specifica: scrivete cosa avete fatto voi, come lo avete organizzato, e perché.

## Decomposizione in moduli

Per ciascun modulo del vostro progetto, una-due righe:

- `main.py` — Il main è il ciclo principale del gioco, gestiamo gli input dell'utente e il tempo di gioco.
- `config.py` — Ha tutte le costanti
- `models.py` — Trial Rappresenta un singolo turno di gioco: abbiamo usato una dataclass per tenere insieme input, risposta attesa e risultato, calcolando automaticamente expected_answer in __post_init__.
- `rules.py` — Gestisce la logica di base del gioco: abbiamo separato le regole in funzioni semplici e riutilizzabili (is_even e is_vowel) per controllare numeri e lettere.
- `scoring.py` — Aumenta o diminuisce il punteggio
- `generator.py` —  Genera un trial usando un generatore casuale con seed per garantire partite riproducibili; separa la creazione dei dati dalla logica delegando il calcolo della risposta a compute_expected_answer.
- `states.py` — Non presente come file separato: abbiamo usato una classe GameState (ereditata da Enum) direttamente dentro main.py per gestire i passaggi tra i vari menu.
- `ui.py` — Disegna gli assets grafici.
- `input_handler.py` — Non presente come file separato: la gestione degli input è integrata nel metodo handle_input della classe Game in main.py, dove traduciamo i tasti K_LEFT e K_RIGHT in risposte False e True.


## Separazione logica / presentazione
Quali moduli sono "puri" (non importano pygame)? Quali sono legati al rendering? Come comunicano fra loro?

Se avete fatto scelte non ovvie (es. passare lo stato come parametro invece che come variabile globale), spiegate il ragionamento.

## Macchina a stati
Il gioco ruota attorno a quattro stati principali gestiti nel ciclo run() di main.py:

INTRO: Schermata iniziale. Aspetta la pressione di un tasto per iniziare.
PLAYING: Il cuore del gioco. Mostra la carta, gestisce il timer decrescente e controlla la logica di risposta.
PAUSED: Blocca il tempo e l'input di gioco, mostrando un overlay di pausa.
RESULTS: Mostra il punteggio finale e le statistiche della sessione. Permette di ricominciare (R) o uscire (ESC).

## Flusso di un trial
sequenceDiagram
    participant G as Generator
    participant M as Main (Game Loop)
    participant R as Rules
    participant S as Scoring

    M->>G: generate_trial()
    G-->>M: Restituisce oggetto Trial
    M->>M: Visualizza carta (UI)
    M->>M: Attesa Input Utente
    M->>R: compute_expected_answer(trial)
    R-->>M: Risposta corretta (Bool)
    M->>S: update_score(is_correct, response_time)
    S-->>M: Nuovo punteggio e feedback

Il trial nasce in generator.py. In main.py, l'oggetto Trial viene mostrato a video. Quando l'utente preme una freccia, il sistema chiama rules.py per calcolare la risposta corretta "al volo" e confrontarla con l'input. Il risultato viene passato a scoring.py che aggiorna il moltiplicatore e il punteggio totale.

## Dati principali
Trial (models.py): Una dataclass che contiene la lettera, il numero e la posizione (TOP/BOTTOM). Calcola automaticamente la risposta attesa nel metodo __post_init__.

ScoringState (scoring.py): Mantiene lo stato del punteggio, del moltiplicatore e del "meter" (la barra che carica i bonus).

SessionStats (models.py): Registra il numero di risposte corrette, errate e il tempo medio di reazione per la schermata finale.

## Scoring: come è implementato
Il fading è gestito tramite la variabile consecutive_correct in ScoringState. In ui.py, la funzione di rendering calcola l'opacità del testo delle istruzioni: finché l'utente non indovina 5 risposte di fila, le istruzioni sono visibili. Superata questa soglia, l'opacità diminuisce linearmente fino a rendere il testo invisibile, forzando il giocatore a memorizzare le regole.

