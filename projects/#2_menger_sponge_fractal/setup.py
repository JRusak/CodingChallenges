import pygame
from sponge import Sponge

WHITE = (255, 255, 255)
RED = (255, 0, 0)


def setup(width, height):
    pygame.init()
    pygame.display.set_mode([width, height])

    origin = [0, 0, 0]
    sponge = Sponge(0, 0, 0, 210, origin)
    sponge.translate_center([width // 2, height // 2, 0])

    sponges = [sponge]

    return sponges


def draw(sponges):
    screen = pygame.display.get_surface()
    width, height = pygame.display.get_window_size()
    pace = 5e-3

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                sponges = mouse_pressed(sponges)

        screen.fill(WHITE)

        for sponge in sponges:
            sponge.rotate_x(pace)
            sponge.rotate_y(pace)
            sponge.rotate_z(pace)
            sponge.show(screen, False)

        clock.tick(60)
        pygame.display.flip()


def mouse_pressed(sponges):
    new = []

    for sponge in sponges:
        new += sponge.generate()

    return new


def main():
    width = 600
    height = 600

    sponges = setup(width, height)
    draw(sponges)


if __name__ == '__main__':
    main()
