from collections import namedtuple
from pypatterns import prototype


def test_ConcreteProto():
    proto = prototype.ConcreteProto([1,2,3,4])
    proto2 = proto.clone()
    proto3 = proto2.clone()
    assert proto.field == proto2.field == proto3.field
    assert proto != proto2 != proto3

def test_ConcreteProto2():
    point = namedtuple('Point', 'x y')
    proto = prototype.ConcreteProto2()

    id1 = 'Point'
    id2 = 'CP-1'
    id3 = 'CP-2'
    id4 = 'CP-3'

    proto.register(id1, point)
    assert id1 in proto.objects

    proto.register(id2, proto)
    assert id2 in proto.objects

    for key in (id3, id4):
        proto.register(key, proto.clone(id2))

    assert proto.objects[id2] != proto.objects[id3] != proto.objects[id4]
    assert '' not in proto.objects

    for key in (id1, id2, id3, id4):
        proto.unregister(key)
        assert key not in proto.objects

    assert len(proto.objects) == 0
