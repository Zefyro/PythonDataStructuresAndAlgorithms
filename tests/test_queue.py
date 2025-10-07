from src.queue import Queue

def test_push_pop_size():
    queue = Queue()
    assert queue.size() == 0

    queue.push("hello")
    queue.push("world")
    assert queue.size() == 2

    assert queue.pop() == "hello"
    assert queue.pop() == "world"
    assert queue.size() == 0


def test_peek_is_empty():
    queue = Queue()
    assert queue.is_empty()

    queue.push("test")
    assert not queue.is_empty()
    queue.push("another")
    assert queue.peek() == "test"
    assert queue.size() == 2


def test_getitem():
    queue = Queue()
    queue.push(1)
    queue.push(2)
    queue.push(3)

    assert queue[0] == 1
    assert queue[1] == 2
    assert queue[2] == 3
    assert queue[-1] == None
    assert queue[3] == None

def test_iter():
    queue = Queue()
    items = [1, 2, 3, 4, 5]
    for item in items:
        queue.push(item)

    for i, item in enumerate(queue):
        assert item == items[i]

def test_datatypes():
    queue = Queue()
    queue.push(1)
    queue.push(2.5)
    queue.push("three")
    queue.push([4, 5])
    queue.push({"six": 6})

    assert queue.pop() == 1
    assert queue.pop() == 2.5
    assert queue.pop() == "three"
    assert queue.pop() == [4, 5]
    assert queue.pop() == {"six": 6}

def test_pop_on_empty_queue():
    queue = Queue()
    assert queue.pop() is None
    assert queue.pop() is None
    assert queue.pop() is None

def test_peek_on_empty_queue():
    queue = Queue()
    assert queue.peek() is None
    assert queue.peek() is None
    assert queue.peek() is None

def test_large_queue():
    queue = Queue()
    for i in range(1000):
        queue.push(i)
    
    assert queue.size() == 1000

    for i in range(1000):
        assert queue.pop() == i
    
    assert queue.size() == 0
    assert queue.is_empty()
