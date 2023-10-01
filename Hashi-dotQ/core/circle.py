from .display import *
import pygame


class Circle:
    def __init__(self, number, x, y, color):
        self.number = number
        self.x = x
        self.y = y
        self.r = 30
        self.color = color
        self.conections = 0
        self.value = number
        self.neighbors_x = list()
        self.neighbors_y = list()
        self.neighbors = list()
        self.close_neighbors = list()
        self.visited = False
        self.is_done = False
        self.is_clicked = False
        self.combinations = list()

    def change_color(self, color):
        self.color = color

    def show(self):
        c = [c1,c2,c3,c4,c5,c6,c7,c8,c9]
        pygame.draw.circle(game_display, self.color, (self.x, self.y), 30, 0)
        text_display(str(self.number),30, c[self.number-1],(self.x, self.y))

    def add_bridge(self, second_circle, value):
        self.conections += value
        second_circle.conections += value
        if second_circle.conections == second_circle.value:
            second_circle.is_done = True

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (pygame.mouse.get_pos()[0] - self.x) ** 2 + (pygame.mouse.get_pos()[1] - self.y) ** 2 <= self.r ** 2:
                self.is_clicked = True
                self.change_color(max_circle)
                return self

    def update_color(self):
        if self.conections == self.value: self.change_color(max_circle)

