import random
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

    def bogo_sort(self, compare: Callable[[Any, Any], int] | None = None):
        if not compare:
            compare = ContainerInterface._default_compare

        # Not sorted? Shuffle:
        while not self.is_sorted(compare):
            self.shuffle()

    def shuffle(self):
        """
        Shuffles the contents of the array, in to a random order.
        Based on the: Fisher–Yates shuffle
        """

        n = len(self)
        for i in reversed(range(n)):
            j = random.randint(0, n - i - 1)
            self[j], self[i] = self[i], self[j]

    def find(self, to_find: Any) -> int:
        """
        Linearly searches the container for an object. If found, index is returned.
        If not found, `-1` is returned
        """
        for i, obj in enumerate(self):
            if obj == to_find:
                return i
        return -1

    def find_callable(self, find_fn: Callable[[Any], bool]) -> int:
        """
        Linearly iterates over the container, calling the find_fn on each element.
        When find_fn returns `true` the iteration is stopped and the index is returned.
        If not matches were found `-1` is returned.
        """
        for i, obj in enumerate(self):
            if find_fn(obj):
                return i
        return -1

    def find_binary(
        self, to_find: Any, compare: Callable[[Any, Any], int] | None = None
    ) -> int:
        """
        Binary search an object, optionally passing a compare function.
        The container has to be sorted for binary search to work!
        If the object is found, then it's index is returned, otherwise `-1` is returned.
        """

        if not compare:
            compare = ContainerInterface._default_compare

        left_hand_side = 0
        right_hand_side = len(self) - 1

        while left_hand_side <= right_hand_side:
            # Middle index
            pivot = (left_hand_side + right_hand_side) // 2
            if self[pivot] == to_find:
                return pivot
            if compare(self[pivot], to_find):
                right_hand_side = pivot - 1
            else:
                left_hand_side = pivot + 1

        return -1

    def is_sorted(self, compare: Callable[[Any, Any], int] | None = None) -> bool:
        """
        Returns true if container is sorted, optionally compared with the compare function.
        """
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
        """
        Default compare functions used for sorting and searching.
        """
        return a > b
