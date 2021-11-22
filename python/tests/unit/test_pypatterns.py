# pylint: disable=undefined-all-variable
"""Test pypatterns.__init__.py"""
from pypatterns import __version__, __all__


def test_version():
    """Test pypatterns version"""
    expected = '0.1.1'
    assert __version__ == expected

def test_all():
    """Test pypatterns import"""
    expected = [
        'singleton',
        'logging',
        'prototype',
        'rts',
    ]

    assert __all__ == expected
