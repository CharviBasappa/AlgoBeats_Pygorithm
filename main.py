import pygame
from settings import WIN
from data import generate_list
from visualizer import draw_list, draw_text_info
from sorts import bubble_sort, insertion_sort, selection_sort, quick_sort, merge_sort, heap_sort
from visualsort import run_preview_mode
import settings

lst = generate_list()
sorting = False
sort_generator = None

current_sort = bubble_sort
current_algo_name = "BUBBLE SORT"
ascending = True

clock = pygame.time.Clock()
visual_settings = {"speed": 60}

run = True
while run:
    clock.tick(visual_settings["speed"])

    draw_list(lst)
    direction = "ASC" if ascending else "DESC"
    draw_text_info(f"{current_algo_name} - {direction}", visual_settings )
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

            if event.key == pygame.K_b and not sorting:
                current_sort = bubble_sort
                current_algo_name = "BUBBLE SORT"

            elif event.key == pygame.K_i and not sorting:
                current_sort = insertion_sort
                current_algo_name = "INSERTION SORT"

            elif event.key == pygame.K_s and not sorting:
                current_sort = selection_sort
                current_algo_name = "SELECTION SORT"
            
            elif event.key == pygame.K_q and not sorting:
                current_sort = quick_sort
                current_algo_name = "QUICK SORT"

            elif event.key == pygame.K_m and not sorting:
                current_sort = merge_sort
                current_algo_name = "MERGE SORT"

            elif event.key == pygame.K_h and not sorting:
                current_sort = heap_sort
                current_algo_name = "HEAP SORT"

            elif event.key == pygame.K_t:
                settings.THEME_INDEX = (settings.THEME_INDEX + 1) % len(settings.THEMES)
                settings.CURRENT_THEME = settings.THEMES[settings.THEME_INDEX]


            elif event.key == pygame.K_a:
                ascending = True

            elif event.key == pygame.K_d:
                ascending = False

            elif event.key == pygame.K_r:
                lst = generate_list()
                sorting = False
                sort_generator = None
                current_sort = bubble_sort
                current_algo_name = "BUBBLE SORT"
                ascending = True

            elif event.key == pygame.K_SPACE and not sorting:
                sort_generator = current_sort(lst, draw_list, visual_settings , ascending)
                sorting = True

            elif event.key == pygame.K_p and not sorting:
                run_preview_mode()

            elif event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
                visual_settings ["speed"] = min(240, visual_settings ["speed"] + 10)

            elif event.key == pygame.K_MINUS:
                visual_settings ["speed"] = max(10, visual_settings ["speed"] - 10)

pygame.quit()
