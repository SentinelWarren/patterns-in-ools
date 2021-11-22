"""Testing singleton.SingletonMeta exceptions"""
from pypatterns import singleton
from pytest import raises

def test_instances_raises():
    """Test KeyError exception"""
    with raises(KeyError):
        instances = singleton.SingletonMeta.get_instances()
        instances['invalid-key']
