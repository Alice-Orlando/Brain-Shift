"""
Test completi per il progetto Brain Shift.

Copertura:
  - rules.py      → is_even, is_vowel, compute_expected_answer
  - scoring.py    → apply_answer (base), apply_answer_advanced, calculate_final_bonus
  - models.py     → dataclass Trial
  - generator.py  → generate_trial

Come eseguire:
  pip install pytest
  pytest test_brain_shift.py -v
"""

import random
import sys
from pathlib import Path

# Aggiunge la radice del progetto al path così gli import funzionano
ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import pytest

# Import protetti: i test di struttura spiegano cosa manca se fallisce
try:
    from rules import is_even, is_vowel, compute_expected_answer
except ImportError:
    is_even = is_vowel = compute_expected_answer = None

try:
    from scoring import apply_answer
except ImportError:
    apply_answer = None

try:
    from scoring import apply_answer_advanced, calculate_final_bonus
except ImportError:
    apply_answer_advanced = calculate_final_bonus = None

try:
    from models import Trial
except ImportError:
    Trial = None

try:
    from generator import generate_trial
except ImportError:
    generate_trial = None


# ═══════════════════════════════════════════════════════════════════
# RULES.PY
# ═══════════════════════════════════════════════════════════════════

class TestRulesStructure:
    def test_is_even_exists(self):
        assert is_even is not None, "Manca 'is_even' in rules.py"

    def test_is_vowel_exists(self):
        assert is_vowel is not None, "Manca 'is_vowel' in rules.py"

    def test_compute_expected_answer_exists(self):
        assert compute_expected_answer is not None, "Manca 'compute_expected_answer' in rules.py"


class TestIsEven:
    def test_even_number_returns_true(self):
        assert is_even(4) is True

    def test_odd_number_returns_false(self):
        assert is_even(3) is False

    def test_one_is_odd(self):
        assert is_even(1) is False

    def test_two_is_even(self):
        assert is_even(2) is True

    def test_nine_is_odd(self):
        assert is_even(9) is False

    def test_eight_is_even(self):
        assert is_even(8) is True

    def test_returns_bool(self):
        assert isinstance(is_even(4), bool)
        assert isinstance(is_even(3), bool)

    def test_all_even_numbers_1_to_9(self):
        for n in [2, 4, 6, 8]:
            assert is_even(n) is True, f"is_even({n}) dovrebbe essere True"

    def test_all_odd_numbers_1_to_9(self):
        for n in [1, 3, 5, 7, 9]:
            assert is_even(n) is False, f"is_even({n}) dovrebbe essere False"


class TestIsVowel:
    def test_A_is_vowel(self):
        assert is_vowel("A") is True

    def test_E_is_vowel(self):
        assert is_vowel("E") is True

    def test_I_is_vowel(self):
        assert is_vowel("I") is True

    def test_O_is_vowel(self):
        assert is_vowel("O") is True

    def test_U_is_vowel(self):
        assert is_vowel("U") is True

    def test_all_vowels(self):
        for v in "AEIOU":
            assert is_vowel(v) is True, f"is_vowel('{v}') dovrebbe essere True"

    def test_B_is_consonant(self):
        assert is_vowel("B") is False

    def test_Z_is_consonant(self):
        assert is_vowel("Z") is False

    def test_all_consonants(self):
        for c in "BCDFGHJKLMNPQRSTVWXYZ":
            assert is_vowel(c) is False, f"is_vowel('{c}') dovrebbe essere False"

    def test_returns_bool(self):
        assert isinstance(is_vowel("A"), bool)
        assert isinstance(is_vowel("B"), bool)


class TestComputeExpectedAnswer:
    def test_top_even_number_is_true(self):
        assert compute_expected_answer("TOP", "B", 4) is True

    def test_top_odd_number_is_false(self):
        assert compute_expected_answer("TOP", "A", 3) is False

    def test_bottom_vowel_is_true(self):
        assert compute_expected_answer("BOTTOM", "E", 7) is True

    def test_bottom_consonant_is_false(self):
        assert compute_expected_answer("BOTTOM", "K", 2) is False

    def test_top_ignores_letter_vowel(self):
        # A è vocale ma TOP conta solo il numero (3 dispari → False)
        assert compute_expected_answer("TOP", "A", 3) is False

    def test_top_ignores_letter_consonant(self):
        # Z è consonante ma TOP conta solo il numero (6 pari → True)
        assert compute_expected_answer("TOP", "Z", 6) is True

    def test_bottom_ignores_number_even(self):
        # Numero pari ma BOTTOM conta solo la lettera (B consonante → False)
        assert compute_expected_answer("BOTTOM", "B", 4) is False

    def test_bottom_ignores_number_odd(self):
        # Numero dispari ma BOTTOM conta solo la lettera (I vocale → True)
        assert compute_expected_answer("BOTTOM", "I", 7) is True

    def test_returns_bool(self):
        assert isinstance(compute_expected_answer("TOP", "A", 4), bool)
        assert isinstance(compute_expected_answer("BOTTOM", "B", 3), bool)


