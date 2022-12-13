import math

import pygame
import random


class Board:
    def __init__(self, da, db, feed, k, drops, size_of_drop):
        self.width, self.height = pygame.display.get_window_size()
        self.screen = pygame.display.get_surface()
        self.grid = self._make_a_grid()
        self.next = self._make_a_grid()
        self.da = da
        self.db = db
        self.feed = feed
        self.k = k
        self.drops = drops
        self.size_of_drop = size_of_drop
        self._put_random_drops()

    def _make_a_grid(self):
        grid = []
        for x in range(self.width):
            grid.append([])
            for y in range(self.height):
                grid[x].append({'a': 1, 'b': 0})
        return grid

    def clear_board(self):
        self.grid = self._make_a_grid()
        self.next = self._make_a_grid()

    def reset(self):
        self.clear_board()
        self._put_random_drops()

    def _put_random_drops(self):
        for _ in range(self.drops):
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            for i in range(x, x + min(self.size_of_drop, self.width - x)):
                for j in range(y, y + min(self.size_of_drop, self.height - y)):
                    self.grid[i][j]['b'] = 1

    def update(self):
        for x in range(1, self.width-1):
            for y in range(1, self.height-1):
                a = self.grid[x][y]['a']
                b = self.grid[x][y]['b']
                new_a = a + (self.da * self._laplace(x, y, 'a') - a * b**2 + self.feed * (1 - a))
                new_b = b + (self.db * self._laplace(x, y, 'b') + a * b**2 - (self.k + self.feed) * b)
                self.next[x][y]['a'] = 1 if new_a > 1 else max(new_a, 0)
                self.next[x][y]['b'] = 1 if new_b > 1 else max(new_b, 0)

        self._swap()

    def _laplace(self, x, y, letter):
        s = 0
        s += self.grid[x][y][letter] * -1
        s += self.grid[x-1][y][letter] * 0.2
        s += self.grid[x+1][y][letter] * 0.2
        s += self.grid[x][y-1][letter] * 0.2
        s += self.grid[x][y+1][letter] * 0.2
        s += self.grid[x+1][y+1][letter] * 0.05
        s += self.grid[x-1][y-1][letter] * 0.05
        s += self.grid[x+1][y-1][letter] * 0.05
        s += self.grid[x-1][y+1][letter] * 0.05
        return s

    def draw(self):
        for x in range(self.width):
            for y in range(self.height):
                c = self._get_color(x, y)
                pygame.Surface.set_at(self.screen, [x, y], (c, c, c, 255))

    def _get_color(self, x, y):
        a = self.next[x][y]['a']
        b = self.next[x][y]['b']
        c = math.floor((a - b) * 255)
        c = 0 if c < 0 else min(c, 255)
        return c

    def _swap(self):
        self.grid, self.next = self.next, self.grid
