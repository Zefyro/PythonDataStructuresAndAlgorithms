import pytest

from src._array import Array


def test_array_slicing():
    array = Array(5)
    assert len(array) == 5
    for i in range(5):
        array[i] = i

    assert array[:-1] == [0, 1, 2, 3]
    assert array[:-2] == [0, 1, 2]
    assert array[2:-2] == [2]


def test_initialization():
    array = Array(5)
    assert len(array) == 5
    for i in range(5):
        assert array[i] is None

    assert type(array) == Array


def test_getitem_setitem():
    array = Array(5)
    array[0] = 1
    array[4] = 5
    assert array[0] == 1
    assert array[4] == 5
    assert type(array) == Array


def test_getitem_invalid_index():
    array = Array(5)
    with pytest.raises(IndexError):
        _ = array[5]
    with pytest.raises(IndexError):
        _ = array[-1]

    assert type(array) == Array


def test_setitem_invalid_index():
    array = Array(5)
    with pytest.raises(IndexError):
        array[5] = 1
    with pytest.raises(IndexError):
        array[-1] = 1

    assert type(array) == Array


def test_len():
    array = Array(10)
    assert len(array) == 10


def test_iter():
    array = Array(5)
    for i in range(5):
        array[i] = i

    for i, item in enumerate(array):
        assert item == i

    assert type(array) == Array


def test_datatypes():
    array = Array(5)
    array[0] = 1
    array[1] = 2.5
    array[2] = "three"
    array[3] = [4, 5]
    array[4] = {"six": 6}

    assert array[0] == 1
    assert array[1] == 2.5
    assert array[2] == "three"
    assert array[3] == [4, 5]
    assert array[4] == {"six": 6}
    assert type(array) == Array