# ═══════════════════════════════════════════════════════════════════
# SCORING.PY — versione base lineare
# ═══════════════════════════════════════════════════════════════════

class TestApplyAnswerStructure:
    def test_apply_answer_exists(self):
        assert apply_answer is not None, (
            "Manca 'apply_answer' in scoring.py. "
            "La firma attesa è: def apply_answer(score: int, is_correct: bool) -> int"
        )


class TestApplyAnswerBase:
    def test_correct_adds_10_from_zero(self):
        assert apply_answer(0, True) == 10

    def test_correct_adds_10_from_50(self):
        assert apply_answer(50, True) == 60

    def test_correct_adds_10_from_123(self):
        assert apply_answer(123, True) == 133

    def test_wrong_does_not_increase_score(self):
        assert apply_answer(100, False) <= 100
        assert apply_answer(0, False) <= 0
        assert apply_answer(50, False) <= 50

    def test_wrong_policy_is_consistent(self):
        delta_1 = 50 - apply_answer(50, False)
        delta_2 = 200 - apply_answer(200, False)
        assert delta_1 == delta_2, (
            f"Policy incoerente: da 50 tolti {delta_1}, da 200 tolti {delta_2}."
        )

    def test_correct_from_negative_score(self):
        assert apply_answer(-5, True) == 5

    def test_is_pure(self):
        assert apply_answer(100, True) == apply_answer(100, True)
        assert apply_answer(100, False) == apply_answer(100, False)

    def test_five_corrects_from_zero_give_50(self):
        score = 0
        for _ in range(5):
            score = apply_answer(score, True)
        assert score == 50, (
            f"5 corrette da 0 dovrebbero dare 50, ottenuto {score}. "
            "La versione base NON ha moltiplicatore."
        )

    def test_returns_int(self):
        assert isinstance(apply_answer(10, True), int)
        assert isinstance(apply_answer(10, False), int)


# ═══════════════════════════════════════════════════════════════════
# SCORING.PY — versione avanzata con meter e moltiplicatore
# ═══════════════════════════════════════════════════════════════════

class TestApplyAnswerAdvancedStructure:
    def test_apply_answer_advanced_exists(self):
        assert apply_answer_advanced is not None, "Manca 'apply_answer_advanced' in scoring.py"

    def test_calculate_final_bonus_exists(self):
        assert calculate_final_bonus is not None, "Manca 'calculate_final_bonus' in scoring.py"


