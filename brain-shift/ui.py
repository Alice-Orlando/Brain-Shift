import pygame
from models import Trial


def draw_card(surface, trial: Trial, config, color_override=None):
    """Disegna la carta con il numero e la lettera."""
    font = pygame.font.Font(None, 72)

    if trial.position == "TOP":
        card_rect = config["top_card_rect"]
    else:
        card_rect = config["bottom_card_rect"]

    color = color_override if color_override else config["card_color"]
    pygame.draw.rect(surface, color, card_rect, border_radius=12)

    string = f"{trial.letter} {trial.number}"
    text = font.render(string, True, config["text_color"])
    text_rect = text.get_rect(center=card_rect.center)
    surface.blit(text, text_rect)


def draw_timer(surface, remaining_time, config):
    """Disegna il timer in alto al centro."""
    font = pygame.font.Font(None, 40)
    timer_string = f"Tempo: {remaining_time}s"
    text = font.render(timer_string, True, config["timer_color"])
    text_rect = text.get_rect(center=(config["screen_width"] // 2, 20))
    surface.blit(text, text_rect)


def draw_instructions(surface, config, correct_count, hide_after=10):
    """Mostra le due regole sullo schermo. Scompare dopo hide_after corrette."""
    if correct_count >= hide_after:
        return

    font = pygame.font.Font(None, 28)
    color = (100, 100, 100)
    width = config["screen_width"]

    # Regola TOP: sotto la carta TOP
    top_text = font.render("Il numero è PARI?", True, color)
    top_rect = top_text.get_rect(center=(width // 2, 205))
    surface.blit(top_text, top_rect)

    # Regola BOTTOM: sopra la carta BOTTOM
    bottom_text = font.render("La lettera è una VOCALE?", True, color)
    bottom_rect = bottom_text.get_rect(center=(width // 2, 295))
    surface.blit(bottom_text, bottom_rect)


def draw_controls_hint(surface, config):
    """Mostra i pulsanti NO e SI in basso con colori."""
    font_button = pygame.font.Font(None, 36)
    width = config["screen_width"]
    height = config["screen_height"]

    # Pulsante NO (sinistra) - rosso
    no_rect = pygame.Rect(width // 4 - 65, 475, 130, 55)
    pygame.draw.rect(surface, (255, 195, 195), no_rect, border_radius=8)
    pygame.draw.rect(surface, (200, 50, 50), no_rect, 3, border_radius=8)
    no_text = font_button.render("NO", True, (200, 50, 50))
    no_text_rect = no_text.get_rect(center=no_rect.center)
    surface.blit(no_text, no_text_rect)

    # Pulsante SI (destra) - verde
    si_rect = pygame.Rect(3 * width // 4 - 65, 475, 130, 55)
    pygame.draw.rect(surface, (178, 242, 187), si_rect, border_radius=8)
    pygame.draw.rect(surface, (50, 150, 80), si_rect, 3, border_radius=8)
    si_text = font_button.render("SI", True, (50, 150, 80))
    si_text_rect = si_text.get_rect(center=si_rect.center)
    surface.blit(si_text, si_text_rect)


def draw_score(surface, score, config):
    """Disegna il punteggio in alto a destra."""
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, (30, 30, 30))
    text_rect = text.get_rect(topright=(config["screen_width"] - 20, 18))
    surface.blit(text, text_rect)


def draw_background(surface, config):
    """Disegna lo sfondo chiaro."""
    surface.fill((243, 250, 252))


def draw_results_screen(surface, score, correct_count, wrong_count, accuracy, config):
    """Disegna la schermata dei risultati finali."""
    title_font = pygame.font.Font(None, 90)
    stat_font = pygame.font.Font(None, 50)
    hint_font = pygame.font.Font(None, 36)

    width = config["screen_width"]

    # Sfondo
    surface.fill((243, 250, 252))

    # Titolo
    title = title_font.render("TEMPO SCADUTO!", True, (220, 40, 40))
    title_rect = title.get_rect(center=(width // 2, 60))
    surface.blit(title, title_rect)

    # Riga divisoria
    pygame.draw.line(surface, (150, 150, 150), (50, 140), (width - 50, 140), 2)

    # Statistiche
    lines = [
        f"Punteggio: {score}",
        f"Corrette: {correct_count}",
        f"Sbagliate: {wrong_count}",
        f"Accuratezza: {accuracy}%",
    ]

    y_offset = 200
    for line in lines:
        txt = stat_font.render(line, True, (30, 30, 30))
        txt_rect = txt.get_rect(center=(width // 2, y_offset))
        surface.blit(txt, txt_rect)
        y_offset += 70

    # Hint per rigiocare
    hint = hint_font.render("Premi R per rigiocare", True, (100, 100, 100))
    hint_rect = hint.get_rect(center=(width // 2, config["screen_height"] - 40))
    surface.blit(hint, hint_rect)