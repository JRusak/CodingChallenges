import random


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, vector):
        self.x += vector.x
        self.y += vector.y

    @staticmethod
    def random(n):
        return Vector(random.choice(range(-n, n+1)), random.choice(range(-n, n+1)))

    @staticmethod
    def combine(vec1, vec2):
        new_x = vec1.x + vec2.x
        new_y = vec1.y + vec2.y
        return Vector(new_x, new_y)
