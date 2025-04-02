import pygame
from settings import WIN
from data import generate_list
from visualizer import draw_list
from sorts import bubble_sort
from visualsort import run_preview_mode

lst = generate_list()
sorting = False
sort_generator = None

clock = pygame.time.Clock()
speed = 60

run = True
while run:
    clock.tick(speed)

    if sorting:
        try:
            next(sort_generator)
        except StopIteration:
            sorting = False

    else:
        draw_list(lst)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not sorting:
                sort_generator = bubble_sort(lst, draw_list, speed)
                sorting = True
            elif event.key == pygame.K_p and not sorting:
                print("⚡ Launching quick preview mode from visualsort.py...")
                run_preview_mode()

pygame.quit()