class TestApplyAnswerAdvanced:
    def test_correct_adds_50_times_multiplier_1(self):
        score, mult, meter = apply_answer_advanced(0, 1, 0, True)
        assert score == 50

    def test_correct_adds_100_with_multiplier_2(self):
        score, mult, meter = apply_answer_advanced(0, 2, 0, True)
        assert score == 100

    def test_correct_increments_meter(self):
        _, _, meter = apply_answer_advanced(0, 1, 0, True)
        assert meter == 1

    def test_multiplier_unchanged_before_4_corrects(self):
        score, mult, meter = 0, 1, 0
        for _ in range(3):
            score, mult, meter = apply_answer_advanced(score, mult, meter, True)
        assert mult == 1
        assert meter == 3

    def test_level_up_after_4_corrects(self):
        score, mult, meter = 0, 1, 0
        for _ in range(4):
            score, mult, meter = apply_answer_advanced(score, mult, meter, True)
        assert mult == 2

    def test_meter_resets_on_level_up(self):
        score, mult, meter = 0, 1, 0
        for _ in range(4):
            score, mult, meter = apply_answer_advanced(score, mult, meter, True)
        assert meter == 0

    def test_score_after_4_corrects_mult1(self):
        # 4 × 50 = 200
        score, mult, meter = 0, 1, 0
        for _ in range(4):
            score, mult, meter = apply_answer_advanced(score, mult, meter, True)
        assert score == 200

    def test_fifth_correct_uses_new_multiplier(self):
        # 4×50 + 1×100 = 300
        score, mult, meter = 0, 1, 0
        for _ in range(5):
            score, mult, meter = apply_answer_advanced(score, mult, meter, True)
        assert score == 300

    def test_multiplier_caps_at_10(self):
        score, mult, meter = 0, 10, 0
        for _ in range(4):
            score, mult, meter = apply_answer_advanced(score, mult, meter, True)
        assert mult == 10

    def test_multiplier_does_not_exceed_10_from_9(self):
        score, mult, meter = 0, 9, 0
        for _ in range(4):
            score, mult, meter = apply_answer_advanced(score, mult, meter, True)
        assert mult == 10

    def test_wrong_resets_meter_if_positive(self):
        score, mult, meter = apply_answer_advanced(0, 1, 3, False)
        assert meter == 0
        assert mult == 1  # moltiplicatore invariato

    def test_wrong_decrements_multiplier_if_meter_zero(self):
        score, mult, meter = apply_answer_advanced(0, 3, 0, False)
        assert mult == 2

    def test_multiplier_floor_at_1(self):
        score, mult, meter = apply_answer_advanced(0, 1, 0, False)
        assert mult == 1

    def test_wrong_does_not_change_score(self):
        new_score, _, _ = apply_answer_advanced(150, 2, 1, False)
        assert new_score == 150

    def test_two_consecutive_wrongs(self):
        # Prima errata (meter=2): azzera meter, mult invariato
        score, mult, meter = apply_answer_advanced(0, 3, 2, False)
        assert meter == 0 and mult == 3
        # Seconda errata (meter=0): decrementa mult
        score, mult, meter = apply_answer_advanced(score, mult, meter, False)
        assert mult == 2

    def test_scenario_from_spec(self):
        """
        Riproduce la tabella della consegna:
        C C C C C E → score=300, mult=2, meter=0
        """
        score, mult, meter = 0, 1, 0
        esiti = [True, True, True, True, True, False]
        snapshots = []
        for e in esiti:
            score, mult, meter = apply_answer_advanced(score, mult, meter, e)
            snapshots.append((score, mult, meter))

        assert snapshots[3] == (200, 2, 0), f"Dopo 4 corrette: {snapshots[3]}"
        assert snapshots[4] == (300, 2, 1), f"Dopo 5ª corretta: {snapshots[4]}"
        assert snapshots[5] == (300, 2, 0), f"Dopo errata con meter>0: {snapshots[5]}"

    def test_is_pure(self):
        r1 = apply_answer_advanced(100, 3, 2, True)
        r2 = apply_answer_advanced(100, 3, 2, True)
        assert r1 == r2


class TestCalculateFinalBonus:
    def test_bonus_is_250_times_multiplier(self):
        assert calculate_final_bonus(0, 1) == 250
        assert calculate_final_bonus(0, 2) == 500

    def test_bonus_added_to_existing_score(self):
        assert calculate_final_bonus(300, 3) == 300 + 750

    def test_bonus_is_pure(self):
        assert calculate_final_bonus(100, 5) == calculate_final_bonus(100, 5)


# ═══════════════════════════════════════════════════════════════════
# MODELS.PY — dataclass Trial
# ═══════════════════════════════════════════════════════════════════

class TestTrialStructure:
    def test_trial_exists(self):
        assert Trial is not None, "Manca la classe 'Trial' in models.py"


class TestTrialCreation:
    def test_creation_with_required_fields(self):
        t = Trial(position="TOP", letter="A", number=4, expected_answer=True)
        assert t.position == "TOP"
        assert t.letter == "A"
        assert t.number == 4
        assert t.expected_answer is True

    def test_user_answer_default_is_none(self):
        t = Trial(position="TOP", letter="B", number=3, expected_answer=False)
        assert t.user_answer is None

    def test_is_correct_default_is_false(self):
        t = Trial(position="BOTTOM", letter="E", number=7, expected_answer=True)
        assert t.is_correct is False

    def test_user_answer_settable(self):
        t = Trial(position="TOP", letter="C", number=2, expected_answer=True)
        t.user_answer = True
        assert t.user_answer is True
        t.user_answer = False
        assert t.user_answer is False

    def test_is_correct_settable(self):
        t = Trial(position="TOP", letter="D", number=5, expected_answer=False)
        t.is_correct = True
        assert t.is_correct is True


