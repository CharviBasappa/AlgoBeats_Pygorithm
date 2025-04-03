import pygame

# BAR_GRADIENTS = [
#     (180, 205, 255),
#     (130, 180, 255),
#     (80, 150, 255)
# ]
# BG_COLOR = (0, 0, 0)

THEMES = [
    {
        "BACKGROUND_COLOR": (20, 20, 30),
        "BAR_GRADIENTS": [(0, 191, 255), (30, 144, 255), (70, 130, 180)]  # 💙 Ocean Blues
    },
    {
        "BACKGROUND_COLOR": (15, 15, 15),
        "BAR_GRADIENTS": [(255, 99, 71), (255, 140, 0), (255, 215, 0)]  # 🔥 Sunset
    },
    {
        "BACKGROUND_COLOR": (25, 25, 25),
        "BAR_GRADIENTS": [(186, 85, 211), (148, 0, 211), (75, 0, 130)]  # 💜 Violet Dreams
    },
    {
        "BACKGROUND_COLOR": (240, 240, 240),
        "BAR_GRADIENTS": [(100, 149, 237), (72, 61, 139), (106, 90, 205)]  # 🌤 Cool Twilight
    },
]


# Default
THEME_INDEX = 0
CURRENT_THEME = THEMES[THEME_INDEX]

WIDTH, HEIGHT = 1000, 650
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Algorithm Visualizer")
