from abc import ABCMeta, abstractmethod
class Walker(metaclass=ABCMeta):
    
    @abstractmethod
    def go(self):
        raise NotImplementedError("Not implemented")