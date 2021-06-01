from cell.cell import Cell
from maze.maze_builder import IMaze
from visualizer.visualizer import Visualizer
import random

class Maze(IMaze):
    """A Maze, represented as a grid of cells."""

    def __init__(self, size, visualizer: Visualizer):
        """Initialize the maze grid.
        The maze consists of nx x ny cells and will be constructed starting
        at the cell indexed at (ix, iy).

        """

        self.nx = size
        self.ny = size
        self.ix = random.randint(0, size-1)
        self.iy = random.randint(0, size-1)
        self.maze_map = [[Cell(x, y) for y in range(size)] for x in range(size)]
        self.exit_x = random.choice([0, size-1])
        self.exit_y = random.choice([0, size-1])
        self.visualizer = visualizer

    def cell_at(self, x, y):
        """Return the Cell object at (x,y)."""
        return self.maze_map[x][y]
    
    def show(self):
        self.visualizer.draw(self.nx, self.ny, self.maze_map)

            
    def find_valid_neighbours(self, cell):
        """Return a list of unvisited neighbours to cell."""

        delta = [('W', (-1, 0)),
                 ('E', (1, 0)),
                 ('S', (0, 1)),
                 ('N', (0, -1))]
        neighbours = []
        for direction, (dx, dy) in delta:
            x2, y2 = cell.x + dx, cell.y + dy
            if (0 <= x2 < self.nx) and (0 <= y2 < self.ny):
                neighbour = self.cell_at(x2, y2)
                if neighbour.has_all_walls():
                    neighbours.append((direction, neighbour))
        return neighbours
    
    def find_all_available_neighbours(self, cell):
        """Return a list of unvisited neighbours to cell."""

        delta = [('W', (-1, 0)),
                 ('E', (1, 0)),
                 ('S', (0, 1)),
                 ('N', (0, -1))]
        neighbours = []
        for direction, (dx, dy) in delta:
            x2, y2 = cell.x + dx, cell.y + dy
            if (0 <= x2 < self.nx) and (0 <= y2 < self.ny):
                neighbour = self.cell_at(x2, y2)
                neighbours = {k for k, v in cell.walls.items() if v == False}
        return neighbours

    def make_maze(self):
        # Total number of cells.
        n = self.nx * self.ny
        cell_stack = []
        current_cell = self.cell_at(self.ix, self.iy)
        # Total number of visited cells during maze construction.
        nv = 1

        while nv < n:
            neighbours = self.find_valid_neighbours(current_cell)

            if not neighbours:
                # We've reached a dead end: backtrack.
                current_cell = cell_stack.pop()
                continue

            # Choose a random neighbouring cell and move to it.
            direction, next_cell = random.choice(neighbours)
            current_cell.knock_down_wall(next_cell, direction)
            cell_stack.append(current_cell)
            current_cell = next_cell
            nv += 1
            
        self.treasure = cell_stack[-1]
        self.wormholes = self.get_wormholes()
        
    def get_wormholes(self):
        size = 5
        xs = []
        ys = []
        for i in range(size):
            xs.append(random.choice(range(self.nx)))
            ys.append(random.choice(range(self.nx)))
            
        wormholes = list(zip(xs, ys))
        return wormholes
