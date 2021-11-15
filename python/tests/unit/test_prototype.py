from pypatterns import ConcreteProto
from collections import namedtuple


def test_prototype():
    point = namedtuple('Point', 'x y')
    prototype = ConcreteProto()
    
    id1 = 'Point'
    id2 = 'CP-1'
    id3 = 'CP-2'
    id4 = 'CP-3'

    prototype.register(id1, point)
    assert id1 in prototype.objects

    prototype.register(id2, prototype)
    assert id2 in prototype.objects

    for key in (id3, id4):
        prototype.register(key, prototype.clone(id2))

    assert prototype.objects[id2] != prototype.objects[id3] != prototype.objects[id4]
    assert '' not in prototype.objects
    
    for key in (id1, id2, id3, id4):
        prototype.unregister(key)
        assert key not in prototype.objects

    assert len(prototype.objects) == 0
