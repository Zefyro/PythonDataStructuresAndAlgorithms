from typing import Any
from src.container import ContainerInterface
from src.linked_list import LinkedList


class HashMap(ContainerInterface):
    """
    A HashMap implementation that uses chaining with LinkedLists for collision resolution.
    """

    def __init__(self, capacity=10):
        self._capacity = capacity
        self._size = 0
        self._buckets = [LinkedList() for _ in range(self._capacity)]

    def _hash(self, key: Any) -> int:
        """
        Hashes the key to determine the bucket index.
        """
        return hash(key) % self._capacity

    def __setitem__(self, key: Any, value: Any):
        """
        Adds or updates a key-value pair in the hash map.
        """
        index = self._hash(key)
        bucket = self._buckets[index]

        for i, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                bucket[i] = (key, value)
                return

        bucket.push_back((key, value))
        self._size += 1

    def __getitem__(self, key: Any) -> Any:
        """
        Retrieves the value associated with a given key.
        """
        index = self._hash(key)
        bucket = self._buckets[index]

        for existing_key, value in bucket:
            if existing_key == key:
                return value

        raise KeyError(f"Key not found: {key}")

    def __delitem__(self, key: Any):
        """
        Removes a key-value pair from the hash map.
        """
        index = self._hash(key)
        bucket = self._buckets[index]
        
        for i, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                bucket.remove(i)
                self._size -= 1
                return

        raise KeyError(f"Key not found: {key}")

    def __len__(self) -> int:
        """
        Returns the number of items in the hash map.
        """
        return self._size

    def __iter__(self):
        """
        Iterates over the keys in the hash map.
        """
        for bucket in self._buckets:
            for key, _ in bucket:
                yield key
