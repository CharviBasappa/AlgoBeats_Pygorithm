from settings import WIN, WIDTH, HEIGHT, BAR_COLOR, BG_COLOR
import pygame

def draw_list(lst, color_positions=None):
    if color_positions is None:
        color_positions = {}

    WIN.fill(BG_COLOR)
    width = WIDTH // len(lst)

    for i, val in enumerate(lst):
        color = color_positions.get(i, BAR_COLOR)
        pygame.draw.rect(WIN, color, (i * width, HEIGHT - val * 5, width - 2, val * 5))

    pygame.display.update()
