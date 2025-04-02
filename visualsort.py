import pygame
import random

def run_preview_mode():
    pygame.init()
    win = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Quick Visual Mode")

    lst = [random.randint(10, 100) for _ in range(50)]

    def draw():
        win.fill((0, 0, 0))
        width = 800 // len(lst)
        for i, val in enumerate(lst):
            pygame.draw.rect(win, (100, 200, 255), (i * width, 600 - val * 5, width - 2, val * 5))
        pygame.display.update()

    run = True
    while run:
        draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()
