import pygame


def setup(width, height):
    pygame.init()
    pygame.display.set_mode([width, height], pygame.RESIZABLE)


def draw():
    screen = pygame.display.get_surface()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(0)

        pygame.display.flip()


def main():
    width = 600
    height = 600

    setup(width, height)
    draw()


if __name__ == '__main__':
    main()
