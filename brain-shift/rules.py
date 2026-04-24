def is_even(number: int) -> bool:
    """
    Verifica se un numero è pari.
    Se il resto della divisione per 2 è 0, è pari.
    """
    result = number % 2 == 0
    print(f"Pygame Log: Il numero {number} è pari? {result}")
    return result

def is_vowel(letter: str) -> bool:
    """
    Verifica se una lettera è una vocale.
    Converte la lettera in minuscolo per coprire entrambi i casi (A/a).
    """
    vocali = "aeiou"
    # Gestiamo il caso in cui l'input sia più lungo di un carattere o vuoto
    if len(letter) != 1:
        return False
        
    result = letter.lower() in vocali
    print(f"Pygame Log: La lettera '{letter}' è una vocale? {result}")
    return result

def compute_expected_answer(position: str, letter: str, number: int) -> bool:
    """
    Restituisce il risultato atteso in base alla posizione:
    - 'number' → verifica se il numero è pari
    - 'letter' → verifica se la lettera è una vocale
    """
    if position == "number":
        return is_even(number)
    elif position == "letter":
        return is_vowel(letter)
    else:
        # Caso non valido
        print(f"Pygame Log: Posizione non valida '{position}'")
        return False
    