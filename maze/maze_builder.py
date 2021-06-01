from abc import ABCMeta, abstractmethod
class IMaze(metaclass=ABCMeta):
    
    @abstractmethod
    def make_maze(self):
        raise NotImplementedError("Not implemented")
        
    @abstractmethod
    def get_wormholes(self):
        raise NotImplementedError("Not implemented")