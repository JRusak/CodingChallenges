import random
import pygame


class Food:
    def __init__(self, snake, cell_size, top_offset):
        self.cell_size = cell_size
        self.screen_top_offset = top_offset
        self.screen_width, self.screen_height = pygame.display.get_window_size()
        self.screen = pygame.display.get_surface()
        self.x, self.y = self.set_location(snake)

    def update(self, snake):
        self.x, self.y = self.set_location(snake)

    def set_location(self, snake):
        food_x, food_y = snake.tail[0]

        while (food_x, food_y) in snake.tail:
            food_x = random.choice(range(0, self.screen_width, self.cell_size))
            food_y = random.choice(range(self.screen_top_offset, snake.height, self.cell_size))

        return food_x, food_y

    def show(self):
        pygame.draw.rect(self.screen, (255, 0, 100), (self.x, self.y, self.cell_size, self.cell_size), border_radius=10)
