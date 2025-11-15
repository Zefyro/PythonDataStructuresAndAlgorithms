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

    # Base container algorithms
    def sort(self, compare: Callable[[Any, Any], int] | None = None):
        assert False, "Todo"

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
        if compare == None:
            compare = lambda ob1, ob2: ob1 - ob2

        for i in range(1, len(self)):
            score = compare(self[i - 1], self[i])
            if score > 0:
                return False

        return True
