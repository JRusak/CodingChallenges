import pygame
from board import Board

BACKGROUND_COLOR = (51, 51, 51)


def setup(width, height, params):
    pygame.init()
    pygame.display.set_mode([width, height], pygame.RESIZABLE)
    return Board(*params)


def draw(board):
    screen = pygame.display.get_surface()
    clock = pygame.time.Clock()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                key_pressed(board, event)

        screen.fill(BACKGROUND_COLOR)

        board.update()
        board.draw()

        pygame.display.flip()

        clock.tick(60)


def key_pressed(board, event):
    if event.key == pygame.K_SPACE:
        board.reset()


def main():
    width = 100
    height = 100
    drops = 4
    size_of_drop = 10

    da = 1.0
    db = 0.5
    feed = 0.055
    k = 0.061

    params = [da, db, feed, k, drops, size_of_drop]

    board = setup(width, height, params)
    draw(board)


if __name__ == '__main__':
    main()
