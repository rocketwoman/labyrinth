from abc import ABCMeta, abstractmethod
class Visualizer(metaclass=ABCMeta):
    
    @abstractmethod
    def draw(self, filename):
        raise NotImplementedError("Not implemented")