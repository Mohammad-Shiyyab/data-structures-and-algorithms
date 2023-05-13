import pytest 
from linked_list.linked_list_adv import LinkedList


@pytest.fixture
def linked_list():
    linked_list = LinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    return linked_list


def test_linked_list():
    actual = LinkedList()
    expected = None
    assert actual.head == expected


def test_linked_list_insert():
    actual = LinkedList()
    actual.insert(1)
    excepted = 1
    assert actual.head is not None
    assert actual.head.value == excepted


def test_linked_list_insert_multiple():
    actual = LinkedList()
    actual.insert(1)
    actual.insert(2)
    actual.insert(3)
    assert actual[0].value == 3
    assert actual[1].value == 2
    assert actual[2].value == 1


def test_linked_list_index_error(linked_list):
    with pytest.raises(IndexError):
        linked_list[5]


def test_linked_list_length(linked_list):
    actual = len(linked_list)
    expected = 3
    assert actual == expected


def test_linked_list_head(linked_list):
    head = linked_list.head
    assert head is not None
    assert head.value == 3


def test_linked_list_includes(linked_list):
    actual = linked_list.includes(1)
    expected = True
    assert actual == expected


def test_linked_list_includes_false(linked_list):
    actual = linked_list.includes(4)
    expected = False
    assert actual == expected


def test_linked_list_to_string(linked_list):
    actual = linked_list.to_string()
    expected = "{ 3 } -> { 2 } -> { 1 } -> NONE"
    assert actual == expected