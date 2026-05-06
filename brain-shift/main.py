import pygame 
import time 
import scoring
import generator  
import ui

# STATI DEL GIOCO
PLAYING = "PLAYING"
RESULTS = "RESULTS"
state = PLAYING
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Brain Shift")
clock = pygame.time.Clock()


TOTAL_TIME = 60
start_time = None

running = True
while running:  # Loop principale del gioco
    for event in pygame.event.get():  # Gestisce gli eventi
        if event.type == pygame.QUIT:
            running = False

        # EVENTI SOLO DURANTE IL GIOCO
        if state == PLAYING:

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RIGHT:
                    user_answer = True
                    is_correct = (user_answer == trial.expected_answer)

                    # Avvia timer al primo trial
                    if start_time is None:
                        start_time = time.time()

                    # Aggiorna punteggio
                    score = scoring.apply_answer(score, is_correct)

                    # Conta corrette/sbagliate
                    if is_correct:
                        correct_count += 1
                    else:
                        wrong_count += 1

                    # Nuovo trial
                    trial = generator.generate_trial()

                elif event.key == pygame.K_LEFT:
                    user_answer = False
                    is_correct = (user_answer == trial.expected_answer)

                    # Avvia timer al primo trial
                    if start_time is None:
                        start_time = time.time()

                    # Aggiorna punteggio
                    score = scoring.apply_answer(score, is_correct)

                    # Conta corrette/sbagliate
                    if is_correct:
                        correct_count += 1
                    else:
                        wrong_count += 1

                    # Nuovo trial
                    trial = generator.generate_trial()

        # EVENTI SOLO NELLA SCHERMATA RISULTATI
        elif state == RESULTS:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:

                    # RESET COMPLETO
                    score = 0
                    correct_count = 0
                    wrong_count = 0
                    start_time = None

                    trial = generator.generate_trial()
                    state = PLAYING

   
    # DISEGNO SCHERMATA
    screen.fill((255, 255, 255))

    if state == PLAYING:

        # TIMER
        if start_time is not None:
            elapsed = time.time() - start_time
            remaining = max(0, int(TOTAL_TIME - elapsed))

            if elapsed >= TOTAL_TIME:
                state = RESULTS
        else:
            remaining = TOTAL_TIME

        # QUI DISEGNI IL TUO TRIAL NORMALE
        ui.draw_fixation(screen)
        ui.draw_trial(screen, trial)

        # TIMER IN ALTO
        ui.draw_timer(screen, remaining)

    elif state == RESULTS:

        total_answers = correct_count + wrong_count

        if total_answers > 0:
            accuracy = round((correct_count / total_answers) * 100, 1)
        else:
            accuracy = 0

        ui.draw_results_screen(screen, score, correct_count, wrong_count, accuracy)

    pygame.display.flip()
    clock.tick(60)

