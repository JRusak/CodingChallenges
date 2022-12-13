import pygame.draw


class Bullet:
    def __init__(self, x, y, color):
        self.width, self.height = pygame.display.get_window_size()
        self.screen = pygame.display.get_surface()
        self.x = x
        self.y = y
        self.color = color
        self.speed = 3
        self.operative = True

    def show(self):
        pygame.draw.line(self.screen, self.color, (self.x, self.y - 20), (self.x, self.y), 5)

    def disable(self):
        self.operative = False

    def update(self):
        if self.y < 0 or self.y - 20 > self.height:
            self.disable()


class ShipBullet(Bullet):
    def update(self):
        super(ShipBullet, self).update()
        self.y -= self.speed


class AlienBullet(Bullet):
    def update(self):
        super(AlienBullet, self).update()
        self.y += self.speed
