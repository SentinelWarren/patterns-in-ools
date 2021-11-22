from pypatterns import prototype
from pytest import raises

def test_objects_raises():
    with raises(KeyError):
        prototype.ConcreteProto2().objects['invalid']

def test_clone_raises():
    with raises(ValueError) as e:
        prototype.ConcreteProto2().clone('invalid')
    
    assert e.value.args[0] == "Incorrect object identifier: invalid"
