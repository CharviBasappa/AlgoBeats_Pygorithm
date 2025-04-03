import pygame
from settings import WIN, WIDTH, HEIGHT, CURRENT_THEME

def draw_list(lst, color_positions=None):
    from settings import CURRENT_THEME

    if color_positions is None:
        color_positions = {}

    WIN.fill(CURRENT_THEME["BACKGROUND_COLOR"])
    width = WIDTH // len(lst)
    gradients = CURRENT_THEME["BAR_GRADIENTS"]

    for i, val in enumerate(lst):
        color = color_positions.get(i, gradients[i % len(gradients)])
        pygame.draw.rect(WIN, color, (i * width, HEIGHT - val * 5, width - 2, val * 5))


def draw_text_info(algorithm_name, settings):
    font = pygame.font.SysFont('consolas', 20)

    title = font.render(algorithm_name, True, (255, 255, 255))
    WIN.blit(title, ((WIDTH - title.get_width()) // 2, 10))

    controls1 = font.render(
        "R - Reset | A - Asc | D - Desc | SPACE - Start | T - Theme | + / - Speed ",
        True, (180, 180, 180)
    )
    WIN.blit(controls1, ((WIDTH - controls1.get_width()) // 2, 35))

    controls2 = font.render(
        "I - Insertion | B - Bubble | S - Selection | Q - Quick | M - Merge | H - Heap",
        True, (180, 180, 180)
    )
    WIN.blit(controls2, ((WIDTH - controls2.get_width()) // 2, 60))
