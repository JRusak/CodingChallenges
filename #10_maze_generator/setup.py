import pygame
from maze import Maze
from generator import Generator
from logger import Logger

BACKGROUND_COLOR = (51, 51, 51)


def setup(width, height, cell_size):
    pygame.init()
    pygame.display.set_mode([width, height], pygame.RESIZABLE)

    cols = width // cell_size
    rows = height // cell_size
    return Maze(cols, rows, cell_size), Logger()


def draw(generator, speed):
    screen = pygame.display.get_surface()
    clock = pygame.time.Clock()

    running = True

    generator.log()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                generator.print_log_result()
                running = False
            elif event.type == pygame.KEYDOWN:
                key_pressed(generator, event)
                break

        screen.fill(BACKGROUND_COLOR)

        if generator.move_on():
            generator.log()

        generator.show_maze()

        pygame.display.flip()
        clock.tick(speed)


def key_pressed(generator, event):
    if event.key == pygame.K_SPACE:
        generator.reset()
        generator.log()


def main():
    width = 400
    height = 400
    speed = 5
    cell_size = 40

    maze, logger = setup(width, height, cell_size)
    generator = Generator(maze, logger)
    draw(generator, speed)


if __name__ == '__main__':
    main()
