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


# File: ui.py

def draw_instructions(surface, config, correct_count):
    """Disegna le regole con opacità variabile (Fading progressivo)."""
    
    # 1. Calcolo del livello di opacità (Alpha)
    if correct_count <= 3:
        alpha = 255  # 100%
    elif correct_count <= 7:
        alpha = 178  # 70%
    elif correct_count <= 11:
        alpha = 102  # 40%
    else:
        return  # Non disegnare le istruzioni dopo 12 risposte corrette

    font = pygame.font.Font(None, 28)
    # Colore base grigio (100, 100, 100)
    base_color = (100, 100, 100)
    
    # 2. Rendering del testo
    top_text = font.render("Il numero è PARI?", True, base_color)
    bottom_text = font.render("La lettera è una VOCALE?", True, base_color)

    # 3. Applicazione della trasparenza
    # Dobbiamo impostare l'alpha sulla "superficie" del testo appena creata
    top_text.set_alpha(alpha)
    bottom_text.set_alpha(alpha)

    # 4. Disegno a schermo
    width = config["screen_width"]
    top_rect = top_text.get_rect(center=(width // 2, 205))
    bottom_rect = bottom_text.get_rect(center=(width // 2, 295))

    surface.blit(top_text, top_rect)
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


def draw_score(surface, score, multiplier, meter, config):
    """Disegna punteggio, moltiplicatore e i quadratini del meter."""
    font = pygame.font.Font(None, 34)
    
    # 1. Creiamo il testo
    score_txt = f"Score: {score}  |  Mult: x{multiplier}"
    # Usiamo il colore BLACK o un grigio scuro dal tuo config
    text = font.render(score_txt, True, (40, 40, 40)) 
    
    # 2. Posizionamento dinamico a destra
    text_rect = text.get_rect(topright=(config["screen_width"] - 20, 15))
    surface.blit(text, text_rect)
    
    # 3. Disegno dei 4 quadratini del meter sotto il testo
    # Partiamo dalla stessa X del testo per allinearli
    start_x = text_rect.left 
    for i in range(4):
        # Verde se attivo, Grigio chiaro se spento
        color = (50, 180, 50) if i < meter else (210, 210, 210)
        # Disegnamo il rettangolino
        pygame.draw.rect(surface, color, (start_x + (i * 22), 45, 18, 8), border_radius=2)


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