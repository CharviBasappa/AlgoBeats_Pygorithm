import pygame
from settings import WIN, WIDTH, HEIGHT

side_padding = 60

def draw_list(lst, color_positions=None):
    from settings import CURRENT_THEME

    if color_positions is None:
        color_positions = {}

    WIN.fill(CURRENT_THEME["BACKGROUND_COLOR"])
    bar_width = (WIDTH - side_padding * 2) / len(lst)
    gradients = CURRENT_THEME["BAR_GRADIENTS"]

    for i, val in enumerate(lst):
        color = color_positions.get(i, gradients[i % len(gradients)])
        x = side_padding + i * bar_width
        pygame.draw.rect(WIN, color, (x, HEIGHT - val * 5, bar_width - 1, val * 5))


def draw_text_info(algorithm_name, settings, duration=None):
    font = pygame.font.SysFont('consolas', 20)

    title = font.render(algorithm_name, True, (255, 255, 255))
    WIN.blit(title, ((WIDTH - title.get_width()) // 2, 10))

    controls1 = font.render(
        "R - Reset | A - Asc | D - Desc | SPACE - Start | T - Theme | + / - Speed | O - Replay last list",
        True, (180, 180, 180)
    )
    WIN.blit(controls1, ((WIDTH - controls1.get_width()) // 2, 35))

    controls2 = font.render(
        "I - Insertion | B - Bubble | S - Selection | Q - Quick | M - Merge | H - Heap",
        True, (180, 180, 180)
    )
    WIN.blit(controls2, ((WIDTH - controls2.get_width()) // 2, 60))

    # ✅ Live speed display
    speed_display = font.render(f"Speed: {settings['speed']} FPS", True, (255, 255, 255))
    # WIN.blit(speed_display, (WIDTH - 160, HEIGHT - 30))
    WIN.blit(speed_display, (20, 100))


    if duration is not None:
        label = "Sorting" if isinstance(duration, float) and duration < 60 else "Sorting completed in"
        timer_font = pygame.font.SysFont('consolas', 18)
        timer_text = timer_font.render(f"{label}: {duration:.2f} seconds", True, (255, 255, 255))
        WIN.blit(timer_text, ((WIDTH - timer_text.get_width()) // 2, 85))
        
