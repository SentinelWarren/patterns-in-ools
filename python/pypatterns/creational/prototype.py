from copy import deepcopy
from typing import Dict
from abc import ABCMeta, abstractmethod


class Prototype(metaclass=ABCMeta):
    @abstractmethod
    def clone(self):
        pass


class ConcreteProto(Prototype):
    def __init__(self) -> None:
        self.objects: Dict[str, object] = dict()
    
    def register(self, identifier: str, obj: object) -> None:
        self.objects[identifier] = obj

    def unregister(self, identifier: str) -> None:
        del self.objects[identifier]

    def clone(self, identifier: str) -> object:
        found = self.objects.get(identifier)
        if not found:
            raise ValueError(f"Incorrect object identifier: {identifier}")
        
        return deepcopy(found)

    
if __name__ == '__main__':
    prototype = ConcreteProto()
    prototype.clone('test')
