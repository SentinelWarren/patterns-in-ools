"""Testing singleton module"""
from pypatterns import singleton, logging


singleton_instances = singleton.SingletonMeta.get_instances()
FOO_CLASS = "<class 'pypatterns.creational.singleton.FooTone'>"
LOGGER_CLASS = "<class 'pypatterns.examples.creational.logging.Logger'>"

def instantiate_foo(arg):
    """Instantiate singleton.FooTone class"""
    return singleton.FooTone(arg)

def instantiate_logger(arg):
    """Instantiate logging.Logger class"""
    return logging.Logger(arg)

def delete_instance(name):
    """Delete an instance in singleton.SingletonMeta"""
    if name in singleton_instances:
        del singleton_instances[name]

def test_global_state():
    """Test Singleton global state"""
    foo1 = instantiate_foo("some_attr")
    foo2 = instantiate_foo("diff_attr")
    assert foo1 is foo2
    assert foo1.attribute == foo2.attribute

    foo2.attribute = "another_attr"
    assert foo1.attribute == foo2.attribute

def test_empty_instances():
    """Test empty singleton.Singleton._instances"""
    singleton_instances.clear()

    assert len(singleton_instances) == 0
    assert LOGGER_CLASS, FOO_CLASS not in singleton_instances

def test_all_added_instances():
    """Test all added instances in singleton.Singleton._instances"""
    if LOGGER_CLASS not in singleton_instances:
        instantiate_logger("file.log")

    if FOO_CLASS not in singleton_instances:
        instantiate_foo("some_attr")

    assert len(singleton_instances) == 2
    assert FOO_CLASS, LOGGER_CLASS in singleton_instances

def test_logger_instance():
    """Test only logging.Logger instance in singleton.Singleton._instances"""
    delete_instance(FOO_CLASS)

    assert len(singleton_instances) == 1
    assert LOGGER_CLASS in singleton_instances

def test_foo_instance():
    """Test only singleton.FooTone instance in singleton.Singleton._instances"""
    instantiate_foo("some_attr")
    delete_instance(LOGGER_CLASS)

    assert len(singleton_instances) == 1
    assert FOO_CLASS in singleton_instances
