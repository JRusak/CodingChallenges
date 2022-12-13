import pygame
from cell import Cell


def setup(width, height, n_cells):
    pygame.init()
    pygame.display.set_mode([width, height])

    cells = [Cell() for _ in range(n_cells)]

    return cells


def draw(cells):
    screen = pygame.display.get_surface()
    clock = pygame.time.Clock()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pressed(cells)

        screen.fill((200, 200, 200))

        for cell in cells:
            cell.show()
            cell.move()

        pygame.display.flip()

        clock.tick(20)


def mouse_pressed(cells):
    mouse_x, mouse_y = pygame.mouse.get_pos()

    for i in range(len(cells)):
        cell = cells[i]
        if cell.clicked(mouse_x, mouse_y):
            for c in cell.mitosis():
                cells.append(c)
            cells.remove(cell)
            break


def main():
    width = 600
    height = 600

    n_cells = 3

    cells = setup(width, height, n_cells)
    draw(cells)


if __name__ == '__main__':
    main()
