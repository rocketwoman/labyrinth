import pickle
from maze.maze import Maze
from walker.adventurer import Adventurer

def play():
    a = Adventurer(maze)
    print("""
        print 'east', 'west', 'north' or 'south' to move,
        'skip' to stay where you are,
        'exit' to exit and 
        'map' to see map
        'save' to save the game""")
    treasure_found = False
    while treasure_found == False:
        command = input()
        if command == 'east':
            a.go('east')
        elif command == 'west':
            a.go('west')
        elif command == 'north':
            a.go('north')
        elif command == 'south':
            a.go('south')
        elif command == 'skip':
            a.skip()
        elif command == 'map':
            print(maze)
            a.skip()
        elif command=='save':
            name = input()
            with open(f'{name}.pkl', 'wb') as output:
                pickle.dump(maze, output, pickle.HIGHEST_PROTOCOL)
        elif command == 'exit':
            break
        else:
            print('this command doesn\'t exist!')

        if a.check_for_exit():
                break

                
print('continue old game or start a new one? type \'old\' or \'new\'')
is_new = input()
if is_new == 'old':
    print('enter filename:')
    name = input()
    maze = pickle.load(open(f'{name}.pkl', "rb"))
    print('old maze is uploaded')
    play()
        
if is_new == 'new':
    print('enter the size of the maze:')
    size = input()

    maze = Maze(int(size))
    maze.make_maze()
    print('maze of size {} is saved to maze.png'.format(size))

    maze.write_svg('maze.svg')
    play()
else:
    print('???')