from pypatterns import ConcreteProto
from pytest import raises

def test_objects_raises():
    with raises(KeyError):
        ConcreteProto().objects['invalid']

def test_clone_raises():
    with raises(ValueError) as e:
        ConcreteProto().clone('invalid')
    
    assert e.value.args[0] == "Incorrect object identifier: invalid"
