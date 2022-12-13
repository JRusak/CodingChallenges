import random
import pygame.draw

PURPLE = (138, 43, 226)


class Drop:
    def __init__(self):
        self.width, self.height = pygame.display.get_window_size()
        self.screen = pygame.display.get_surface()
        self.x = random.choice(range(self.width))
        self.y = random.choice(range(-500, -51))
        self.z = random.choice(range(21))
        self.len = self.z / 2 + 10
        self.y_speed = self.z / 20 * 19 + 1

    def fall(self):
        self.y += self.y_speed
        grav = self.z / 20 * 0.2
        self.y_speed += grav

        if self.y > self.height:
            self.y = random.choice(range(-200, -101))
            self.y_speed = self.z / 20 * 6 + 4

    def show(self):
        thick = self.z // 20 * 2 + 1
        pygame.draw.line(self.screen, PURPLE, (self.x, self.y), (self.x, self.y + self.len), thick)

