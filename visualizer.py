import pygame
# from settings import WIN, WIDTH, HEIGHT, BAR_COLOR, BG_COLOR
from settings import WIN, WIDTH, HEIGHT, BAR_GRADIENTS, BG_COLOR

def draw_list(lst, color_positions=None):
    if color_positions is None:
        color_positions = {}

    WIN.fill(BG_COLOR)
    width = WIDTH // len(lst)

    for i, val in enumerate(lst):
        # color = color_positions.get(i, BAR_COLOR)
        color = color_positions.get(i, BAR_GRADIENTS[i % len(BAR_GRADIENTS)])
        pygame.draw.rect(WIN, color, (i * width, HEIGHT - val * 5, width - 2, val * 5))
    pass

def draw_text_info(algorithm_name, settings):
    font = pygame.font.SysFont('consolas', 20)

    title = font.render(algorithm_name, True, (255, 255, 255))
    WIN.blit(title, ((WIDTH - title.get_width()) // 2, 10))

    controls1 = font.render(
        "R - Reset   |   SPACE - Start   |   + / - Speed   |   P - Preview Mode",
        True, (180, 180, 180)
    )
    WIN.blit(controls1, ((WIDTH - controls1.get_width()) // 2, 35))

    controls2 = font.render(
        "B - Bubble   |   I - Insertion   |   S - Selection   |   A - Asc   |   D - Desc",
        True, (180, 180, 180)
    )
    WIN.blit(controls2, ((WIDTH - controls2.get_width()) // 2, 60))
