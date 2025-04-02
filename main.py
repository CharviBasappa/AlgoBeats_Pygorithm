import pygame
from settings import WIN
from data import generate_list
from visualizer import draw_list
from sorts import bubble_sort, insertion_sort, selection_sort
from visualsort import run_preview_mode

lst = generate_list()
sorting = False
sort_generator = None
current_sort = bubble_sort  # default sort


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
            if event.key == pygame.K_b and not sorting:
                print("🔁 Bubble Sort selected. Press SPACE to start.")
                current_sort = bubble_sort

            elif event.key == pygame.K_i and not sorting:
                print("🔁 Insertion Sort selected. Press SPACE to start.")
                current_sort = insertion_sort

            elif event.key == pygame.K_s and not sorting:
                print("🔁 Selection Sort selected. Press SPACE to start.")
                current_sort = selection_sort

            elif event.key == pygame.K_r:
                print("🔄 List reset to new random values.")
                lst = generate_list()
                sorting = False
                sort_generator = None
                current_sort = bubble_sort

            elif event.key == pygame.K_SPACE and not sorting:
                if current_sort:
                    print("▶️ Sorting started...")
                    sort_generator = current_sort(lst, draw_list, speed)
                    sorting = True

            elif event.key == pygame.K_p and not sorting:
                print("⚡ Launching preview mode...")
                run_preview_mode()

pygame.quit()
