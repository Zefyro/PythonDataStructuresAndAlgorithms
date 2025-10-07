from typing import Any, Iterator
from .container import ContainerInterface

class Queue(ContainerInterface):
    """
    ### An implementation of a queue.  
    - A queue follows a "first-in, first-out" (FIFO) principle.
    """
    
    def __init__(self) -> None:
        self.items: list[Any] = []
    
    def __iter__(self) -> Iterator[Any]:
        return iter(self.items)
    
    def __getitem__(self, idx: int) -> Any:
        if idx >= self.size() or idx < 0:
            return None
        else:
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