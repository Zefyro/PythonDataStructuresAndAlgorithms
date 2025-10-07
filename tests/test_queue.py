from src._queue import Queue

def test_push_pop_size():
    """
    Tests the basic push, pop, and size functionality.
    """
    queue = Queue()
    assert queue.size() == 0

    queue.push("hello")
    queue.push("world")
    assert queue.size() == 2

    assert queue.pop() == "hello"
    assert queue.pop() == "world"
    assert queue.size() == 0
    assert queue.pop() == None


def test_peek_is_empty():
    """
    Tests peek and is_empty functionality.
    """
    queue = Queue()
    assert queue.is_empty()
    assert queue.peek() == None

    queue.push("test")
    assert not queue.is_empty()
    queue.push("another")
    assert queue.peek() == "test"