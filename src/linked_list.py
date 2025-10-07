from container import ContainerInterface
from typing import Any


# Implement doubly linked lists
class LinkedListNode:
    obj: Any = None

    next_node: "LinkedListNode | None" = None
    prev_node: "LinkedListNode | None" = None

    def __init__(self, element: Any):
        self.obj = element

    def remove(self) -> None:
        # Patch
        if self.prev_node:
            self.prev_node.next_node = self.next_node
        if self.next_node:
            self.next_node.prev_node = self.prev_node
        self.obj = None

    def add_after(self, element: Any) -> "LinkedListNode":
        n = LinkedListNode(element)

        n.prev_node = self
        n.next_node = self.next_node

        if self.next_node:
            self.next_node.prev_node = n
        self.next_node = n

        return n

    def add_before(self, element: Any) -> "LinkedListNode":
        n = LinkedListNode(element)
        n.prev_node = self.prev_node
        n.next_node = self

        if self.prev_node:
            self.prev_node.next_node = n
        self.prev_node = n
        return n


class LinkedList(ContainerInterface):
    node: LinkedListNode | None = None

    def __iter__(self):
        node = self.node
        while node:
            yield node.obj
            node = node.next_node

    def __getitem__(self, idx: int) -> Any | None:
        n = self.nth_node(idx)
        if n:
            return n.obj
        return None

    def first(self) -> Any | None:
        if self.node:
            return self.node.obj
        return None

    def last(self) -> Any | None:
        n = self.last_node()
        if n:
            return n.obj
        return None

    def length(self) -> int:
        node = self.node
        num: int = 1 if self.node else 0
        while node and node.next_node:
            node = node.next_node
            num += 1
        return num

    def first_node(self) -> LinkedListNode | None:
        return self.node

    def last_node(self) -> LinkedListNode | None:
        node = self.node
        while node and node.next_node:
            node = node.next_node
        return node

    def nth_node(self, idx: int) -> LinkedListNode | None:
        if idx < 0:
            return None

        node = self.node
        if not node:
            return None

        for _i in range(0, idx):
            if node:
                node = node.next_node

        return node

    def remove(self, idx: int) -> Any | None:
        n = self.nth_node(idx)
        if n:
            obj = n.obj
            n.remove()
            return obj
        return None

    def insert(self, value: Any, idx: int) -> bool:
        n = self.nth_node(idx - 1)
        if n:
            n.add_after(value)
            return True
        return False

    def push_front(self, element: Any) -> None:
        if not self.node:
            self.node = LinkedListNode(element)
            return

        self.node = self.node.add_before(element)

    def push_back(self, element: Any):
        if not self.node:
            self.node = LinkedListNode(element)
            return

        n = self.last_node()
        assert n, "?"
        n.add_after(element)

    def pop_front(self) -> Any | None:
        if not self.node:
            return None

        # Store element, since we're going to delete the source node
        element = self.node.obj

        # Delete the source node, and store the one after.
        to_remove = self.node
        self.node = to_remove.next_node
        to_remove.remove()

        return element

    def pop_back(self) -> Any | None:
        last = self.last_node()
        if not last:
            return None

        element = last.obj
        last.remove()
        return element
