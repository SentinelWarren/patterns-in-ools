from pypatterns import Singleton, FooTone, Logger


foo = "<class 'pypatterns.singleton.singleton.FooTone'>"
logger = "<class 'pypatterns.singleton.logger.Logger'>"

def instantiate_foo(arg):
    return FooTone(arg)

def instantiate_logger(arg):
    return Logger(arg)

def delete_instance(name):
    if name in Singleton._instances.keys():
        del Singleton._instances[name]

def test_global_state():
    foo1 = instantiate_foo("some_attr")
    foo2 = instantiate_foo("diff_attr")
    assert foo1 == foo2
    assert foo1.attribute == foo2.attribute

    foo2.attribute = "another_attr"
    assert foo1.attribute == foo2.attribute

def test_empty_instances():
    Singleton._instances.clear()
    
    assert len(Singleton._instances) == 0
    assert logger, foo not in Singleton._instances

def test_all_instances():
    if logger not in Singleton._instances:
        instantiate_logger("file.log")
    
    if foo not in Singleton._instances:
        instantiate_foo("some_attr")
    
    assert len(Singleton._instances) == 2
    assert foo, logger in Singleton._instances

def test_logger_instance():
    delete_instance(foo)
    
    assert len(Singleton._instances) == 1
    assert logger in Singleton._instances

def test_foo_instance():
    instantiate_foo("some_attr")
    delete_instance(logger)
    
    assert len(Singleton._instances) == 1
    assert foo in Singleton._instances
