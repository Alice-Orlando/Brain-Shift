def is_even(number: int) -> bool:
    """Verifica se un numero è pari."""
    return number % 2 == 0


def is_vowel(letter: str) -> bool:
    """Verifica se una lettera è una vocale."""
    if len(letter) != 1:
        return False
    return letter.upper() in "AEIOU"


def compute_expected_answer(position: str, letter: str, number: int) -> bool:
    """
    Calcola la risposta attesa in base alla posizione della carta:
    - TOP  → il numero è pari?
    - BOTTOM → la lettera è una vocale?
    """
    if position == "TOP":
        return is_even(number)
    elif position == "BOTTOM":
        return is_vowel(letter)
    return False