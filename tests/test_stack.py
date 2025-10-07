from src.stack import Stack

def test_push_pop_size():
    """
    Tests the basic push, pop, and size functionality.
    """
    stack: Stack = Stack()
    assert stack.size() == 0

    stack.push("hello")
    stack.push("world")
    assert stack.size() == 2

    assert stack.pop() == "world"
    assert stack.pop() == "hello"
    assert stack.size() == 0


def test_peek_is_empty():
    """
    Tests peek and is_empty functionality.
    """
    stack: Stack = Stack()
    assert stack.is_empty()
    assert stack.peek() == None

    stack.push("test")
    assert not stack.is_empty()
    assert stack.peek() == "test"