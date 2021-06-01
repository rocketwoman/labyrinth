import pickle
from maze.maze import Maze
from walker.adventurer import Adventurer
from serializer.pickle_saver import PickleSaver
from visualizer.visualizer import Visualizer
from visualizer.console_drawer import ConsoleDrawer
from interactor.interactor import Interactor

class ConsoleInteractor(Interactor):

    def interact(self):

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
                    maze.show()
                    a.skip()
                elif command=='save':
                    ps = PickleSaver()
                    name = input()
                    ps.serialize(name, maze)
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
            ps = PickleSaver()
            maze = ps.deserialize(name)
            print('old maze is uploaded')
            play()

        if is_new == 'new':
            print('enter the size of the maze:')
            size = input()

            maze = Maze(int(size), ConsoleDrawer())
            maze.make_maze()
            play()
        else:
            print('???')