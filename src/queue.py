from typing import Any, Callable, Iterator

from container import ContainerInterface, _merge_sort_impl


class Queue(ContainerInterface):
    """
    ### An implementation of a queue.
    - A queue follows a "first-in, first-out" (FIFO) principle.
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
        Returns: True if the queue is empty, false otherwise.
        """
        return not self.items

    def push(self, item) -> None:
        """
        Adds the item to the end of the queue.
        """
        self.items.append(item)

    def pop(self) -> Any | None:
        """
        Removes the item at the front of the queue.
        Returns: The item at the front of the queue, or None if the queue is empty.
        """
        if not self.is_empty():
            return self.items.pop(0)
        else:
            None

    def peek(self) -> Any | None:
        """
        Returns: The item at the front of the queue, or None if the queue is empty.
        """
        if not self.is_empty():
            return self.items[0]
        else:
            return None

    def size(self) -> int:
        """
        Returns: The size of the queue.
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
