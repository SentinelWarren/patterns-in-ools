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

__all__ = [
    'singleton',
    'logging',
    'prototype',
    'rts',
]

# __all__ = [
    #     'Singleton',
    #     'FooTone',
    #     'Logger',
    #     'IPrototype',
    #     'IPrototype2',
    #     'ConcreteProto',
    #     'ConcreteProto2',
    #     'RTS',
    # ]

from .creational import singleton
from .creational import prototype

from .examples.creational import logging, rts
