import math
import random

import pygame
from vector import Vector


class Cell:
    def __init__(self, pos=None, r=30, c=None):
        self.width, self.height = pygame.display.get_window_size()
        self.screen = pygame.display.get_surface()
        self.pos = Vector(random.choice(range(self.width)), random.choice(range(self.height))) if not pos else pos
        self.r = r
        self.c = pygame.color.Color(random.choice(range(100, 256)), 0, random.choice(range(100, 256)), 100) if not c else c
        self.speed = random.choice(range(1, 10))

    def show(self):
        pygame.draw.ellipse(self.screen, self.c, (self.pos.x, self.pos.y, 2 * self.r, 2 * self.r), 5)

    def move(self):
        vec = Vector.random(self.speed)
        self.pos.add(vec)

        self.pos.x = max(0, self.pos.x)
        self.pos.x = min(self.pos.x, self.width - 2 * self.r)

        self.pos.y = max(0, self.pos.y)
        self.pos.y = min(self.pos.y, self.height - 2 * self.r)

    def mitosis(self):
        new_positions = [Vector.combine(self.pos, Vector.random(self.speed)) for _ in range(2)]
        return [Cell(pos, self.r, self.c) for pos in new_positions]

    def clicked(self, x, y):
        d = math.dist((self.pos.x + self.r, self.pos.y + self.r), (x, y))
        return d < self.r
