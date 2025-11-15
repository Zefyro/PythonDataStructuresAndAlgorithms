import pytest
from src.deque import Deque

def test_push_front_pop_front_size():
    deque = Deque()
    assert deque.size() == 0

    deque.push_front("hello")
    deque.push_front("world")
    assert deque.size() == 2

    assert deque.pop_front() == "world"
    assert deque.pop_front() == "hello"
    assert deque.size() == 0
    assert deque.pop_front() == None

def test_push_back_pop_back_size():
    deque = Deque()
    assert deque.size() == 0

    deque.push_back("hello")
    deque.push_back("world")
    assert deque.size() == 2

    assert deque.pop_back() == "world"
    assert deque.pop_back() == "hello"
    assert deque.size() == 0
    assert deque.pop_back() == None

def test_peek_front_is_empty():
    deque = Deque()
    assert deque.is_empty()
    assert deque.peek_front() == None

    deque.push_front("test")
    assert not deque.is_empty()
    deque.push_front("another")
    assert deque.peek_front() == "another"

def test_peek_back_is_empty():
    deque = Deque()
    assert deque.is_empty()
    assert deque.peek_back() == None

    deque.push_back("test")
    assert not deque.is_empty()
    deque.push_back("another")
    assert deque.peek_back() == "another"

def test_mixed_operations():
    deque = Deque()
    deque.push_front(1)
    deque.push_back(2)
    deque.push_front(0)
    deque.push_back(3)

    assert deque.size() == 4
    assert deque.pop_front() == 0
    assert deque.pop_back() == 3
    assert deque.pop_front() == 1
    assert deque.pop_back() == 2
    assert deque.size() == 0

def test_getitem():
    deque = Deque()
    deque.push_back(1)
    deque.push_back(2)
    deque.push_back(3)

    assert deque[0] == 1
    assert deque[1] == 2
    assert deque[2] == 3
    assert deque[-1] == None
    assert deque[3] == None

def test_setitem():
    deque = Deque()
    deque.push_back(1)
    deque.push_back(2)
    deque.push_back(3)
    deque[0] = 0
    deque[1] = 0
    deque[2] = 0

    with pytest.raises(IndexError):
        deque[3] = 0

    assert deque[0] == 0
    assert deque[1] == 0
    assert deque[2] == 0
    assert deque[-1] == None
    assert deque[3] == None

def test_iter():
    deque = Deque()
    items = [1, 2, 3, 4, 5]
    for item in items:
        deque.push_back(item)

    for i, item in enumerate(deque):
        assert item == items[i]

def test_datatypes():
    deque = Deque()
    deque.push_front(1)
    deque.push_back(2.5)
    deque.push_front("three")
    deque.push_back([4, 5])
    deque.push_front({"six": 6})

    assert deque.pop_front() == {"six": 6}
    assert deque.pop_back() == [4, 5]
    assert deque.pop_front() == "three"
    assert deque.pop_back() == 2.5
    assert deque.pop_front() == 1

def test_pop_on_empty_deque():
    deque = Deque()
    assert deque.pop_front() is None
    assert deque.pop_back() is None
    assert deque.pop_front() is None
    assert deque.pop_back() is None

def test_peek_on_empty_deque():
    deque = Deque()
    assert deque.peek_front() is None
    assert deque.peek_back() is None
    assert deque.peek_front() is None
    assert deque.peek_back() is None

def test_large_deque():
    deque = Deque()
    for i in range(1000):
        deque.push_back(i)
    
    assert deque.size() == 1000

    for i in range(500):
        assert deque.pop_front() == i
    
    for i in range(999, 499, -1):
        assert deque.pop_back() == i
    
    assert deque.size() == 0
    assert deque.is_empty()
