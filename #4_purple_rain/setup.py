import pygame
from drop import Drop

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

BACKGROUND = (230, 230, 250)

N_DROPS = 500


def setup(width, height):
    pygame.init()
    pygame.display.set_mode([width, height])
    pygame.display.set_caption('Purple rain')
    font_style = pygame.font.Font(None, 50)

    drops = [Drop() for _ in range(N_DROPS)]

    return font_style, drops


def draw(drops):
    width = pygame.display.get_window_size()[0]
    screen = pygame.display.get_surface()
    clock = pygame.time.Clock()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BACKGROUND)

        for drop in drops:
            drop.fall()
            drop.show()

        pygame.display.flip()

        clock.tick(60)


def main():
    width = 600
    height = 600

    font_style, drops = setup(width, height)
    draw(drops)


if __name__ == '__main__':
    main()
