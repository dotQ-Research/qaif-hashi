import random


class Randomize:
    def __init__(self, level):
        self.level = level

    def random_circle(self):
        value = 0
        if self.level == 0:
            value = random.randint(4, 7)
        if self.level == 1:
            value = random.randint(8, 10)
        if self.level == 2:
            value = random.randint(11, 13)
        return value
