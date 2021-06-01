from cell.cell import Cell
from maze.maze_builder import IMaze

class Maze():
    
    def __init__(self):
        """Initialize the maze grid.
        The maze consists of nx x ny cells and will be constructed starting
        at the cell indexed at (ix, iy).

        """

        self.nx = 4
        self.ny = 4
        self.ix = 0
        self.iy = 0
        self.maze_map = [[Cell(x, y) for y in range(4)] for x in range(4)]
        self.exit_x = 4
        self.exit_y = 4
        
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
            print(neighbours)
            direction, next_cell = neighbours[0]
            current_cell.knock_down_wall(next_cell, direction)
            cell_stack.append(current_cell)
            current_cell = next_cell
            nv += 1

        self.treasure = cell_stack[-1]
        self.wormholes = self.get_wormholes()
    
        
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
    
    def cell_at(self, x, y):
        """Return the Cell object at (x,y)."""

        return self.maze_map[x][y]
    
    def get_wormholes(self):
        size = 5
        xs = [0, 1, 2, 3, 0]
        ys = [1, 2, 3, 0, 1]
            
        wormholes = list(zip(xs, ys))
        return wormholes