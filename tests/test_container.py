import random

from src.container import ContainerInterface
from src.deque import Deque
from src.linked_list import LinkedList
from src.stack import Stack


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


def test_container_bubble_sort():
    r = range(0, 100)

    def container_iterate(container: ContainerInterface):
        container.bubble_sort()
        assert container.is_sorted()

    list = LinkedList()
    for _ in r:
        list.push_back(random.random())
    container_iterate(list)

    deque = Deque()
    for _ in r:
        deque.push_back(random.random())
    container_iterate(deque)

    stack = Stack()
    for _ in r:
        stack.push(random.random())
    container_iterate(stack)
