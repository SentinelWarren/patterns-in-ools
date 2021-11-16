from typing import Dict


class Singleton(type):
    _instances: Dict[str, object] = dict()

    def __call__(cls, *args: object, **kwargs: object) -> object:
        if str(cls) not in cls._instances:
            cls._instances[str(cls)] = super(Singleton,
            cls).__call__(*args, **kwargs)

        return cls._instances[str(cls)]


class FooTone(metaclass=Singleton):
    def __init__(self, arg: str) -> None:
        self.attribute = arg

    def __repr__(self) -> str:
        return (
            f"<class {self.__class__.__name__}("
            f"{self.attribute!r}) "
            f"at {hex(id(self))}>"
        )
