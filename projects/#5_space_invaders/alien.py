import random

import pygame

from bullet import AlienBullet

RED = (255, 0, 0)
YELLOW = (255, 255, 0)


class Alien:
    def __init__(self, x, y, alien_size):
        self.alien_size = alien_size
        self.width, self.height = pygame.display.get_window_size()
        self.screen = pygame.display.get_surface()
        self.x = x
        self.y = y
        self.x_dir = 1
        self.speed = 1
        self.y_dir = alien_size // 2
        self.visible = True
        self.bullets = []
        self.shoot_chance = 1e-3

    def show(self):
        if not self.is_visible():
            return

        pygame.draw.ellipse(self.screen, RED, (self.x, self.y, self.alien_size, self.alien_size))

    def update(self, bullets):
        self.hit_check(bullets)

        self.x += self.x_dir * self.speed

        if random.uniform(0, 1) < self.shoot_chance and self.visible:
            self.shoot_bullet()

        for bullet in self.bullets[::-1]:
            if not bullet.operative:
                self.bullets.remove(bullet)
                continue

            bullet.show()
            bullet.update()

    def shoot_bullet(self):
        self.bullets.append(AlienBullet(self.x + self.alien_size // 2, self.y + self.alien_size, YELLOW))

    def edge_touchdown(self):
        return self.x <= 0 or self.x + self.alien_size >= self.width

    def change_x_dir(self):
        self.x_dir *= -1
        self.y += self.y_dir

    def is_visible(self):
        return self.visible

    def hit_check(self, bullets):
        for bullet in bullets:
            if self.visible and self.was_hit(bullet):
                self.visible = False
                bullet.disable()

    def was_hit(self, bullet):
        return bullet.x + 5 >= self.x and bullet.x <= self.x + self.alien_size and bullet.y - 20 <= self.y + self.alien_size and bullet.y >= self.y
