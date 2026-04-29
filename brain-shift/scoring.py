def apply_answer(score: int, is_correct: bool) -> int:

    if is_correct:
        score += 10
    elif score - 5 < 0:
        score == 0
    else:
        score -= 5

    return score