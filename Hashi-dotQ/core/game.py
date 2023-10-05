from .randomize import Randomize
from .gameElements import Board
from .gameElements import *
from pygame import mixer

mixer.init()
clic_sound = mixer.Sound("Hashi-dotQ/core/sounds/clic.mp3")
clic_island_complete = mixer.Sound("Hashi-dotQ/core/sounds/island_complete.mp3")

def set_level(s):
    if s == 'easy':
        return 0
    if s == 'midi':
        return 1
    if s == 'hard':
        return 2


def is_finished(l):
    finished = False
    for i in l:
        if i.conections == i.value:
            finished = True
        else:
            return False
    if finished is True:
        clic_island_complete.play()
        return True


class Game:
    def __init__(self, s='easy'):
        self.level = set_level(s)
        self.randomize = Randomize(self.level)
        self.number_of_circle = self.randomize.random_circle()
        self.board = Board(self.number_of_circle)
        self.number_of_hints = 0


def is_in(l, source, dest):
    for b in l:
        if (b.circle1 == source and b.circle2 == dest) or (b.circle1 == dest and b.circle2 == source):
            return True, int(l.index(b))

    return False, 0


def if_remove(l, source, dest):
    for b in l:
        if ((b.circle1 == source and b.circle2 == dest) or (
                        b.circle1 == dest and b.circle2 == source)) and b.number == 1:
            return True, int(l.index(b))

    return False, 0


def check(z, g):
    if len(z) == 2:
        if z[0] in z[1].close_neighbors:
            w = is_in(g.board.user_list_bridge, z[0], z[1])
            s = if_remove(g.board.user_list_bridge, z[0], z[1])
            clic_sound.play()
            if s[0]:
                g.board.user_list_bridge.remove(g.board.user_list_bridge[s[1]])
                z[0].conections -= 1
                z[1].conections -= 1
            # elif w[0]:
            #     g.board.user_list_bridge.remove(g.board.user_list_bridge[w[1]])
            #     z[0].conections -= 1
            #     z[1].conections -= 1
            #     g.board.user_list_bridge.append(Bridge(z[0], z[1], green, 2))
                # z[0].add_bridge(z[1], 2)
            elif w[0] is False:
                g.board.user_list_bridge.append(Bridge(z[0], z[1], green, 1))
                z[0].add_bridge(z[1], 1)

        z[0].change_color(circle_green)
        z[1].change_color(circle_green)
        z.clear()


def clear_bridges(l):
    for i in l:
        # if i.number == 2:
        #     i.circle1.conections -= 2
        #     i.circle2.conections -= 2
        if i.number == 1:
            i.circle1.conections -= 1
            i.circle2.conections -= 1
        i.circle1.change_color(circle_green)
        i.circle2.change_color(circle_green)
    l.clear()


def show_solution(l):
    for i in l:
        i.conections = i.value


def print_bridge(l):
    for i in range(len(l)):
        if l[i].number == 1:
            l[i].show()
        # if l[i].number == 2:
        #     l[i].show_more()
