from typing import Any
from src.container import ContainerInterface


class HashTable(ContainerInterface):
    """
    A basic hash table implementation with chaining for collision resolution.
    """

    def __init__(self, capacity=1024):
        self._capacity = capacity
        self._size = 0
        self.table = [[] for _ in range(self._capacity)]

    def _hash(self, key: Any) -> int:
        """
        A simple hash function.
        """
        return hash(key) % self._capacity

    def __setitem__(self, key: Any, value: Any):
        """
        Adds a key-value pair to the hash table.
        If the key already exists, its value is updated.
        """
        key_hash = self._hash(key)
        bucket = self.table[key_hash]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        self._size += 1

    def __getitem__(self, key: Any) -> Any:
        """
        Retrieves the value associated with a key.
        Raises KeyError if the key is not found.
        """
        key_hash = self._hash(key)
        bucket = self.table[key_hash]

        for k, v in bucket:
            if k == key:
                return v

        raise KeyError(key)

    def __delitem__(self, key: Any):
        """
        Deletes a key-value pair from the hash table.
        Raises KeyError if the key is not found.
        """
        key_hash = self._hash(key)
        bucket = self.table[key_hash]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self._size -= 1
                return

        raise KeyError(key)

    def __len__(self) -> int:
        return self._size

    def __iter__(self):
        for bucket in self.table:
            for key, value in bucket:
                yield key
