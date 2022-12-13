import random
from cell import Cell


class Maze:
    def __init__(self, cols, rows, cell_size):
        self.cols = cols
        self.rows = rows
        self.cell_size = cell_size
        self.grid = self.create_grid()
        self.current = self.grid[0]

    def create_grid(self):
        grid = []
        for j in range(self.rows):
            for i in range(self.cols):
                grid.append(Cell(i, j))
        return grid

    def show(self):
        for cell in self.grid:
            cell.show(self.cell_size)
        self.current.show(self.cell_size, True)

    def _idx(self, i, j):
        return i + j * self.cols

    def _cell_in_bounds(self, i, j):
        return not (i < 0 or j < 0 or i > self.cols - 1 or j > self.rows - 1)

    def _get_cell(self, i, j):
        if self._cell_in_bounds(i, j):
            return self.grid[self._idx(i, j)]

    def _get_neighbours(self):
        i, j = self.current.i, self.current.j
        top = self._get_cell(i, j-1)
        left = self._get_cell(i-1, j)
        right = self._get_cell(i+1, j)
        bottom = self._get_cell(i, j+1)

        return [cell for cell in [top, left, right, bottom] if cell and not cell.visited]

    def get_neighbour(self):
        neighbours = self._get_neighbours()
        return random.choice(neighbours) if neighbours else None

    def get_number_of_visited_cells(self):
        return sum(cell.visited for cell in self.grid)

    def reset(self):
        self.grid = self.create_grid()
        self.current = self.grid[0]

    def remove_walls(self, next_cell):
        i_curr, j_curr = self.current.i, self.current.j
        i_nxt, j_nxt = next_cell.i, next_cell.j
        di = i_curr - i_nxt
        dj = j_curr - j_nxt

        if (di, dj) == (0, 1):
            self.current.walls['top'] = False
            next_cell.walls['down'] = False
        elif (di, dj) == (1, 0):
            self.current.walls['left'] = False
            next_cell.walls['right'] = False
        elif (di, dj) == (0, -1):
            self.current.walls['bottom'] = False
            next_cell.walls['top'] = False
        elif (di, dj) == (-1, 0):
            self.current.walls['right'] = False
            next_cell.walls['left'] = False

    def get_number_of_neighbours(self):
        return len(self._get_neighbours())
