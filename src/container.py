import typing


class ContainerInterface:
    def __iter__(self) -> typing.Iterator[object]:
        assert False, "Todo"

    def __getitem__(self, name: int) -> object:
        assert False, "Todo"

    def sort(self, callable: typing.Callable[[object, object], int]):
        assert False, "Todo"

    def find(self, to_find: object) -> object | None:
        for obj in self:
            if obj == to_find:
                return obj
        return None

    def find_binary(self, to_find: object) -> object | None:
        assert False, "Todo"

    def find_with(self, find_fn: typing.Callable[[object], bool]) -> object | None:
        for obj in self:
            if find_fn(obj):
                return obj
        return None

    def is_sorted(self) -> bool:
        return False
