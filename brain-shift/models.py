from dataclasses import dataclass

@dataclass
class Trial:
    position: str  # "TOP" o "BOTTOM"
    letter: str
    number: int
    expected_answer: bool = False
    user_answer: bool | None = None
    is_correct: bool = False

