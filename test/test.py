#!/usr/bin/env python3

import propertybag as pb

try:
    import sparen
    Log = sparen.log
except:
    Log = print


def test_1():

    _p = pb.Bag(a='b', c='d')
    Log(_p.toJson(True))

    assert _p['a'] == 'b'
    assert _p.a == 'b'

    _p.a = 'z'
    assert _p.a == 'z'
    _p.a = 'b'

    r = str(_p)
    Log(r)
    assert r == '{"a": "b", "c": "d"}'
    assert _p.as_dict() == {"a": "b", "c": "d"}

    r = len(_p)
    Log(r)
    assert r == 2

    _p.set("b.c.d", 42)
    r = _p.get("b.c.d")
    Log(r)
    assert r == 42

    _p.set("b.c.d.e", 42)
    r = _p.get("b.c.d")
    Log(r)
    assert r == {'e': 42}

    r = _p.get("b.c.d.f", "missing")
    Log(r)
    assert r == "missing"

    r = repr(_p)
    Log(r)
    assert r == "Bag(a='b', c='d', b={'c': {'d': {'e': 42}}})"

    _p2 = eval("pb."+repr(_p))
    Log(_p2)
    assert _p == _p2

    _p2.v = 'changed'
    Log(_p2)
    assert _p != _p2

    i = 0
    r = ['a', 'c', 'b']
    for k in _p:
        Log(k, '==', r[i])
        assert r[i] == k
        i += 1

    i = 0
    r = [{'a': 'b'}, {'c': 'd'}, {'b': {'c': {'d': {'e': 42}}}}]
    for k,v in _p.items():
        Log(k, v, '==', r[i][k])
        assert r[i][k] == v
        i += 1

    _p2['v'] = 'changed_again'
    Log(_p2['v'])
    assert _p2['v'] == 'changed_again'


def test_2():

    _p = pb.Bag({'a':{'b': 'c'}, 'd':'e'})

    r = _p.a.b
    Log(r)
    assert r == 'c'

    _p.x.y.z = 'v'
    r = _p.x.y.z
    Log(r)
    assert r == 'v'

    _p2 = _p.copy()

    fail = False
    try:
        # Read non-existant value
        print(_p.q.r.s)
    except ValueError as e:
        Log(str(e))
        fail = True
    assert fail

    # Reading non-existant value shouldn't change anything
    assert _p == _p2

    _p = pb.Bag()
    assert 'a' not in _p

    _p.a.b = 42
    assert 'a' in _p
    assert 'b' in _p.a

    del _p.a.b
    assert 'a' in _p
    assert 'b' not in _p.a

    del _p.a
    assert 'a' not in _p

    _p.a.b = 42
    assert 'a' in _p
    assert 'b' in _p.a

    del _p.a['b']
    assert 'a' in _p
    assert 'b' not in _p.a

    del _p['a']
    assert 'a' not in _p

    if _p.a:
        raise Exception('Bool failed')

    if _p.a > 0:
        raise Exception('> failed')
    if _p.a < 0:
        raise Exception('< failed')

    _p = pb.Bag({}, 99, 99)
    assert _p.a.b.c == 99

    _p.a.b.c = 100
    assert _p.a.b.c == 100

    if not _p.a:
        raise Exception('Bool failed')


def test_3():

    _p = pb.Bag({'a': {'a': 1, 'b': 2, 'c': 3, 'd': 4}})

    i = 1
    for k, v in _p.a.items():
        Log(i, v)
        assert i == v
        i += 1


def main():
    test_1()
    test_2()
    test_3()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        Log(e)
