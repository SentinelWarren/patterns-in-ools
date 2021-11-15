from pypatterns import Singleton
from pytest import raises

def test_instances_raises():
    with raises(KeyError):
        Singleton._instances['invalid']
