from models import Trial
from rules import compute_expected_answer

VOCALI = "AEIOU"
CONSONANTI = "BCDFGHJKLMNPQRSTVWXYZ"


def generate_trial(rng) -> Trial:
    position = rng.choice(["TOP", "BOTTOM"])
    index = rng.randint(0, 1)
    if index == 0:
        letter = rng.choice(VOCALI)
    else:
        letter = rng.choice(CONSONANTI)
    number = rng.randint(1, 9)
    expected = compute_expected_answer(position, letter, number)
    return Trial(position, letter, number, expected)
