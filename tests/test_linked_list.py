from linked_list import LinkedList


def test_linked_list_push_front_pop_back():
    r = range(0, 50)
    list = LinkedList()
    for i in r:
        list.push_front(i)

    for i in range(0, 50):
        assert list.pop_back() == i


def test_linked_list_push_back_pop_front():
    r = range(0, 50)
    list = LinkedList()
    for i in r:
        list.push_back(i)

    for i in range(0, 50):
        assert list.pop_front() == i


def test_linked_list_remove_idx():
    r = range(0, 100)
    list = LinkedList()
    for i in r:
        list.push_back(i)

    # Too far
    removed = list.remove(100)
    assert removed == None

    removed = list.remove(10)
    assert removed == 10

    removed = list.remove(10)
    assert removed == 11

    removed = list.remove(97)
    assert removed == 99
