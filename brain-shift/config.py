import pygame

# Dimensioni schermo
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Timing
TOTAL_TIME = 60  # secondi
FEEDBACK_DURATION = 0.15  # secondi
INSTRUCTIONS_HIDE_AFTER = 10  # nasconde istruzioni dopo N corrette

# Colori
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
LIGHT_GRAY = (243, 250, 252)  # Sfondo chiaro
RED = (200, 40, 40)
GREEN = (50, 180, 50)
DARK_RED = (180, 30, 30)
CARD_DEFAULT = (70, 130, 200)
CARD_CORRECT = (100, 200, 100)
CARD_WRONG = (230, 100, 100)
TEXT_COLOR = (255, 255, 255)
TIMER_COLOR = (200, 40, 40)
INSTRUCTION_COLOR = (100, 100, 100)

# Rettangoli delle carte - centrate e ben distanziate
TOP_CARD_RECT = pygame.Rect(250, 60, 300, 130)
BOTTOM_CARD_RECT = pygame.Rect(250, 320, 300, 130)

def get_config():
    return {
        "screen_width": SCREEN_WIDTH,
        "screen_height": SCREEN_HEIGHT,
        "top_card_rect": TOP_CARD_RECT,
        "bottom_card_rect": BOTTOM_CARD_RECT,
        "card_color": CARD_DEFAULT,
        "text_color": TEXT_COLOR,
        "timer_color": TIMER_COLOR,
        "instruction_color": INSTRUCTION_COLOR,
    }