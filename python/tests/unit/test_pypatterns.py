from pypatterns import __version__, __all__


def test_version():
    expected = '0.1.1'
    assert __version__ == expected

def test_all():
    expected = (
        'Singleton',
        'FooTone',
        'Logger',
        'Prototype',
        'ConcreteProto',
        'RTS',
    )
    assert __all__ == expected
