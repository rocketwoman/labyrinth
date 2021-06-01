from abc import ABCMeta, abstractmethod
class Interactor(metaclass=ABCMeta):
    
    @abstractmethod
    def interact(self):
        raise NotImplementedError("Not implemented")