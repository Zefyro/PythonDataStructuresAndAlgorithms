from typing import Any
from .container import ContainerInterface

class Stack(ContainerInterface):
    """
    An implementation of a stack.  
    A stack follows a "last-in, first-out" (LIFO) principle.
    """
    def __init__(self) -> None:
        self.items: list[Any] = []
    
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