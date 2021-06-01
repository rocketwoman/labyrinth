from visualizer.visualizer import Visualizer

class ConsoleDrawer(Visualizer):
    
    def draw(self, nx, ny, maze_map):
        """Return a (crude) string representation of the maze."""

        maze_rows = ['-' * nx * 2]
        for y in range(ny):
            maze_row = ['|']
            for x in range(nx):
                if maze_map[x][y].walls['E']:
                    maze_row.append(' |')
                else:
                    maze_row.append('  ')
            maze_rows.append(''.join(maze_row))
            maze_row = ['|']
            for x in range(nx):
                if maze_map[x][y].walls['S']:
                    maze_row.append('-+')
                else:
                    maze_row.append(' +')
            maze_rows.append(''.join(maze_row))
        print('\n'.join(maze_rows))