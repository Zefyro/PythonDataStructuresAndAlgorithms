from typing import Any, Callable, Iterator

from container import ContainerInterface, _merge_sort_impl


class Array(ContainerInterface):
    """
    ### An implementation of an array.
    - An array represents a collection of elements, with a predefined size.
    """

    def __init__(self, size: int, from_array: list[Any] | None = None) -> None:
        self.items: list[Any] = [] if not from_array else from_array
        if len(self.items) < size:
            for _ in range(len(self.items), size):
                self.items.append(None)
        elif len(self.items) > size:
            self.items = self.items[:size]

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

    def __setitem__(self, idx: int, value: Any) -> None:
        if idx >= len(self.items) or idx < 0:
            raise IndexError("Index out of range")
        else:
            self.items[idx] = value

    def __len__(self) -> int:
        return len(self.items)

    def merge_sort(self, compare: Callable[[Any, Any], int] | None = None) -> None:
        """
        Sorts a given container, optionally using a user-provided compare function.
        Uses bubble sorting.
        Average time complexity: O(n log n)
        """
        compare = ContainerInterface._default_compare if not compare else compare
        _merge_sort_impl(self.items, compare)
