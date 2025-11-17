from typing import Any, Callable, Iterator

from container import ContainerInterface, _merge_sort_impl


class Deque(ContainerInterface):
    """
    ### An implementation of a deque.
    - A deque allows adding and removing elements from both the front and back.
    """

    def __init__(self, from_array: list[Any] | None = None) -> None:
        self.items: list[Any] = [] if not from_array else from_array

    def __iter__(self) -> Iterator[Any]:
        return iter(self.items)

    def __getitem__(self, idx: int | slice) -> Any:
        if isinstance(idx, int):
            if idx >= len(self.items) or idx < 0:
                raise IndexError("Index out of range")
            else:
                return self.items[idx]
        else:
            return self.items[idx]

    def __setitem__(self, idx: int, value: Any) -> Any:
        if idx >= self.size() or idx < 0:
            raise IndexError(f"Out of index {idx}")
        self.items[idx] = value
        return self.items[idx]

    def __len__(self) -> int:
        return self.size()

    def is_empty(self) -> bool:
        """
        Returns: True if the deque is empty, false otherwise.
        """
        return not self.items

    def push_front(self, item) -> None:
        """
        Adds the item to the front of the deque.
        """
        self.items.insert(0, item)

    def push_back(self, item) -> None:
        """
        Adds the item to the back of the deque.
        """
        self.items.append(item)

    def pop_front(self) -> Any | None:
        """
        Removes the item at the front of the deque.
        Returns: The item at the front of the deque, or None if the deque is empty.
        """
        if not self.is_empty():
            return self.items.pop(0)
        else:
            None

    def pop_back(self) -> Any | None:
        """
        Removes the item at the back of the deque.
        Returns: The item at the back of the deque, or None if the deque is empty.
        """
        if not self.is_empty():
            return self.items.pop()
        else:
            None

    def peek_front(self) -> Any | None:
        """
        Returns: The item at the front of the deque, or None if the deque is empty.
        """
        if not self.is_empty():
            return self.items[0]
        else:
            return None

    def peek_back(self) -> Any | None:
        """
        Returns: The item at the back of the deque, or None if the deque is empty.
        """
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self) -> int:
        """
        Returns: The size of the deque.
        """
        return len(self.items)

    def merge_sort(self, compare: Callable[[Any, Any], int] | None = None) -> None:
        """
        Sorts a given container, optionally using a user-provided compare function.
        Uses bubble sorting.
        Average time complexity: O(n log n)
        """
        compare = ContainerInterface._default_compare if not compare else compare
        _merge_sort_impl(self.items, compare)
