import pygame

WHITE = (255, 255, 255)


class Cell:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.screen = pygame.display.get_surface()
        self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
        self.visited = False

    def show(self, cell_size, current=False):
        x = self.i * cell_size
        y = self.j * cell_size

        if current:
            pygame.draw.rect(self.screen, (0, 0, 255, 100), (x, y, cell_size, cell_size))
        elif self.visited:
            pygame.draw.rect(self.screen, (255, 0, 255, 100), (x, y, cell_size, cell_size))

        if self.walls['top']:
            pygame.draw.line(self.screen, WHITE, (x, y), (x + cell_size, y), 1)
        if self.walls['left']:
            pygame.draw.line(self.screen, WHITE, (x, y), (x, y + cell_size), 1)
        if self.walls['bottom']:
            pygame.draw.line(self.screen, WHITE, (x + cell_size, y + cell_size), (x + cell_size, y), 1)
        if self.walls['right']:
            pygame.draw.line(self.screen, WHITE, (x + cell_size, y + cell_size), (x + cell_size, y), 1)
