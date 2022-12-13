import random

import pygame

from alien import Alien
from ship import Ship

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


def setup(width, height, ship_w, ship_h):
    pygame.init()
    pygame.display.set_mode([width, height])
    pygame.display.set_caption('Space invaders')

    ship = Ship(ship_w, ship_h)
    aliens = get_aliens(width)

    return ship, aliens


def draw(ship, aliens):
    width = pygame.display.get_window_size()[0]
    screen = pygame.display.get_surface()
    clock = pygame.time.Clock()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                key_pressed(ship, event)
            elif event.type == pygame.KEYUP:
                key_released(ship, event)

        screen.fill(BLACK)

        for alien in aliens[::-1]:
            if not alien.is_visible() and not alien.bullets:
                aliens.remove(alien)
                continue

            alien.show()
            alien.update(ship.bullets)

        if not aliens:
            aliens = get_aliens(width)
            ship.bullets = []

        ship.show()
        ship.update(aliens)

        if ship.is_broken():
            break

        if edge(aliens):
            change_direction(aliens)

        pygame.display.flip()

        clock.tick(60)


def key_released(ship, event):
    if event.key == pygame.K_LEFT:
        ship.release(-1)
    elif event.key == pygame.K_RIGHT:
        ship.release(1)


def key_pressed(ship, event):
    if event.key == pygame.K_LEFT:
        ship.press(-1)
    elif event.key == pygame.K_RIGHT:
        ship.press(1)
    elif event.key == pygame.K_SPACE:
        ship.shoot_bullet()


def get_aliens(width):
    aliens_in_row = random.choice(range(1, 31))
    n_alien_rows = 1 + int(aliens_in_row / 30 * 9)

    places = aliens_in_row * 2 + 1

    aliens = []

    alien_size = width // places

    for y in range(n_alien_rows):
        for x in range(1, places, 2):
            aliens.append(Alien(x * alien_size, y * 2 * alien_size, alien_size))

    return aliens


def change_direction(aliens):
    for alien in aliens:
        alien.change_x_dir()


def edge(aliens):
    return any(alien.edge_touchdown() and alien.is_visible() for alien in aliens)


def main():
    width = 600
    height = 600

    ship_w = 20
    ship_h = 50

    ship, aliens = setup(width, height, ship_w, ship_h)
    draw(ship, aliens)


if __name__ == '__main__':
    main()
