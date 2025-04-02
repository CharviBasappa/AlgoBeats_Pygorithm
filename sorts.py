import winsound
import pygame
from visualizer import draw_list

def bubble_sort(lst, draw_callback, speed=60):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

                # Sound
                try:
                    winsound.Beep(100 + lst[j]*10, 20)
                except:
                    pass

                # Visual update
                draw_callback(lst, {j: (0, 255, 0), j + 1: (255, 100, 100)})
                pygame.time.wait(1000 // speed)
                yield True
