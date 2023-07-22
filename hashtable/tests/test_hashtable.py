
from hashtable.hashtable import Hashtable


def test_hashtable_insert_one():
    hatb = Hashtable()
    hatb.set('apple', 5)
    assert hatb.get('apple') == 5


def test_hashtable_insert_two():
    hatb = Hashtable()
    hatb.set('apple', 5)
    hatb.set('banana', 6)
    assert hatb.get('apple') == 5
    assert hatb.get('banana') == 6



def hatb():
    hs = Hashtable()
    hs.set('apple', 5)
    hs.set('banana', 6)
    hs.set('carrot', 7)

    return hs


def test_hashtable_get_none(hatb):
    assert hatb.get('dinosaur') == None


def test_hashtable_get_value(hatb):
    assert hatb.get('apple') == 5


def test_hashtable_get_value_collision():
    hatb = Hashtable(2)
    hatb.set('apple', 5)
    hatb.set('banana', 6)
    hatb.set('carrot', 7)
    keys = hatb.keys()
    keys.sort()
    assert keys == ['apple', 'banana', 'carrot']


def test_hashtable_has_key_true(hatb):
    assert hatb.has('apple') == True


def test_hashtable_has_key_false(hatb):
    assert hatb.has('dinosaur') == False


def test_hashtable_key(hatb):
    expected = ['apple', 'banana', 'carrot']
    actual = hatb.keys()
    expected.sort()
    actual.sort()
    assert actual == expected