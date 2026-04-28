from dataclasses import dataclass

def is_even(n: int) -> bool:
    return n % 2 == 0

def is_vowel(c: str) -> bool:
    return c.upper() in "AEIOU"

@dataclass
class Trial:
    position: str  # "TOP" o "BOTTOM"
    letter: str
    number: int
    expected_answer: bool = False
    user_answer: bool | None = None
    is_correct: bool = False

    def __post_init__(self):
        if self.position == "TOP":
            self.expected_answer = is_even(self.number)
        elif self.position == "BOTTOM":
            self.expected_answer = is_vowel(self.letter)
        else:
            raise ValueError(f"Invalid position: {self.position}")

    def evaluate(self):
        if self.user_answer is None:
            self.is_correct = False
        else:
            self.is_correct = (self.user_answer == self.expected_answer)