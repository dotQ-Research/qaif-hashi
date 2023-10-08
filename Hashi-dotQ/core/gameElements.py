from operator import attrgetter
from .solver import *
from .display import *
import random
import copy
import pygame


def sort_circle(l, key):
    list_circle = sorted(l, key=attrgetter(key))
    return list_circle

class Board:
    def __init__(self, number_of_circle):
        self.board = list()
        self.list_circle = list()
        self.list_bridge = list()
        self.possible = list()
        self.number_of_circle = number_of_circle
        self.recognition = list()
        self.user_list_bridge = list()
        self.solver = Solver()

    def generate_default_board(self):
        for i in range(5):
            for j in range(6):
                self.board.append(Circle(0, j * 100 + 50, i * 100 + 50, circle_green))
        return self.board

    def generate_board(self):
        for i in self.list_circle:
            i = Circle(i.value, i.x, i.y, i.color)
            i.show()

    def solve(self):
        self.user_list_bridge = self.solver.solve(self.list_circle)

    def random_board(self):
        n = (random.choice(self.board))
        self.list_circle.append(n)
        for i in range(1, self.number_of_circle):
            for j in range(len(self.board)):
                if (self.board[j].x == n.x or self.board[j].y == n.y) and self.board[j] not in self.possible and \
                                self.board[j] not in self.list_circle:
                    self.possible.append(self.board[j])
            n = random.choice(self.possible)
            self.list_circle.append(n)
            self.possible.remove(n)

        return self.list_circle

    def set_neighbors(self):
        for i in range(len(self.list_circle)):
            for j in range(len(self.list_circle)):
                if self.list_circle[i].x == self.list_circle[j].x:
                    self.list_circle[i].neighbors_x.append(self.list_circle[j])
                if self.list_circle[i].y == self.list_circle[j].y:
                    self.list_circle[i].neighbors_y.append(self.list_circle[j])

    def set_close_neighbors(self):
        for i in range(len(self.list_circle)):
            sorted_y = sort_circle(self.list_circle[i].neighbors_x, 'y')
            sorted_x = sort_circle(self.list_circle[i].neighbors_y, 'x')

            for j in range(0, len(self.list_circle[i].neighbors_x)):
                index_y = sorted_y.index(self.list_circle[i])
                if sorted_y.index(self.list_circle[i].neighbors_x[j]) == index_y - 1 or sorted_y.index(
                        self.list_circle[i].neighbors_x[j]) == index_y + 1:
                    self.list_circle[i].close_neighbors.append(self.list_circle[i].neighbors_x[j])

            for j in range(0, len(self.list_circle[i].neighbors_y)):
                index_x = sorted_x.index(self.list_circle[i])
                if sorted_x.index(self.list_circle[i].neighbors_y[j]) == index_x - 1 or sorted_x.index(
                        self.list_circle[i].neighbors_y[j]) == index_x + 1:
                    self.list_circle[i].close_neighbors.append(self.list_circle[i].neighbors_y[j])

    def set_bridges(self):
        for i in range(len(self.list_circle)):
            self.list_circle[i].visited = True
            for j in range(len(self.list_circle[i].close_neighbors)):
                if self.list_circle[i].close_neighbors[j].visited is False:
                    value = 1
                    self.list_circle[i].value += value
                    self.list_circle[i].close_neighbors[j].value += value
                    self.list_bridge.append(
                        Bridge(self.list_circle[i], self.list_circle[i].close_neighbors[j], green, value))
            if self.list_circle[i].value == 0:
                for j in range(len(self.list_circle[i].close_neighbors)):
                    value = random.randint(1, 2)
                    self.list_circle[i].value += value
                    self.list_circle[i].close_neighbors[j].value += value
                    self.list_bridge.append(
                        Bridge(self.list_circle[i], self.list_circle[i].close_neighbors[j], green, value))

    def update(self, event):
        for circle in self.list_circle:
            z = circle.update(event)
            circle.update_color()
            if z is not None:
                return z

class Bridge:
    def __init__(self, from_circle, to_circle, color, value):
        self.circle1 = from_circle
        self.circle2 = to_circle
        self.color = color
        self.number = value

    def show(self):
        if self.circle1.x == self.circle2.x:
            if self.circle1.y > self.circle2.y:
                pygame.draw.line(game_display, self.color, (self.circle1.x, self.circle1.y - self.circle1.r),
                                 (self.circle2.x, self.circle2.y + self.circle2.r))
            else:
                pygame.draw.line(game_display, self.color, (self.circle2.x, self.circle2.y - self.circle2.r),
                                 (self.circle1.x, self.circle1.y + self.circle1.r))
        if self.circle1.y == self.circle2.y:
            if self.circle1.x > self.circle2.x:
                pygame.draw.line(game_display, self.color, (self.circle1.x - self.circle1.r, self.circle1.y),
                                 (self.circle2.x + self.circle2.r, self.circle2.y))
            else:
                pygame.draw.line(game_display, self.color, (self.circle2.x - self.circle2.r, self.circle2.y),
                                 (self.circle1.x + self.circle1.r, self.circle1.y))

    def show_more(self):
        if self.circle1.x == self.circle2.x:
            if self.circle1.y > self.circle2.y:
                pygame.draw.line(game_display, self.color, (self.circle1.x - 10, self.circle1.y - self.circle1.r),
                                 (self.circle2.x - 10, self.circle2.y + self.circle2.r))
                pygame.draw.line(game_display, self.color, (self.circle1.x + 10, self.circle1.y - self.circle1.r),
                                 (self.circle2.x + 10, self.circle2.y + self.circle2.r))
            else:
                pygame.draw.line(game_display, self.color, (self.circle2.x - 10, self.circle2.y - self.circle2.r),
                                 (self.circle1.x - 10, self.circle1.y + self.circle1.r))
                pygame.draw.line(game_display, self.color, (self.circle2.x + 10, self.circle2.y - self.circle2.r),
                                 (self.circle1.x + 10, self.circle1.y + self.circle1.r))
        if self.circle1.y == self.circle2.y:
            if self.circle1.x > self.circle2.x:
                pygame.draw.line(game_display, self.color, (self.circle1.x - self.circle1.r, self.circle1.y - 10),
                                 (self.circle2.x + self.circle2.r, self.circle2.y - 10))
                pygame.draw.line(game_display, self.color, (self.circle1.x - self.circle1.r, self.circle1.y + 10),
                                 (self.circle2.x + self.circle2.r, self.circle2.y + 10))
            else:
                pygame.draw.line(game_display, self.color, (self.circle2.x - self.circle2.r, self.circle2.y - 10),
                                 (self.circle1.x + self.circle1.r, self.circle1.y - 10))
                pygame.draw.line(game_display, self.color, (self.circle2.x - self.circle2.r, self.circle2.y + 10),
                                 (self.circle1.x + self.circle1.r, self.circle1.y + 10))

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