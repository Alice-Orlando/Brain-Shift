# File: scoring.py

def apply_answer_advanced(score, multiplier, meter, is_correct):
    """
    Gestisce lo scoring avanzato:
    Ogni corretta: score += 50 * multiplier, meter +1. Se meter==4 -> mult+1, meter=0.
    Ogni errata: se meter>0 -> meter=0, altrimenti mult-1.
    """
    if is_correct:
        score += 50 * multiplier
        meter += 1
        if meter == 4:
            multiplier = min(multiplier + 1, 10)
            meter = 0
    else:
        if meter > 0:
            meter = 0
        else:
            multiplier = max(multiplier - 1, 1)
            
    return score, multiplier, meter

def calculate_final_bonus(score, multiplier):
    """Aggiunge il bonus finale a fine partita."""
    return score + (250 * multiplier)