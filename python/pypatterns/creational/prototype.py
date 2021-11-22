"Prototype pattern Sample Code"
from abc import ABCMeta, abstractmethod
from typing import Any, Dict
from copy import copy, deepcopy


class IPrototype(metaclass=ABCMeta):
    "interface with clone method"
    #@staticmethod
    @abstractmethod
    def clone(self):
        """The clone method, deep or shallow.
        It is up to you how you want to implement
        the details in your concrete class
        """


class IPrototype2(metaclass=ABCMeta):
    "interface with clone method that takes arguments"
    @abstractmethod
    def clone(self, identifier):
        """The clone method, deep or shallow.
        It is up to you how you want to implement
        the details in your concrete class
        """


class ConcreteProto(IPrototype):
    "1st concrete Prototype Class"

    def __init__(self, field: Any) -> None:
        self.field = field

    def clone(self) -> object:
        """This clone method uses a 2 level shallow copy technique"""
        return type(self)(copy(self.field))


class ConcreteProto2(IPrototype2):
    "2nd concrete Prototype Class"

    def __init__(self) -> None:
        self.objects: Dict[str, object] = {}

    def register(self, identifier: str, obj: object) -> None:
        """Add an object to the cloned objects dict"""
        self.objects[identifier] = obj

    def unregister(self, identifier: str) -> None:
        """Remove an object from the cloned objects dict"""
        del self.objects[identifier]

    def clone(self, identifier: str):
        """This clone method uses a deep copy technique"""
        found = self.objects.get(identifier)
        if not found:
            raise ValueError(f"Incorrect object identifier: {identifier}")

        return deepcopy(found)


if __name__ == '__main__':
    prototype = ConcreteProto2()
    prototype.register('proto', prototype)
    proto = prototype.clone('proto')
