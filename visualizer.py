# from settings import WIN, WIDTH, HEIGHT, BAR_COLOR, BG_COLOR
# import pygame

# def draw_list(lst, color_positions=None):
#     if color_positions is None:
#         color_positions = {}

#     WIN.fill(BG_COLOR)
#     width = WIDTH // len(lst)

#     for i, val in enumerate(lst):
#         color = color_positions.get(i, BAR_COLOR)
#         pygame.draw.rect(WIN, color, (i * width, HEIGHT - val * 5, width - 2, val * 5))

#     # pygame.display.update()
#     draw_text_info("Algorithm", {"speed": 60})  # temp placeholders
#     pygame.display.update()

# def draw_text_info(algorithm_name, settings):
#     font = pygame.font.SysFont('consolas', 20)

#     # Line 1: Main Controls
#     controls1 = font.render(
#         "R - Reset   |   SPACE - Start   |   + / - Speed   |   P - Preview Mode",
#         True, (180, 180, 180)
#     )
#     WIN.blit(controls1, ((WIDTH - controls1.get_width()) // 2, 10))

#     # Line 2: Sorting Options
#     controls2 = font.render(
#         "B - Bubble   |   I - Insertion   |   S - Selection",
#         True, (180, 180, 180)
#     )
#     WIN.blit(controls2, ((WIDTH - controls2.get_width()) // 2, 35))

import pygame
from settings import WIN, WIDTH, HEIGHT, BAR_COLOR, BG_COLOR

def draw_list(lst, color_positions=None):
    if color_positions is None:
        color_positions = {}

    WIN.fill(BG_COLOR)
    width = WIDTH // len(lst)

    for i, val in enumerate(lst):
        color = color_positions.get(i, BAR_COLOR)
        pygame.draw.rect(WIN, color, (i * width, HEIGHT - val * 5, width - 2, val * 5))

    # NOTE: Do NOT call draw_text_info() here — it's called from main.py after this
    pass

def draw_text_info(algorithm_name, settings):
    font = pygame.font.SysFont('consolas', 20)

    # Line 0: Algorithm name + direction (e.g. BUBBLE SORT - ASC)
    title = font.render(algorithm_name, True, (255, 255, 255))
    WIN.blit(title, ((WIDTH - title.get_width()) // 2, 10))

    # Line 1: Main controls
    controls1 = font.render(
        "R - Reset   |   SPACE - Start   |   + / - Speed   |   P - Preview Mode",
        True, (180, 180, 180)
    )
    WIN.blit(controls1, ((WIDTH - controls1.get_width()) // 2, 35))

    # Line 2: Sorting options
    controls2 = font.render(
        "B - Bubble   |   I - Insertion   |   S - Selection   |   A - Asc   |   D - Desc",
        True, (180, 180, 180)
    )
    WIN.blit(controls2, ((WIDTH - controls2.get_width()) // 2, 60))
