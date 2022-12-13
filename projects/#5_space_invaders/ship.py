import pygame

from bullet import ShipBullet

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)


class Ship:
    def __init__(self, ship_w, ship_h):
        self.ship_w = ship_w
        self.ship_h = ship_h
        self.width, self.height = pygame.display.get_window_size()
        self.screen = pygame.display.get_surface()
        self.x = (self.width - ship_w) // 2
        self.y = self.height - ship_h
        self.x_dir = 0
        self.speed = 3
        self.left = False
        self.right = False
        self.bullets = []
        self.lives = 3

    def show(self):
        pygame.draw.rect(self.screen, WHITE, (self.x, self.y, self.ship_w, self.ship_h))

    def update(self, aliens):
        self.hit_check(aliens)
        self.move()
        self.update_bullets()

    def update_bullets(self):
        for bullet in self.bullets[::-1]:
            if not bullet.operative:
                self.bullets.remove(bullet)
                continue

            bullet.show()
            bullet.update()

        if not self.bullets:
            return

        bullet = self.bullets[0]

        if bullet.y <= 0:
            self.bullets.remove(bullet)

    def move(self):
        m = self.x_dir * self.speed

        if (self.x + m) < 0 or (self.x + self.ship_w + m) > self.width:
            return

        self.x += m

    def set_dir(self, direction):
        self.x_dir = direction

    def press(self, direction):
        if direction < 0:
            self.left = True
        elif direction > 0:
            self.right = True

        self.set_dir(direction)

    def release(self, direction):
        if direction < 0:
            self.left = False
            if self.right:
                self.set_dir(1)
        elif direction > 0:
            self.right = False
            if self.left:
                self.set_dir(-1)

        if self.stop_check():
            self.set_dir(0)

    def stop_check(self):
        return not (self.left or self.right)

    def shoot_bullet(self):
        self.bullets.append(ShipBullet(self.x + self.ship_w // 2, self.y, BLUE))

    def hit_check(self, aliens):
        for alien in aliens:
            for bullet in alien.bullets:
                if self.was_hit(bullet):
                    self.lives -= 1
                    bullet.disable()

    def was_hit(self, bullet):
        return self.x <= bullet.x <= self.x + self.ship_w and bullet.y >= self.y and bullet.y - 20 <= self.y + self.ship_h

    def is_broken(self):
        return self.lives == 0
