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
INTRO = "INTRO"
PAUSED = "PAUSED"
PLAYING = "PLAYING"
RESULTS = "RESULTS"


def reset_game():
    """Inizializza / resetta tutte le variabili di gioco."""
    global state, score, correct_count, wrong_count, start_time, multiplier, meter 
    global trial, feedback_until, feedback_color
    global pause_start, total_paused_time


    pause_start = 0
    total_paused_time = 0
    state = INTRO
    multiplier = 1
    meter = 0
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
    # 1. AGGIUNGI multiplier e meter ai global
    global score, multiplier, meter, correct_count, wrong_count, trial, start_time
    global feedback_until, feedback_color

    # Avvia il timer al primo input
    if start_time is None:
        start_time = time.time()

    # 2. CALCOLA se la risposta è corretta
    is_correct = (user_answer_bool == trial.expected_answer)

    # 3. SOSTITUISCI la vecchia riga 'score = scoring.apply_answer(...)' con questa:
    score, multiplier, meter = scoring.apply_answer_advanced(score, multiplier, meter, is_correct)

    # 4. IL RESTO RIMANE UGUALE: gestisci contatori e feedback visivo
    if is_correct:
        correct_count += 1
        feedback_color = config.CARD_CORRECT
    else:
        wrong_count += 1
        # PENALITÀ FADING: se sbaglia, abbassiamo il contatore delle corrette
        # così le istruzioni tornano a vedersi (senza scendere sotto lo zero)
        correct_count = max(0, correct_count - 2)
        feedback_color = config.CARD_WRONG

    # Feedback visivo non bloccante
    feedback_until = time.time() + config.FEEDBACK_DURATION

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
            if event.key == pygame.K_p:
                if state == PLAYING and start_time is not None:
                    state = PAUSED
                    pause_start = time.time() # Inizia a contare il tempo di pausa
                    
        elif state == PAUSED:
            state = PLAYING
            # Calcola quanto è durata questa pausa e aggiungila al totale
            total_paused_time += (time.time() - pause_start)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        if state == INTRO:
            if event.key == pygame.K_SPACE:
                state = PLAYING
                # Il timer partirà comunque al primo tasto freccia grazie alla logica esistente

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
            # Sottraiamo il tempo totale delle pause dal tempo trascorso
            elapsed = (now - start_time) - total_paused_time 
            remaining = max(0, int(config.TOTAL_TIME - elapsed))
            if elapsed >= config.TOTAL_TIME:
                score = scoring.calculate_final_bonus(score, multiplier)
                state = RESULTS
        else:
            remaining = config.TOTAL_TIME

# ── Logica Inter-trial interval ──────────────────────────────────────────
    if state == PLAYING and feedback_until != 0:
        if now >= feedback_until:
            # Il tempo di attesa è finito: generiamo il nuovo trial
            trial = generator.generate_trial(rng)
            feedback_until = 0 # Resetta il timer
            feedback_color = None # Resetta il colore del feedback

    # ── Disegno ───────────────────────────────────────────────────────────────
    ui.draw_background(screen, cfg)

    if state == INTRO:
        ui.draw_intro_screen(screen, cfg)

    if state == PAUSED:
        ui.draw_pause_screen(screen, cfg)

    elif state == PLAYING:
        # Colore carta: durante il feedback usa verde/rosso
        if now < feedback_until and feedback_color is not None:
            card_color = feedback_color
        else:
            card_color = config.CARD_DEFAULT

        ui.draw_card(screen, trial, cfg, color_override=card_color)
        ui.draw_timer(screen, remaining, cfg)
        ui.draw_score(screen, score, multiplier, meter, cfg)
        ui.draw_instructions(screen, cfg, correct_count)
        ui.draw_controls_hint(screen, cfg)

    elif state == RESULTS:
        total_answers = correct_count + wrong_count
        accuracy = round((correct_count / total_answers) * 100, 1) if total_answers > 0 else 0
        ui.draw_results_screen(screen, score, correct_count, wrong_count, accuracy, cfg)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()