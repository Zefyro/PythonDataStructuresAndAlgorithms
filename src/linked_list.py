from typing import Any

from container import ContainerInterface


# Implement doubly linked lists
class LinkedListNode:
    """
    LinkedList's internal node, representing the cell with the element / obj.

    This this how the nodes are connected in to each other.
    [prev_node] --> [THIS NODE] --> [next_node] -> [next_node's next node] ...etc
    """

    obj: Any = None

    next_node: "LinkedListNode | None" = None
    prev_node: "LinkedListNode | None" = None

    def __init__(self, element: Any):
        self.obj = element

    def __str__(self) -> str:
        return f"{self.obj}"

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
    """
    ### Doubly linkedlist container.
    - LinkedLists are excellent for heavy modifications, such as pushing, popping, and inserting.
    - LinkedLists are not good for, storing heavily accessed data, since they're slow to iterate.
    """

    node: LinkedListNode | None = None

    def first(self) -> Any | None:
        """
        Accesses the first available element, if available.
        """

        if self.node:
            return self.node.obj
        return None

    def last(self) -> Any | None:
        """
        Accesses the last available element, if available.
        """

        n = self.last_node()
        if n:
            return n.obj
        return None

    def last_node(self) -> LinkedListNode | None:
        """
        Accesses the last available node, if available.
        Mainly for internal use in the data structure.
        """

        node = self.node
        while node and node.next_node:
            node = node.next_node
        return node

    def nth_node(self, idx: int) -> LinkedListNode | None:
        """
        Accesses the nth node, if available.
        Mainly for internal use in the data structure.
        To access the element instead use indexing `linked_list[0]`
        """

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
        """
        Removes the node at `idx`, if available.
        Returns the removed element, or None.
        """

        n = self.nth_node(idx)
        if n:
            obj = n.obj
            n.remove()
            return obj
        return None

    def insert(self, idx: int, value: Any) -> bool:
        """
        Inserts a node, so that it will be available at `idx`.
        Returns success, may fail if there is no node at `idx-1`.
        """

        n = self.nth_node(idx - 1)
        if n:
            n.add_after(value)
            return True
        return False

    def push_front(self, element: Any) -> None:
        """
        Push an element to the front of the list.
        """

        if not self.node:
            self.node = LinkedListNode(element)
            return

        self.node = self.node.add_before(element)

    def push_back(self, element: Any):
        """
        Push an element to the back of the list
        """

        if not self.node:
            self.node = LinkedListNode(element)
            return

        n = self.last_node()
        assert n, "?"
        n.add_after(element)

    def pop_front(self) -> Any | None:
        """
        Pop an element from the front of the list. Returns the element if available.
        """

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
        """
        Pop an element from the back of the list. Returns the element if available.
        """

        last = self.last_node()
        if not last:
            return None

        element = last.obj
        last.remove()
        return element

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

    def __setitem__(self, idx: int, value: Any) -> Any:
        n = self.nth_node(idx)
        if not n:
            raise IndexError(f"Out of index {idx}!")
        n.obj = value
        return n.obj

    def __len__(self) -> int:
        node = self.node
        num: int = 1 if self.node else 0
        while node and node.next_node:
            node = node.next_node
            num += 1
        return num
