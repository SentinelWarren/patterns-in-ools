from patterns import __version__, __all__


def test_version():
    assert __version__ == '0.1.1'

def test_all():
    assert __all__ == [
                        'Singleton',
                        'FooTone',
                        'Logger',
                        'Prototype',
                        'RTS',
                    ]
