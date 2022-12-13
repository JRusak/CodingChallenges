import pygame

from star import Star


def setup(width, height, n_stars, fullscreen):
    pygame.init()
    if fullscreen:
        pygame.display.set_mode([0, 0], pygame.FULLSCREEN)
    else:
        pygame.display.set_mode([width, height])

    stars = [Star() for _ in range(n_stars)]

    return stars


def draw(stars):
    screen = pygame.display.get_surface()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        speed = pygame.mouse.get_pos()[0] / pygame.display.get_window_size()[0] * 10

        screen.fill(0)

        for star in stars:
            star.update(speed)
            star.show()

        pygame.display.flip()


def main():
    width = 600
    height = 600
    fullscreen = True

    n_stars = 100

    stars = setup(width, height, n_stars, fullscreen)
    draw(stars)


if __name__ == '__main__':
    main()
