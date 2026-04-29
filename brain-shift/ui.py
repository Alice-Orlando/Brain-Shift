import pygame
from models import Trial 

def draw_card(surface, trial: Trial, config):
    font = pygame.font.Font(None, 74)

    # --- posizione della card ---
    if trial.position == "TOP":
        card_rect = config["top_card_rect"]
    else:
        card_rect = config["bottom_card_rect"]

    # --- disegna carta ---
    pygame.draw.rect(surface, config["card_color"], card_rect, border_radius=12)

    # --- testo dentro la carta ---
    string = f"{trial.letter} {trial.number}"
    text = font.render(string, True, config["text_color"])
    text_rect = text.get_rect(center=card_rect.center)
    surface.blit(text, text_rect)