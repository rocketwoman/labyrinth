import pickle
from serializer.serializer import Serializer

class PickleSaver(Serializer):
    
    def serialize(self, name, maze):
        with open(f'{name}.pkl', 'wb') as output:
                pickle.dump(maze, output, pickle.HIGHEST_PROTOCOL)
                
    def deserialize(self, name):
        return pickle.load(open(f'{name}.pkl', "rb"))