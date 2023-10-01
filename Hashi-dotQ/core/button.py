from .display import *

class Button:
    def __init__(self, x_left, y_left, w, h, color, text, size_of_letters):
        self.x = x_left
        self.y = y_left
        self.w = w
        self.h = h
        self.color = color
        self.text = text
        self.size = size_of_letters
        self.position_of_text = (0, 0)

    def show(self):
        pygame.draw.rect(game_display, self.color, (self.x, self.y, self.w, self.h))
        self.position_of_text = ((self.x + (self.w / 2)), (self.y + (self.h / 2)))
        text_display(self.text, self.size, dark_green, self.position_of_text)

    def change_color(self, color):
        self.color = color

    def backlight(self):
        mouse = pygame.mouse.get_pos()
        if self.x + self.w > mouse[0] > self.x and self.y + self.h > mouse[1] > self.y:
            self.change_color(bright_green)
            self.show()

    def is_clicked(self):
        mouse = pygame.mouse.get_pos()
        if pygame.event.peek(pygame.MOUSEBUTTONDOWN) and self.x + self.w > mouse[0] > self.x and self.y + self.h > \
                mouse[1] > self.y:
            pygame.event.clear()
            return True
        return False
