from .container import ContainerInterface

class Stack(ContainerInterface):
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return not self.items
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return self.items
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None
    
    def size(self):
        return len(self.items)