from abc import ABCMeta, abstractmethod
class Serializer(metaclass=ABCMeta):
    
    @abstractmethod
    def serialize(self):
        raise NotImplementedError("Not implemented")
        
    @abstractmethod
    def deserialize(self):
        raise NotImplementedError("Not implemented")