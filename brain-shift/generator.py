TOP = "letter"
BOTTOM = "number"

@dataclass
class Trial:
    position: str
    letter: str
    number: int
    expected_answer: bool

def generate_trial(rng) -> Trial:
    position = rng.choice([TOP, BOTTOM])
    letter = rng.choice(string.ascii_uppercase)
    number = rng.randint(1, 9)
    expected = compute_expected_answer(position, letter, number)
    return Trial(position, letter, number, expected)
