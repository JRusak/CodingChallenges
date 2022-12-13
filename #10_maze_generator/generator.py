class Generator:
    def __init__(self, maze, logger):
        self.maze = maze
        self.mark_visited()
        self.logger = logger
        self.stack = []

    def mark_visited(self):
        self.maze.current.visited = True

    def show_maze(self):
        self.maze.show()

    def move_on(self):
        next_cell = self.maze.get_neighbour()
        if next_cell is not None:
            self.stack.append(self.maze.current)
            self.maze.remove_walls(next_cell)
            self.maze.current = next_cell
            self.mark_visited()
            return True
        elif self.stack:
            self.maze.current = self.stack.pop()

    def log(self):
        self.logger.log_current_cell(self.maze)

    def print_log_result(self):
        self.logger.print_logs(self.maze)

    def print_maze_result(self):
        for cell in self.maze.grid:
            print(f'coords: ({cell.i}, {cell.j}), visited = {cell.visited}')
        print(self.maze.get_number_of_visited_cells())

    def reset(self):
        self.maze.reset()
        self.mark_visited()
        self.logger.clear_logs()
