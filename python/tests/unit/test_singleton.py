from patterns import Singleton, FooTone


def test_singleton(tmpdir):
    assert "<class 'patterns.singleton.singleton.FooTone'>" not in Singleton._instances
    assert len(Singleton._instances) == 0

    foo1 = FooTone(tmpdir.join("some_attr"))
    foo2 = FooTone(tmpdir.join("diff_attr"))

    assert foo1 == foo2

    foo2.attribute = tmpdir.join("another_attr")
    assert foo1.attribute == foo2.attribute

    assert len(Singleton._instances) == 1
    assert "<class 'patterns.singleton.singleton.FooTone'>" in Singleton._instances
