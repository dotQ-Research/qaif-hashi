from .bridge import *
from .circle import *
import itertools


'''Hashi-dotQ/

    This class can be implemented with quanutm computing functionalities.
    E.g, as the solution is an NP problem, we can make a Hamiltonian 
    and get the minimun eigenvalue as the solution - Enrique
'''

def ready(l):
    active = list()
    for i in l:
        if i.conections < i.value:
            active.append(i)
    return active


def sort_circle(l):
    list_circle = sorted(l, key=lambda circle: (len(ready(circle.close_neighbors)), circle.value - circle.conections))
    return list_circle

class Solver:
    def __init__(self):
        self.list_bridge = list()
        self.list_circles = list()
        self.combinations = list()

    def find_possible_bridges(self, circle):
        circle.combinations = list()
        self.combinations = list(
            itertools.combinations_with_replacement(ready(circle.close_neighbors),
                                                    circle.value - circle.conections))
        bad = list()
        for i in self.combinations:
            for j in i:
                if j.value - j.conections == 1:
                    if i.count(j) > 1:
                        bad.append(i)
                        break

                if i.count(j) > 2:
                    bad.append(i)
                    break
        for i in self.combinations:
            if i not in bad:
                circle.combinations.append(i)

    def is_in(self, source, dest):
        for b in self.list_bridge:
            if (b.circle1 == source and b.circle2 == dest) or (b.circle1 == dest and b.circle2 == source):
                return True, int(self.list_bridge.index(b))

        return False, 0

    def remove_bridge(self, index):
        number = self.list_bridge[index].number
        self.list_bridge[index].circle1.conections -= number
        self.list_bridge[index].circle2.conections -= number
        self.list_bridge.remove(self.list_bridge[index])

    def remove_all(self, source, dest):
        for b in self.list_bridge:
            if (b.circle1 == source and b.circle2 == dest) or (b.circle1 == dest and b.circle2 == source):
                self.remove_bridge(self.list_bridge.index(b))

    def solve(self, circles):
        self.list_circles = circles
        self.list_circles = sort_circle(self.list_circles)
        self.recursion(0)
        return self.list_bridge

    def recursion(self, index):
        is_ok = False
        if index < len(self.list_circles):
            circle = self.list_circles[index]
            self.find_possible_bridges(circle)
            active = ready(circle.close_neighbors)

            if circle.conections == circle.value:
                return self.recursion(index + 1)

            elif len(active) > 0:
                j = 0
                while not is_ok and j < len(circle.combinations):

                    if set(circle.combinations[j]).issubset(set(active)):
                        for z in circle.combinations[j]:
                            is_in_list = self.is_in(circle, z)
                            if is_in_list[0]:
                                self.remove_bridge(is_in_list[1])
                                self.list_bridge.append(Bridge(circle, z, violet, 2))
                                circle.add_bridge(z, 2)
                            else:
                                self.list_bridge.append(Bridge(circle, z, violet, 1))
                                circle.add_bridge(z, 1)

                        is_ok = self.recursion(index + 1)
                        if not is_ok:
                            for z in circle.combinations[j]:
                                self.remove_all(circle, z)

                    j += 1
                return is_ok
            else:
                return False

        return True
