from .settings import *


def text_display(text, s, color, position):
    t = text_object(text, s, color)
    rect = t.get_rect()
    rect.center = position
    game_display.blit(t, rect)


def text_object(text, s, color):
    font = pygame.font.Font(None, s)
    text_surface = font.render(text, True, color)
    return text_surface
