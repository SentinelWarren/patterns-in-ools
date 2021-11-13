__version__ = '0.1.1'
__all__ = [
            'Singleton',
            'FooTone',
            'Logger',
            'Prototype',
            'RTS',
        ]

from patterns.singleton.singleton import Singleton, FooTone
from patterns.singleton.logger import Logger

from patterns.prototype.prototype import Prototype
from patterns.prototype.rts import RTS