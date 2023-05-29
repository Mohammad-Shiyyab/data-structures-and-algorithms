import pytest

from linked_list.linked_list import LinkedList


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


def test_linked_list_length(linked_list):
    
    actual = linked_list.length
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


def test_linked_list_to_string_None():
    actual = LinkedList().to_string()
    expected = "NONE"
    assert actual == expected


def test_linked_list_to_string(linked_list):
    actual = linked_list.to_string()
    expected = "{ 3 } -> { 2 } -> { 1 } -> NONE"
    assert actual == expected


def test_linked_list_append_one():
    actual = LinkedList()
    actual.append(1)
    expected = 1
    assert actual.head is not None
    assert actual.head.value == expected

def test_linked_list_append_multiple():
    actual = LinkedList()
    actual.append(1)
    actual.append(2)
    actual.append(3)
    expected = "{ 1 } -> { 2 } -> { 3 } -> NONE"
    assert actual.to_string() == expected

def test_insert_after_head(linked_list):
    linked_list.insert_after(3,6)
    expected="{ 3 } -> { 6 } -> { 2 } -> { 1 } -> NONE"
    assert str(linked_list) == expected

def test_insert_after_middle(linked_list):
    linked_list.insert_after(2,6)
    expected="{ 3 } -> { 2 } -> { 6 } -> { 1 } -> NONE"
    assert str(linked_list) == expected
 

def test_insert_after_end(linked_list):
    linked_list.insert_after(1,6)
    expected="{ 3 } -> { 2 } -> { 1 } -> { 6 } -> NONE"
    assert str(linked_list) == expected

def test_insert_after_end(linked_list):
    try:
        linked_list.insert_after(8,1)
    except:
        assert True    

def test_insert_before_head(linked_list):
    linked_list.insert_before(3, 9)
    expected = "{ 9 } -> { 3 } -> { 2 } -> { 1 } -> NONE"
    assert str(linked_list) == expected



def test_insert_before_middle(linked_list):
    linked_list.insert_before(2, 9)
    expected = "{ 3 } -> { 9 } -> { 2 } -> { 1 } -> NONE"
    assert str(linked_list) == expected
    


def test_insert_before_end(linked_list):
    linked_list.insert_before(1, 9)
    expected = "{ 3 } -> { 2 } -> { 9 } -> { 1 } -> NONE"
    assert str(linked_list) == expected


def test_kth_from_end_():
    linked_list = LinkedList()
    linked_list.insert(2)
    linked_list.insert(8)
    linked_list.insert(3)
    linked_list.insert(1)
    print(linked_list)
    actual = linked_list.kth_from_end(k=0)
    expected=2
    assert actual == expected
    
def test_kth_from_end_out_the_rage():
    linked_list = LinkedList()
    linked_list.insert(2)
    linked_list.insert(8)
    linked_list.insert(3)
    linked_list.insert(1)

    try:
       
       linked_list.kth_from_end(6)  
    except:
        
        assert True 



def test_zip_lists():
    linked_list_one = LinkedList()
    linked_list_one.append(1)
    linked_list_one.append(3)
    linked_list_one.append(2)
    linked_list_two = LinkedList()
    linked_list_two.append(5)
    linked_list_two.append(9)
    linked_list_two.append(4)

    actual = LinkedList.zip_lists(linked_list_one, linked_list_two)
    expected = "{ 1 } -> { 5 } -> { 3 } -> { 9 } -> { 2 } -> { 4 } -> NONE"
    
    assert str(actual) == expected


def test_zip_lists_one_longer():
    linked_list_one = LinkedList()
    linked_list_one.append(1)
    linked_list_one.append(3)
    linked_list_one.append(2)
    linked_list_two = LinkedList()
    linked_list_two.append(5)
    linked_list_two.append(9)

    actual = LinkedList.zip_lists(linked_list_one, linked_list_two)
    expected = "{ 1 } -> { 5 } -> { 3 } -> { 9 } -> { 2 } -> NONE"
    assert str(actual) == expected


def test_zip_lists_two_longer():
    linked_list_one = LinkedList()
    linked_list_one.append(1)
    linked_list_one.append(3)
    linked_list_two = LinkedList()
    linked_list_two.append(5)
    linked_list_two.append(9)
    linked_list_two.append(4)

    actual = LinkedList.zip_lists(linked_list_one, linked_list_two)
    expected = "{ 1 } -> { 5 } -> { 3 } -> { 9 } -> { 4 } -> NONE"

    assert str(actual) == expected


def test_zip_lists_one_empty():
    linked_list_one = LinkedList()
    linked_list_two = LinkedList()
    linked_list_two.append(5)
    linked_list_two.append(9)
    linked_list_two.append(4)

    actual = LinkedList.zip_lists(linked_list_one, linked_list_two)
    expected = "{ 5 } -> { 9 } -> { 4 } -> NONE"
    assert str(actual) == expected


def test_zip_lists_two_empty():
    linked_list_one = LinkedList()
    linked_list_one.append(1)
    linked_list_one.append(3)
    linked_list_one.append(2)
    linked_list_two = LinkedList()

    actual = LinkedList.zip_lists(linked_list_one, linked_list_two)
    expected = "{ 1 } -> { 3 } -> { 2 } -> NONE"
    assert str(actual) == expected
