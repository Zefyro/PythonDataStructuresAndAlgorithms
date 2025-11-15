from typing import Any, Iterator

from container import ContainerInterface


class Array(ContainerInterface):
    """
    ### An implementation of an array.
    - An array represents a collection of elements, with a predefined size.
    """

    def __init__(self, size: int) -> None:
        self.items: list[Any] = []
        for _ in range(0, size):
            self.items.append(None)

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