class TestTrialEquality:
    def test_equal_trials(self):
        t1 = Trial("TOP", "A", 4, True)
        t2 = Trial("TOP", "A", 4, True)
        assert t1 == t2

    def test_different_position(self):
        assert Trial("TOP", "A", 4, True) != Trial("BOTTOM", "A", 4, True)

    def test_different_letter(self):
        assert Trial("TOP", "A", 4, True) != Trial("TOP", "B", 4, True)

    def test_different_number(self):
        assert Trial("TOP", "A", 4, True) != Trial("TOP", "A", 5, True)

    def test_different_expected_answer(self):
        assert Trial("TOP", "A", 4, True) != Trial("TOP", "A", 4, False)


class TestTrialRepr:
    def test_repr_contains_position(self):
        t = Trial("TOP", "A", 4, True)
        assert "TOP" in repr(t)

    def test_repr_contains_letter(self):
        t = Trial("BOTTOM", "E", 7, True)
        assert "E" in repr(t)


# ═══════════════════════════════════════════════════════════════════
# GENERATOR.PY — generate_trial
# ═══════════════════════════════════════════════════════════════════

class TestGeneratorStructure:
    def test_generate_trial_exists(self):
        assert generate_trial is not None, "Manca 'generate_trial' in generator.py"


class TestGeneratorOutput:
    def test_returns_trial_instance(self):
        rng = random.Random(42)
        trial = generate_trial(rng)
        assert isinstance(trial, Trial), (
            f"generate_trial deve restituire un Trial, non {type(trial).__name__}"
        )

    def test_position_is_top_or_bottom(self):
        rng = random.Random(0)
        for _ in range(50):
            trial = generate_trial(rng)
            assert trial.position in ("TOP", "BOTTOM")

    def test_letter_is_single_uppercase(self):
        rng = random.Random(7)
        for _ in range(50):
            trial = generate_trial(rng)
            assert len(trial.letter) == 1
            assert trial.letter.isupper() and trial.letter.isalpha()

    def test_number_in_range_1_to_9(self):
        rng = random.Random(13)
        for _ in range(100):
            trial = generate_trial(rng)
            assert isinstance(trial.number, int)
            assert 1 <= trial.number <= 9

    def test_expected_answer_is_bool(self):
        rng = random.Random(99)
        for _ in range(20):
            trial = generate_trial(rng)
            assert isinstance(trial.expected_answer, bool)

    def test_expected_answer_consistent_with_rules(self):
        rng = random.Random(42)
        for _ in range(100):
            trial = generate_trial(rng)
            expected = compute_expected_answer(trial.position, trial.letter, trial.number)
            assert trial.expected_answer == expected, (
                f"Trial({trial.position}, {trial.letter}, {trial.number}): "
                f"expected_answer={trial.expected_answer} ma le regole danno {expected}"
            )


class TestGeneratorDeterminism:
    def test_same_seed_same_sequence(self):
        rng_a = random.Random(42)
        rng_b = random.Random(42)
        for _ in range(20):
            a = generate_trial(rng_a)
            b = generate_trial(rng_b)
            assert a.position == b.position
            assert a.letter == b.letter
            assert a.number == b.number
            assert a.expected_answer == b.expected_answer

    def test_different_seeds_different_sequences(self):
        rng_a = random.Random(1)
        rng_b = random.Random(999)
        trials_a = [generate_trial(rng_a) for _ in range(20)]
        trials_b = [generate_trial(rng_b) for _ in range(20)]
        all_equal = all(
            a.position == b.position and a.letter == b.letter and a.number == b.number
            for a, b in zip(trials_a, trials_b)
        )
        assert not all_equal, "Seed diversi hanno prodotto sequenze identiche."

    def test_reproducibility_after_n_calls(self):
        N = 10
        rng1 = random.Random(7)
        for _ in range(N):
            generate_trial(rng1)
        after_n_1 = generate_trial(rng1)

        rng2 = random.Random(7)
        for _ in range(N):
            generate_trial(rng2)
        after_n_2 = generate_trial(rng2)

        assert after_n_1.position == after_n_2.position
        assert after_n_1.letter == after_n_2.letter
        assert after_n_1.number == after_n_2.number


class TestGeneratorDistribution:
    def test_both_positions_appear(self):
        rng = random.Random(5)
        trials = [generate_trial(rng) for _ in range(200)]
        positions = {t.position for t in trials}
        assert "TOP" in positions
        assert "BOTTOM" in positions

    def test_both_answer_values_appear(self):
        rng = random.Random(3)
        trials = [generate_trial(rng) for _ in range(200)]
        answers = {t.expected_answer for t in trials}
        assert True in answers
        assert False in answers