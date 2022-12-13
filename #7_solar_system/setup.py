import pygame
from Tools.box import Box

WHITE = (255, 255, 255)
RED = (255, 0, 0)


def setup(width, height):
    pygame.init()
    pygame.display.set_mode([width, height])


def draw():
    screen = pygame.display.get_surface()
    width, height = pygame.display.get_window_size()

    clock = pygame.time.Clock()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)

        clock.tick(60)
        pygame.display.flip()


def main():
    width = 600
    height = 600

    setup(width, height)
    draw()


if __name__ == '__main__':
    main()
