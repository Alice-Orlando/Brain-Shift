import pygame
import time
import random

import config
import scoring
import generator
import ui

# ── Init pygame ──────────────────────────────────────────────────────────────
pygame.init()
screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
pygame.display.set_caption("Brain Shift")
clock = pygame.time.Clock()
cfg = config.get_config()

# ── RNG con seed riproducibile ────────────────────────────────────────────────
rng = random.Random(42)

# ── Costanti stati ────────────────────────────────────────────────────────────
PLAYING = "PLAYING"
RESULTS = "RESULTS"


def reset_game():
    """Inizializza / resetta tutte le variabili di gioco."""
    global state, score, correct_count, wrong_count, start_time
    global trial, feedback_until, feedback_color

    state = PLAYING
    score = 0
    correct_count = 0
    wrong_count = 0
    start_time = None          # il timer parte al primo tasto premuto
    feedback_until = 0.0       # timestamp fino a cui mostrare il feedback
    feedback_color = None      # colore feedback (verde/rosso) o None

    # Genera il primo trial
    trial = generator.generate_trial(rng)


def handle_answer(user_answer_bool):
    """Gestisce la risposta del giocatore e aggiorna lo stato."""
    global score, correct_count, wrong_count, trial, start_time
    global feedback_until, feedback_color

    # Avvia il timer al primo input
    if start_time is None:
        start_time = time.time()

    is_correct = (user_answer_bool == trial.expected_answer)
    score = scoring.apply_answer(score, is_correct)

    if is_correct:
        correct_count += 1
        feedback_color = config.CARD_CORRECT
    else:
        wrong_count += 1
        feedback_color = config.CARD_WRONG

    # Feedback visivo non bloccante: dura 150 ms
    feedback_until = time.time() + config.FEEDBACK_DURATION

    # Genera subito il prossimo trial (compare dopo il feedback)
    trial = generator.generate_trial(rng)


# ── Setup iniziale ────────────────────────────────────────────────────────────
reset_game()

# ── Main loop ─────────────────────────────────────────────────────────────────
running = True
while running:

    now = time.time()

    # ── Gestione eventi ───────────────────────────────────────────────────────
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            # Input durante il gioco
            if state == PLAYING:
                if event.key == pygame.K_RIGHT:
                    handle_answer(True)
                elif event.key == pygame.K_LEFT:
                    handle_answer(False)

            # Input nella schermata risultati
            elif state == RESULTS:
                if event.key == pygame.K_r:
                    reset_game()

    # ── Logica timer ──────────────────────────────────────────────────────────
    if state == PLAYING:
        if start_time is not None:
            elapsed = now - start_time
            remaining = max(0, int(config.TOTAL_TIME - elapsed))
            if elapsed >= config.TOTAL_TIME:
                state = RESULTS
        else:
            remaining = config.TOTAL_TIME

    # ── Disegno ───────────────────────────────────────────────────────────────
    ui.draw_background(screen, cfg)

    if state == PLAYING:
        # Colore carta: durante il feedback usa verde/rosso
        if now < feedback_until and feedback_color is not None:
            card_color = feedback_color
        else:
            card_color = config.CARD_DEFAULT

        ui.draw_card(screen, trial, cfg, color_override=card_color)
        ui.draw_timer(screen, remaining, cfg)
        ui.draw_score(screen, score, cfg)
        ui.draw_instructions(screen, cfg, correct_count, config.INSTRUCTIONS_HIDE_AFTER)
        ui.draw_controls_hint(screen, cfg)

    elif state == RESULTS:
        total_answers = correct_count + wrong_count
        accuracy = round((correct_count / total_answers) * 100, 1) if total_answers > 0 else 0
        ui.draw_results_screen(screen, score, correct_count, wrong_count, accuracy, cfg)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()