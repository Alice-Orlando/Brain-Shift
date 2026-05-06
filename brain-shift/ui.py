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


# TIMER DI GIOCO
def draw_timer(surface, remaining_time, config):
    font = pygame.font.Font(None, 50)

    timer_string = f"Tempo: {remaining_time}s"
    text = font.render(timer_string, True, (200, 40, 40))

    text_rect = text.get_rect(midtop=(config["screen_width"] // 2, 20))
    surface.blit(text, text_rect)

# SCHERMATA RISULTATI
def draw_results_screen(surface, score, correct_count, wrong_count, accuracy, config):
    title_font = pygame.font.Font(None, 90)
    stat_font = pygame.font.Font(None, 60)

    width = config["screen_width"]
    height = config["screen_height"]

    # sfondo leggermente grigio
    surface.fill((240, 240, 240))

    # titolo
    title = title_font.render("TEMPO SCADUTO", True, (180, 30, 30))
    title_rect = title.get_rect(center=(width // 2, 100))
    surface.blit(title, title_rect)

    # statistiche
    lines = [
        f"Punteggio finale: {score}",
        f"Risposte corrette: {correct_count}",
        f"Risposte sbagliate: {wrong_count}",
        f"Accuratezza: {accuracy}%",
        "Premi R per rigiocare"
    ]

    for i, line in enumerate(lines):
        txt = stat_font.render(line, True, (20, 20, 20))
        txt_rect = txt.get_rect(center=(width // 2, 220 + i * 80))
        surface.blit(txt, txt_rect)