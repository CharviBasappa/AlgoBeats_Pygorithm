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

def insertion_sort(lst, draw_callback, speed=60):
    for i in range(1, len(lst)):
        current = lst[i]
        j = i
        while j > 0 and lst[j - 1] > current:
            lst[j] = lst[j - 1]
            j -= 1
            lst[j] = current

            # Sound
            try:
                winsound.Beep(100 + lst[j]*10, 20)
            except:
                pass

            # Visual
            draw_callback(lst, {j: (0, 255, 0), j + 1: (255, 100, 100)})
            pygame.time.wait(1000 // speed)
            yield True


def selection_sort(lst, draw_callback, speed=60):
    for i in range(len(lst)):
        min_idx = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j

        lst[i], lst[min_idx] = lst[min_idx], lst[i]

        try:
            winsound.Beep(100 + lst[i]*10, 20)
        except:
            pass

        draw_callback(lst, {i: (0, 255, 0), min_idx: (255, 100, 100)})
        pygame.time.wait(1000 // speed)
        yield True
