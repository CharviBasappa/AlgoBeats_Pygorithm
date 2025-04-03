import pygame
from settings import WIN
from data import generate_list
from visualizer import draw_list, draw_text_info
from sorts import bubble_sort, insertion_sort, selection_sort
from visualsort import run_preview_mode

lst = generate_list()
sorting = False
sort_generator = None

# Track current sort + label
current_sort = bubble_sort
current_algo_name = "BUBBLE SORT"
ascending = True

clock = pygame.time.Clock()
settings = {"speed": 60}

run = True
while run:
    clock.tick(settings["speed"])

    # Draw current state every frame
    draw_list(lst)
    direction = "ASC" if ascending else "DESC"
    draw_text_info(f"{current_algo_name} - {direction}", settings)
    pygame.display.update()

    if sorting:
        try:
            next(sort_generator)
        except StopIteration:
            sorting = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:

            # Sort selection keys
            if event.key == pygame.K_b and not sorting:
                current_sort = bubble_sort
                current_algo_name = "BUBBLE SORT"

            elif event.key == pygame.K_i and not sorting:
                current_sort = insertion_sort
                current_algo_name = "INSERTION SORT"

            elif event.key == pygame.K_s and not sorting:
                current_sort = selection_sort
                current_algo_name = "SELECTION SORT"

            # Direction keys
            elif event.key == pygame.K_a:
                ascending = True

            elif event.key == pygame.K_d:
                ascending = False

            # Reset list
            elif event.key == pygame.K_r:
                lst = generate_list()
                sorting = False
                sort_generator = None
                current_sort = bubble_sort
                current_algo_name = "BUBBLE SORT"
                ascending = True

            # Start sorting
            elif event.key == pygame.K_SPACE and not sorting:
                sort_generator = current_sort(lst, draw_list, settings, ascending)
                sorting = True

            # Preview mode (custom feature)
            elif event.key == pygame.K_p and not sorting:
                run_preview_mode()

            # Speed controls
            elif event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
                settings["speed"] = min(240, settings["speed"] + 10)

            elif event.key == pygame.K_MINUS:
                settings["speed"] = max(10, settings["speed"] - 10)

pygame.quit()
