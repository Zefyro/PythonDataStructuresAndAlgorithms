import random
from typing import Any

import pytest

from src import deque
from src._array import Array
from src.container import ContainerInterface
from src.deque import Deque
from src.linked_list import LinkedList
from src.queue import Queue
from src.stack import Stack


def test_container_str():
    list = LinkedList()
    assert str(list) == "[ ]"
    list.push_back(1)
    list.push_back(2)
    list.push_back(3)
    assert str(list) == "[ 1, 2, 3 ]"

    stack = Stack()
    assert str(stack) == "[ ]"
    stack.push(3)
    stack.push(2)
    stack.push(1)
    assert str(stack) == "[ 3, 2, 1 ]"

    deque = Deque()
    assert str(deque) == "[ ]"
    deque.push_front(1)
    deque.push_front(2)
    deque.push_front(3)
    assert str(deque) == "[ 3, 2, 1 ]"


def test_container_unimplemented():
    interface = ContainerInterface()
    with pytest.raises(Exception):
        x = interface[0]
    with pytest.raises(Exception):
        interface[0] = 0
    with pytest.raises(Exception):
        for i in interface:
            print(i)
    with pytest.raises(Exception):
        n = len(interface)
    with pytest.raises(Exception):
        n = interface.merge_sort()


def test_container_find_default():
    arr = Array(100)
    for i in range(100):
        arr[i] = i

    assert arr.is_sorted()
    assert arr.find(50) == 50
    assert arr.find(1) == 1
    assert arr.find(99) == 99
    assert arr.find(111) == -1

    assert arr.find_binary(0) == 0
    assert arr.find_binary(13) == 13
    assert arr.find_binary(78) == 78
    assert arr.find_binary(111) == -1
    assert arr.find_binary(-500) == -1


def test_container_callable_finding():
    arr = Array(100)
    for i, j in enumerate(reversed(range(100))):
        arr[i] = j

    # This ordering function is for going from bigger to lower.
    def ordering_function(x: Any, y: Any):
        return x < y

    assert arr.is_sorted(ordering_function)

    assert arr.find_binary(0, ordering_function) == 99
    assert arr.find_binary(13, ordering_function) == 86
    assert arr.find_binary(78, ordering_function) == 21
    assert arr.find_binary(111, ordering_function) == -1
    assert arr.find_binary(-500, ordering_function) == -1

    # Use callable to find the element '21'
    assert arr.find_callable(lambda x: x == 21) == 78
    assert arr.find_callable(lambda x: x == 101) == -1
    assert arr.find_callable(lambda x: x == -1) == -1


def test_container_iteration_n_is_sorted():
    r = range(0, 100)

    def container_iterate(container: ContainerInterface):
        for i, j in zip(container, r):
            assert container[j] == i
        assert container.is_sorted()

    list = LinkedList()
    for i in r:
        list.push_back(i)
    container_iterate(list)

    deque = Deque()
    for i in r:
        deque.push_back(float(i))
    container_iterate(deque)

    stack = Stack()
    for i in r:
        stack.push(i)
    container_iterate(stack)


def test_container_merge_sort():
    r = range(0, 100)

    list = Array(100)
    for i in r:
        list[i] = random.random()
    list.merge_sort()
    assert list.is_sorted()

    deque = Deque()
    for i in r:
        deque.push_back(random.random())
    deque.merge_sort()
    assert deque.is_sorted()

    queue = Queue()
    for i in r:
        queue.push(random.random())
    queue.merge_sort()
    assert queue.is_sorted()

    stack = Stack()
    for i in r:
        stack.push(random.random())
    stack.merge_sort()
    assert stack.is_sorted()

    list = LinkedList()
    for i in r:
        list.push_back(random.random())
    list.merge_sort()
    assert list.is_sorted()

def test_container_merge_sort():
    r = range(0, 100)

    list = Array(100)
    for i in r:
        list[i] = random.random()
    list.insertion_sort()
    assert list.is_sorted()

    deque = Deque()
    for i in r:
        deque.push_back(random.random())
    deque.insertion_sort()
    assert deque.is_sorted()

    queue = Queue()
    for i in r:
        queue.push(random.random())
    queue.insertion_sort()
    assert queue.is_sorted()

    stack = Stack()
    for i in r:
        stack.push(random.random())
    stack.insertion_sort()
    assert stack.is_sorted()

    list = LinkedList()
    for i in r:
        list.push_back(random.random())
    list.insertion_sort()
    assert list.is_sorted()


def test_container_bubble_sort():
    r = range(0, 100)

    list = LinkedList()
    for _ in r:
        list.push_back(random.random())
    list.bubble_sort()
    assert list.is_sorted()

    deque = Deque()
    for _ in r:
        deque.push_back(random.random())
    deque.bubble_sort()
    assert deque.is_sorted()

    stack = Stack()
    for _ in r:
        stack.push(random.random())
    stack.bubble_sort()
    assert stack.is_sorted()


def test_container_insertion_sort():
    r = range(0, 100)

    list = LinkedList()
    for _ in r:
        list.push_back(random.random())
    list.insertion_sort()
    assert list.is_sorted()

    deque = Deque()
    for _ in r:
        deque.push_back(random.random())
    deque.insertion_sort()
    assert deque.is_sorted()

    stack = Stack()
    for _ in r:
        stack.push(random.random())
    stack.insertion_sort()
    assert stack.is_sorted()


def test_container_bogo_sort():
    r = range(0, 4)

    list = LinkedList()
    for _ in r:
        list.push_back(random.random())
    list.bogo_sort()
    assert list.is_sorted()

    deque = Deque()
    for _ in r:
        deque.push_back(random.random())
    deque.bogo_sort()
    assert deque.is_sorted()

    stack = Stack()
    for _ in r:
        stack.push(random.random())
    stack.bogo_sort()
    assert stack.is_sorted()
