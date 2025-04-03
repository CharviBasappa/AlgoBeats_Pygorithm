import winsound
import pygame
from visualizer import draw_list

def bubble_sort(lst, draw_callback, settings, ascending=True):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            if (lst[j] > lst[j + 1] and ascending) or (lst[j] < lst[j + 1] and not ascending):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

                try:
                    winsound.Beep(100 + lst[j]*10, 20)
                except:
                    pass

                draw_callback(lst, {j: (0, 255, 0), j + 1: (255, 100, 100)})
                pygame.time.wait(1000 // settings["speed"])
                yield True

def insertion_sort(lst, draw_callback, settings, ascending=True):
    for i in range(1, len(lst)):
        current = lst[i]
        j = i
        while j > 0 and ((lst[j - 1] > current and ascending) or (lst[j - 1] < current and not ascending)):
            lst[j] = lst[j - 1]
            j -= 1
            lst[j] = current

            try:
                winsound.Beep(100 + lst[j]*10, 20)
            except:
                pass

            draw_callback(lst, {j: (0, 255, 0), j + 1: (255, 100, 100)})
            pygame.time.wait(1000 // settings["speed"])
            yield True

def selection_sort(lst, draw_callback, settings, ascending=True):
    for i in range(len(lst)):
        selected_idx = i
        for j in range(i + 1, len(lst)):
            if (lst[j] < lst[selected_idx] and ascending) or (lst[j] > lst[selected_idx] and not ascending):
                selected_idx = j

        lst[i], lst[selected_idx] = lst[selected_idx], lst[i]

        try:
            winsound.Beep(100 + lst[i]*10, 20)
        except:
            pass

        draw_callback(lst, {i: (0, 255, 0), selected_idx: (255, 100, 100)})
        pygame.time.wait(1000 // settings["speed"])
        yield True

def quick_sort(lst, draw_callback, settings, ascending=True):
    def partition(low, high):
        pivot = lst[high]
        i = low - 1
        for j in range(low, high):
            if (lst[j] < pivot and ascending) or (lst[j] > pivot and not ascending):
                i += 1
                lst[i], lst[j] = lst[j], lst[i]

                try:
                    winsound.Beep(100 + lst[i]*10, 20)
                except:
                    pass

                draw_callback(lst, {i: (0, 255, 0), j: (255, 100, 100)})
                pygame.time.wait(1000 // settings["speed"])
                yield True

        lst[i + 1], lst[high] = lst[high], lst[i + 1]
        try:
            winsound.Beep(100 + lst[i + 1]*10, 20)
        except:
            pass

        draw_callback(lst, {i + 1: (0, 255, 0), high: (255, 100, 100)})
        pygame.time.wait(1000 // settings["speed"])
        yield True
        return i + 1

    def quick_sort_recursive(low, high):
        if low < high:
            pi = yield from partition(low, high)
            yield from quick_sort_recursive(low, pi - 1)
            yield from quick_sort_recursive(pi + 1, high)

    yield from quick_sort_recursive(0, len(lst) - 1)


def merge_sort(lst, draw_callback, settings, ascending=True):
    def merge(left, mid, right):
        merged = []
        i, j = left, mid + 1

        while i <= mid and j <= right:
            if (lst[i] <= lst[j] and ascending) or (lst[i] >= lst[j] and not ascending):
                merged.append(lst[i])
                i += 1
            else:
                merged.append(lst[j])
                j += 1

        while i <= mid:
            merged.append(lst[i])
            i += 1
        while j <= right:
            merged.append(lst[j])
            j += 1

        for idx, val in enumerate(merged):
            lst[left + idx] = val

            try:
                winsound.Beep(100 + val * 10, 20)
            except:
                pass

            draw_callback(lst, {left + idx: (0, 255, 0)})
            pygame.time.wait(1000 // settings["speed"])
            yield True

    def merge_sort_recursive(left, right):
        if left < right:
            mid = (left + right) // 2
            yield from merge_sort_recursive(left, mid)
            yield from merge_sort_recursive(mid + 1, right)
            yield from merge(left, mid, right)

    yield from merge_sort_recursive(0, len(lst) - 1)

