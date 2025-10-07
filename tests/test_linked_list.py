from linked_list import LinkedList, LinkedListNode


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
    for i in r:
        list.push_front(i)

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
