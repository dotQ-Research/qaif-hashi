import random
from operator import attrgetter
from .solver import *
import copy

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
        n = random.choice(self.board)
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
                    if len(self.list_circle[i].close_neighbors) == 1:
                        value = random.randint(1, 2)
                    else:
                        value = random.randint(0, 2)
                    if value != 0:
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
