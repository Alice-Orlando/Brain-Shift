import pygame

pygame.init() # Inizializza Pygame 
screen = pygame.display.set_mode((800, 600)) # Crea una finestra di gioco
clock = pygame.time.Clock() # Crea un orologio per gestire il frame rate

score = 0
correct_count = 0
wrong_count = 0

running = True
while running: # Loop principale del gioco
    for event in pygame.event.get(): # Gestisce gli eventi
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                user_answer = True
                is_correct = (user_answer == trial.expected_answer)

                # Aggiorna il punteggio usando la funzione definita
                score = apply_answer(score, is_correct)

                # Incrementa il contatore delle risposte corrette o sbagliate
                if is_correct:
                    correct_count += 1  # risposta giusta
                else:
                    wrong_count += 1    # risposta sbagliata

                # Genera un nuovo trial dopo la risposta
                trial = generate_trial()

            elif event.key == pygame.K_LEFT:
                user_answer = False
                is_correct = (user_answer == trial.expected_answer)

                # Aggiorna il punteggio usando la funzione definita
                score = apply_answer(score, is_correct)

                # Incrementa il contatore delle risposte corrette o sbagliate
                if is_correct:
                    correct_count += 1  # risposta giusta
                else:
                    wrong_count += 1    # risposta sbagliata

                # Genera un nuovo trial dopo la risposta
                trial = generate_trial()

    screen.fill((255, 255, 255)) # Riempie lo schermo di bianco
    pygame.display.flip() # Aggiorna lo schermo
    clock.tick(60) # Limita il frame rate a 60 FPS

