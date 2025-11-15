import pytest

from linked_list import LinkedList, LinkedListNode


def test_linked_node_str():
    assert str(LinkedListNode(0)) == "0"
    assert str(LinkedListNode("Hello World")) == "Hello World"
    assert str(LinkedListNode({"obj": "x"})) == "{'obj': 'x'}"


def test_linked_list_set_n_get():
    list = LinkedList()
    assert list.nth_node(0) == None

    list.push_back(1)
    list.push_back(2)
    list.push_back(3)

    assert list[0] == 1
    assert list[1] == 2
    assert list[2] == 3
    assert list.nth_node(0).obj == 1
    assert list.nth_node(1).obj == 2
    assert list.nth_node(2).obj == 3

    list[0] = "Hello"
    list[1] = "Sailor"
    list[2] = "!"
    assert list[0] == "Hello"
    assert list[1] == "Sailor"
    assert list[2] == "!"

    with pytest.raises(IndexError):
        list[-1] = 0
    with pytest.raises(IndexError):
        list[3] = 0
    assert list.nth_node(3) == None


def test_linked_list_insert():
    list = LinkedList()

    # If there is no elements, don't insert.
    list.insert(0, 10)
    assert list[0] == None

    list.push_back(1)
    list.push_back(2)
    list.push_back(3)

    assert list[0] == 1
    assert list[1] == 2
    assert list[2] == 3

    list.insert(1, 69)
    assert list[0] == 1
    assert list[1] == 69
    assert list[2] == 2
    assert list[3] == 3

    # Past the insert point
    list.insert(100, 10)
    assert list[100] == None


def test_linked_list_node_patching():
    n1 = LinkedListNode(20)
    assert n1.next_node == None
    assert n1.prev_node == None

    #
    # | n1 |   |
    #   v----^ add n2
    n2 = n1.add_after("420")
    assert n1.next_node == n2
    assert n1.prev_node == None
    assert n2.next_node == None
    assert n2.prev_node == n1

    #
    # | n1 |   | n2 |
    #        ^----v add n3
    n3 = n2.add_before(420)
    assert n3.next_node == n2
    assert n3.prev_node == n1
    assert n2.next_node == None
    assert n2.prev_node == n3
    assert n1.next_node == n3
    assert n1.prev_node == None

    #
    # | n1 | n3 |   | n2 |
    #        v----^ add n4
    n4 = n3.add_after("Sailor")

    #
    # | n1 | n3 | n4 | n2 |
    #

    assert n1.next_node == n3
    assert n1.prev_node == None

    assert n2.next_node == None
    assert n2.prev_node == n4

    assert n3.next_node == n4
    assert n3.prev_node == n1

    assert n4.next_node == n2
    assert n4.prev_node == n3


def test_linked_list_iterator():
    r = range(0, 50)
    list = LinkedList()
    for i in r:
        list.push_back(i)

    for i, l in zip(list, r):
        assert i == l


def test_linked_list_push_front_pop_back():
    r = range(0, 50)
    list = LinkedList()
    assert list.first() == None
    assert list.last() == None
    for i in r:
        list.push_front(i)
    assert list.last() == 0
    assert list.first() == 49

    for i in r:
        assert list.pop_back() == i
    assert list.pop_back() == None
    assert list.pop_front() == None


def test_linked_list_push_back_pop_front():
    r = range(0, 50)
    list = LinkedList()
    for i in r:
        list.push_back(i)

    for i in r:
        assert list.pop_front() == i
    assert list.pop_back() == None
    assert list.pop_front() == None


def test_linked_list_remove_idx():
    r = range(0, 100)
    list = LinkedList()
    for i in r:
        list.push_back(i)

    # Too far
    removed = list.remove(100)
    assert removed == None
    assert len(list) == 100

    removed = list.remove(10)
    assert removed == 10
    assert len(list) == 99

    removed = list.remove(10)
    assert removed == 11
    assert len(list) == 98

    removed = list.remove(97)
    assert removed == 99
    assert len(list) == 97


def test_linked_list_index_into():
    r = range(0, 100)
    list = LinkedList()
    for i in r:
        list.push_back(i)

    # Over & Under
    assert list[100] == None
    assert list[-1] == None

    for i in r:
        assert list[i] == i
