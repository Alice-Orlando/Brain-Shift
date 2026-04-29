import pygame

pygame.init() # Inizializza Pygame 
screen = pygame.display.set_mode((800, 600)) # Crea una finestra di gioco
clock = pygame.time.Clock() # Crea un orologio per gestire il frame rate

running = True
while running: # Loop principale del gioco
    for event in pygame.event.get(): # Gestisce gli eventi
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255)) # Riempie lo schermo di bianco
    pygame.display.flip() # Aggiorna lo schermo
    clock.tick(60) # Limita il frame rate a 60 FPS

