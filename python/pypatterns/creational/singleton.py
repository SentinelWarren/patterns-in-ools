"""Singleton Pattern sample code.

Intent: Lets you ensure that a class has only one instance, while providing a
global access point to this instance. One instance per each subclass (if any).
"""
from typing import Dict


class SingletonMeta(type):
    """Singleton metaclass
    
    The Singleton class can be implemented in different ways in Python.
    Possible methods include: base class, decorator, metaclass.
    """
    _instances: Dict[str, object] = {}

    def __call__(cls, *args: object, **kwargs: object) -> object:
        if str(cls) not in cls._instances:
            cls._instances[str(cls)] = super(SingletonMeta,
                                             cls).__call__(*args, **kwargs)

        return cls._instances[str(cls)]

    @staticmethod
    def get_instances():
        """Returns SingletonMeta _instances"""
        return SingletonMeta._instances


class FooTone(metaclass=SingletonMeta):
    """Client class"""

    def __init__(self, arg: str) -> None:
        self.attribute = arg

    def some_method(self):
        """Some method implemanting business logic,
        which can be executed on its instance."""

    def __repr__(self) -> str:
        return (
            f"<class {self.__class__.__name__}("
            f"{self.attribute!r}) "
            f"at {hex(id(self))}>"
        )
