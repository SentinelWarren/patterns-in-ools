"""pypatterns doc

Changelog
---------
"""

__title__ = 'Python Patterns'
__description__ = 'Practical Design Patterns in Python'
__url__ = 'https://github.com/SentinelWarren/patterns-in-langs'
__version__ = '0.1.1'
__author__ = 'SentinelWarren'
__author_email__ = 'warrenkalolo@gmail.com'
__license__ = 'MIT'
__copyright__ = 'Copyright (c) 2021 SentinelWarren'

__all__ = (
    'Singleton',
    'FooTone',
    'Logger',
    'Prototype',
    'ConcreteProto',
    'RTS',
)

from .singleton.singleton import Singleton, FooTone
from .singleton.logger import Logger

from .prototype.prototype import Prototype, ConcreteProto
from .prototype.rts import RTS