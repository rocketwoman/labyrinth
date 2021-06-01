from walker.walker import Walker

class Adventurer(Walker):

    def __init__(self, maze):
        self.maze = maze
        self.ix = maze.iy
        self.iy = maze.ix
        self.current_cell = maze.cell_at(self.ix, self.iy)
        print("You're starting at {}, {}".format(self.ix, self.iy))
        print("The treasure is hidden at {}, {}".format(self.maze.treasure.x, self.maze.treasure.y))
        print("The exit is at {}, {}".format(self.maze.exit_x, self.maze.exit_y))
        
    def check_for_wormholes(self):
        for wormhole in self.maze.wormholes:
            if (wormhole[0] == self.current_cell.x and \
               wormhole[1] == self.current_cell.y):
                print('wormhole!')
                return True
        return False
    
    def check_for_treasure(self):
        if (self.maze.treasure.x == self.current_cell.x and \
               self.maze.treasure.y == self.current_cell.y):
                print('You found treasure!')
                treasure_found = True
                
    def check_for_exit(self):
        exit_found = False
        if (self.maze.exit_x == self.current_cell.x and \
               self.maze.exit_y == self.current_cell.y):
                print('You found exit!')
                exit_found = True
        return exit_found
    
    def go(self, direction):
        directions = {'east': 'E', 'west': 'W', 'north': 'N', 'south': 'S'}
        short_direction = directions.get(direction)
        if short_direction in self.maze.find_all_available_neighbours(self.current_cell):
            if short_direction == 'E':
                self.current_cell = self.maze.cell_at(self.ix+1, self.iy)
            if short_direction == 'W':
                self.current_cell = self.maze.cell_at(self.ix-1, self.iy)
            if short_direction == 'N':
                self.current_cell = self.maze.cell_at(self.ix, self.iy-1)
            if short_direction == 'S':
                self.current_cell = self.maze.cell_at(self.ix, self.iy+1)
            self.ix = self.current_cell.x
            self.iy = self.current_cell.y
            
            if self.check_for_wormholes():
                hole_number = self.maze.wormholes.index((self.current_cell.x, self.current_cell.y))
                print('You\'ve been teleported by a wormhole!')
                if hole_number == 4:
                    next_portal = self.maze.wormholes[0]
                    self.current_cell = self.maze.cell_at(next_portal[0], next_portal[1])
                    self.ix = self.current_cell.x
                    self.iy = self.current_cell.y
                else:
                    next_portal = self.maze.wormholes[hole_number+1]
                    self.current_cell = self.maze.cell_at(next_portal[0], next_portal[1])
                    self.ix = self.current_cell.x
                    self.iy = self.current_cell.y
                
            print("You're now at {}, {}".format(self.ix, self.iy))
            self.check_for_treasure()
            self.check_for_wormholes()
        else:
            print('step impossible, wall')
            
        return self.current_cell
    
    def skip(self):
        if self.check_for_wormholes():
            hole_number = self.maze.wormholes.index((self.current_cell.x, self.current_cell.y))
            if hole_number == 4:
                next_portal = self.maze.wormholes[0]
                self.current_cell = self.maze.cell_at(next_portal[0], next_portal[1])
                self.ix = self.current_cell.x
                self.iy = self.current_cell.y
            else:
                next_portal = self.maze.wormholes[hole_number+1]
                self.current_cell = self.maze.cell_at(next_portal[0], next_portal[1])
                self.ix = self.current_cell.x
                self.iy = self.current_cell.y
            print('you are now at {}, {}'.format(next_portal[0], next_portal[1]))
        return self.current_cell
