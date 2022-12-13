class Logger:
    def __init__(self):
        self.logs = []

    def log_current_cell(self, maze):
        cell = maze.current
        self.logs.append(f'coords: ({cell.i}, {cell.j}), visited = {cell.visited}\nnumber of neighbours: {maze.get_number_of_neighbours()}')

    def print_logs(self, maze):
        print(*self.logs, sep='\n-\n')
        print(f'\nNumber of all logs: {self.get_number_of_logs()}')
        print(f'Number of all visited cells: {maze.get_number_of_visited_cells()}')

    def get_number_of_logs(self):
        return len(self.logs)

    def clear_logs(self):
        self.logs = []
