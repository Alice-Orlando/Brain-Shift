# Brain Shift — progetto di gruppo

> Questa è la prima pagina che vede chi apre il vostro repository. Deve essere chiara, pulita, utile. Niente fuffa.

## Chi siamo

- Alice Orlando — alicenontelodico@gmail.com / Alice-Orlando
- Nome Cognome 2 — email / handle GitHub
- (eventuale terzo membro se siete un trio)

Classe 4A Informatica — a.s. 2025-26.

## Cos'è Brain Shift

Brain Shift è un gioco che mette alla prova la capacità di cambiare rapidamente attenzione e criterio di risposta. In ogni turno compare una carta con una lettera e un numero, posizionata in alto oppure in basso sullo schermo. Se la carta è in alto bisogna controllare se il numero è pari, mentre se è in basso bisogna verificare se la lettera è una vocale, rispondendo sempre solo SÌ o NO.

## Come giocare

Istruzioni minime ma complete per far partire il gioco da clone pulito:

```bash
git clone <URL-del-vostro-repo>
cd <nome-cartella>
pip install -r requirements.txt
python main.py
```

Specificate:

- versione Python richiesta (es. Python 3.11+)
- versione pygame richiesta
- altre dipendenze se ce ne sono

## Controlli

- ← freccia sinistra: …
- → freccia destra: …
- … (eventuale mouse, pausa, ecc.)

## Screenshot

Uno o due screenshot del gioco (anche solo immagini PNG nella cartella `docs/img/`). Aiutano molto chi apre il repo. Una GIF animata è ancora meglio.

## Struttura del repository

Breve spiegazione di dove sta cosa:

```
brain_shift/
├── main.py           ← entry point
├── rules.py          ← logica regole
├── scoring.py        ← sistema scoring
├── ...
├── docs/             ← documentazione
└── tests/            ← test pytest
```

## Come lanciare i test

```bash
pytest tests/
```

---

### Domande-guida per questa pagina

Non vanno lasciate nel file finale, servono solo a voi per capire cosa scrivere.

1. Se un vostro compagno di un'altra classe apre questo repo, capisce in 30 secondi cosa fa il gioco?
2. Le istruzioni di setup sono abbastanza specifiche da funzionare sul suo computer?
3. C'è almeno uno screenshot o una GIF?
4. Tutti i link ad altre pagine di `docs/` sono validi?
