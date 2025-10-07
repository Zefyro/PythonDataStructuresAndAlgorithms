from src.container import ContainerInterface
from src.linked_list import LinkedList
from src.deque import Deque
from src.stack import Stack


def test_container_iteration_n_is_sorted():
    r = range(0, 100)

    def container_iterate(container: ContainerInterface):
        for i, j in zip(container, r):
            assert container[i] == j
        assert container.is_sorted()

    list = LinkedList()
    for i in r:
        list.push_back(i)
    container_iterate(list)

    deque = Deque()
    for i in r:
        deque.push_back(i)
    container_iterate(deque)

    stack = Stack()
    for i in r:
        stack.push(i)
    container_iterate(stack)
