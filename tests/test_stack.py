from src.stack import Stack

def test_push_pop_size():
    stack: Stack = Stack()
    assert stack.size() == 0

    stack.push("hello")
    stack.push("world")
    assert stack.size() == 2

    assert stack.pop() == "world"
    assert stack.pop() == "hello"
    assert stack.size() == 0


def test_peek_is_empty():
    stack: Stack = Stack()
    assert stack.is_empty()

    stack.push("test")
    assert not stack.is_empty()
    assert stack.peek() == "test"
    assert stack.size() == 1

def test_getitem():
    stack: Stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    assert stack[0] == 1
    assert stack[1] == 2
    assert stack[2] == 3
    assert stack[-1] == None
    assert stack[3] == None

def test_iter():
    stack: Stack = Stack()
    items = [1, 2, 3, 4, 5]
    for item in items:
        stack.push(item)

    for i, item in enumerate(stack):
        assert item == items[i]

def test_datatypes():
    stack: Stack = Stack()
    stack.push(1)
    stack.push(2.5)
    stack.push("three")
    stack.push([4, 5])
    stack.push({"six": 6})

    assert stack.pop() == {"six": 6}
    assert stack.pop() == [4, 5]
    assert stack.pop() == "three"
    assert stack.pop() == 2.5
    assert stack.pop() == 1

def test_pop_on_empty_stack():
    stack: Stack = Stack()
    assert stack.pop() is None
    assert stack.pop() is None
    assert stack.pop() is None

def test_peek_on_empty_stack():
    stack: Stack = Stack()
    assert stack.peek() is None
    assert stack.peek() is None
    assert stack.peek() is None

def test_large_stack():
    stack: Stack = Stack()
    for i in range(1000):
        stack.push(i)
    
    assert stack.size() == 1000

    for i in range(999, -1, -1):
        assert stack.pop() == i
    
    assert stack.size() == 0
    assert stack.is_empty()
