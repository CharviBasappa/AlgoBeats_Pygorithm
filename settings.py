import pygame

WIDTH, HEIGHT = 1000, 650
# BAR_COLOR = (100, 200, 255)
BAR_GRADIENTS = [
    (180, 205, 255),
    (130, 180, 255),
    (80, 150, 255)
]
BG_COLOR = (0, 0, 0)

pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Algorithm Visualizer")
