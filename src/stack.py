from typing import Any, Iterator
from .container import ContainerInterface

class Stack(ContainerInterface):
    """
    ### An implementation of a stack.  
    - A stack follows a "last-in, first-out" (LIFO) principle.
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
        Returns: True if the stack is empty, false otherwise.
        """
        return not self.items
    
    def push(self, item) -> None:
        """
        Adds the item to the top of the stack.
        """
        self.items.append(item)
    
    def pop(self) -> Any | None:
        """
        Removes the item at the top of the stack.  
        Returns: The item at the top of the stack, or None if the stack is empty.
        """
        if not self.is_empty():
            return self.items.pop()
        else:
            return None
    
    def peek(self) -> Any | None:
        """
        Returns: The item at the top of the queue, or None if the stack is empty.
        """
        if not self.is_empty():
            return self.items[-1]
        else:
            return None
    
    def size(self) -> int:
        """
        Returns: The size of the stack.
        """
        return len(self.items)