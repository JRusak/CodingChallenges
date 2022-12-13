import random
import pygame

FORBIDDEN_TURNS = {'LEFT': 'RIGHT',
                   'RIGHT': 'LEFT',
                   'UP': 'DOWN',
                   'DOWN': 'UP'}


class Snake:
    def __init__(self, cell_size, top_offset):
        self.cell_size = cell_size
        self.screen_top_offset = top_offset
        self.directions = {'UP': (0, -cell_size), 'DOWN': (0, cell_size), 'LEFT': (-cell_size, 0), 'RIGHT': (cell_size, 0)}
        self.width, self.height = pygame.display.get_window_size()
        self.screen = pygame.display.get_surface()
        self.x = random.choice(range(0, self.width, cell_size))
        self.y = random.choice(range(top_offset, self.height, cell_size))
        self.d = random.choice([*self.directions.keys()])
        self.x_speed, self.y_speed = self.directions[self.d]
        self.total = 1
        self.tail = [(self.x, self.y)]

    def update(self, food, wall_hack=True):
        self.x += self.x_speed
        self.y += self.y_speed

        if wall_hack:

            # go through walls
            if self.x < 0:
                self.x = self.width
            elif self.x > self.width - self.cell_size:
                self.x = 0

            if self.y < self.screen_top_offset:
                self.y = self.height
            elif self.y > self.height - self.cell_size:
                self.y = self.screen_top_offset
        else:

            # don't go through walls
            self.x = max(0, self.x)
            self.x = min(self.x, self.width - self.cell_size)

            self.y = max(self.screen_top_offset, self.y)
            self.y = min(self.y, self.height - self.cell_size)

        self.eat(food)
        self.update_tail(food)

    def show(self):
        for x, y in self.tail:
            pygame.draw.rect(self.screen, (255, 255, 255), (x, y, self.cell_size, self.cell_size), 5, 5)

    def dir(self, d):
        if self.d == FORBIDDEN_TURNS[d]:
            return

        self.d = d

        x, y = self.directions[d]
        self.x_speed = x
        self.y_speed = y

    def eat(self, food):
        if not (self.x == food.x and self.y == food.y):
            return

        self.total += 1

    def update_tail(self, food):
        if (self.x, self.y) in self.tail:
            self.total = 1
            self.tail = [(self.x, self.y)]
            return

        if self.total == len(self.tail):
            for i in range(self.total - 1):
                self.tail[i] = self.tail[i + 1]
            self.tail[self.total - 1] = (self.x, self.y)
        else:
            self.tail.append((self.x, self.y))
            food.update(self)
