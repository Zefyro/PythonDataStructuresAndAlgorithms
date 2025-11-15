from typing import Any, Callable, Iterator


class ContainerInterface:
    """
    ### ContainerInterface
    - Used internally to unify some APIs between all the containers.
    - Allows us to implement algorithms in one place, and so that they work with all the containers
    """

    # IMPLEMENT THESE IN YOUR CONTAINER #
    def __iter__(self) -> Iterator[Any]:
        raise Exception("UNIMPLEMENTED IN YOUR CONTAINER")

    def __len__(self) -> int:
        raise Exception("UNIMPLEMENTED IN YOUR CONTAINER")

    def __getitem__(self, idx: int) -> Any:
        raise Exception("UNIMPLEMENTED IN YOUR CONTAINER")

    def __setitem__(self, idx: int, value: Any) -> Any:
        raise Exception("UNIMPLEMENTED IN YOUR CONTAINER")

    ######################
    # SORTING ALGORITHMS #
    ######################

    # Sort using a custom sorting function.
    #
    def sort(self, compare: Callable[[Any, Any], int] | None = None):
        self.bubble_sort(compare)

    def bubble_sort(self, compare: Callable[[Any, Any], int] | None = None):
        if not compare:
            compare = ContainerInterface._default_compare

        n = len(self)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if not compare(self[j], self[j + 1]):
                    continue
                self[j], self[j + 1] = self[j + 1], self[j]

    def find(self, to_find: Any) -> Any | None:
        for obj in self:
            if obj == to_find:
                return obj
        return None

    def find_callable(self, find_fn: Callable[[Any], bool]) -> Any | None:
        for obj in self:
            if find_fn(obj):
                return obj
        return None

    def find_binary(self, to_find: Any) -> Any | None:
        assert False, "Todo"

    def is_sorted(self, compare: Callable[[Any, Any], int] | None = None) -> bool:
        if not compare:
            compare = ContainerInterface._default_compare

        for i in range(1, len(self)):
            score = compare(self[i - 1], self[i])
            if score > 0:
                return False

        return True

    def __str__(self) -> str:
        if len(self) == 0:
            return "[ ]"

        out_str = "["
        for i in self:
            out_str += f" {i},"
        out_str = out_str[:-1]  # delete ','
        return out_str + " ]"

    def _default_compare(a: Any, b: Any) -> int:
        return a > b
