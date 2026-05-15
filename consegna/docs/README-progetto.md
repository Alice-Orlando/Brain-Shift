# Brain Shift — progetto di gruppo

> Questa è la prima pagina che vede chi apre il vostro repository. Deve essere chiara, pulita, utile. Niente fuffa.

## Chi siamo

- Alice Orlando — alicenontelodico@gmail.com / Alice-Orlando
- Maggy Bersaglio — bersagliomaggy@gmail.com / maggybersaglio
- (eventuale terzo membro se siete un trio)

Classe 4A Informatica — a.s. 2025-26.

## Cos'è Brain Shift

Brain Shift è un gioco che mette alla prova la capacità di cambiare rapidamente attenzione e criterio di risposta. In ogni turno compare una carta con una lettera e un numero, posizionata in alto oppure in basso sullo schermo. Se la carta è in alto bisogna controllare se il numero è pari, mentre se è in basso bisogna verificare se la lettera è una vocale, rispondendo sempre solo SÌ o NO.

## Come giocare

Istruzioni minime ma complete per far partire il gioco da clone pulito: 

```bash
git clone https://github.com/Alice-Orlando/Brain-Shift.git
cd brain-shift
pip install -r requirements.txt
python main.py
```

Specificate:

- versione Python richiesta 3.13
- versione pygame richiesta 2.6.1

## Controlli

- ← freccia sinistra: NO
- → freccia destra: SI
- tastp R: per ricominciare il gioco
- tasto P: Mette il gioco in PAUSA.
- tasto ESC: Esce dal gioco.

## Screenshot

Uno o due screenshot del gioco (anche solo immagini PNG nella cartella `docs/img/`). Aiutano molto chi apre il repo. Una GIF animata è ancora meglio.

## Struttura del repository

Breve spiegazione di dove sta cosa:

```
brain_shift/
├── main.py           ← entry point
├── config.py         ← configurazione del gioco
├── generator.py      ← generazione delle carte
├── models.py         ← modelli di dati (carte, punteggi)
├── rules.py          ← logica regole
├── scoring.py        ← sistema scoring
├── ui.py             ← interfaccia utente (pygame)
├── README.md         ← documentazione principale
├── requirements.text ← dipendenze Python
├── test/             ← cartella dei test
│   ├── conftest.py   ← configurazione pytest
│   ├── README.md     ← documentazione test
│   ├── test_rules.py ← test per rules.py
│   └── test_scoring_base.py ← test per scoring.py
├── docs/             ← documentazione
└── consegna/         ← consegna progetto
    ├── docs/         ← documentazione dettagliata
    ├── slide/        ← presentazioni
    └── tests/        ← test aggiuntivi
```

## Come lanciare i test

```bash
pytest tests/
```

---

