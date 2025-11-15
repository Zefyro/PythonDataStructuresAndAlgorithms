import pytest
from src.hash_map import HashMap


def test_hash_map_set_and_get():
    h_map = HashMap()
    h_map["string"] = "example"
    h_map["int"] = 30
    assert h_map["string"] == "example"
    assert h_map["int"] == 30


def test_hash_map_update_value():
    h_map = HashMap()
    h_map["string"] = "example"
    h_map["string"] = "test"
    assert h_map["string"] == "test"


def test_hash_map_delete_item():
    h_map = HashMap()
    h_map["string"] = "example"
    del h_map["string"]
    with pytest.raises(KeyError):
        _ = h_map["string"]


def test_hash_map_key_error():
    h_map = HashMap()
    with pytest.raises(KeyError):
        _ = h_map["non_existent"]
    with pytest.raises(KeyError):
        del h_map["non_existent"]


def test_hash_map_len():
    h_map = HashMap()
    assert len(h_map) == 0
    h_map["a"] = 1
    assert len(h_map) == 1
    h_map["b"] = 2
    assert len(h_map) == 2
    h_map["a"] = 3
    assert len(h_map) == 2
    del h_map["a"]
    assert len(h_map) == 1


def test_hash_map_iter():
    h_map = HashMap()
    items = {"a": 1, "b": 2, "c": 3}
    for k, v in items.items():
        h_map[k] = v
    
    retrieved_keys = list(h_map)
    assert sorted(retrieved_keys) == sorted(items.keys())


def test_hash_map_collision():
    h_map = HashMap(capacity=2) # Small capacity to force a collision
    
    h_map[0] = "zero" 
    h_map["one"] = 1  
    h_map[2] = "two"  
    h_map[3] = "three"
    h_map["four"] = 4

    assert len(h_map) == 5
    assert h_map[0] == "zero"
    assert h_map["one"] == 1
    assert h_map[2] == "two"
    assert h_map[3] == "three"
    assert h_map["four"] == 4

    del h_map[2]
    assert len(h_map) == 4
    with pytest.raises(KeyError):
        _ = h_map[2]
    
    assert h_map[0] == "zero"
    assert h_map["four"] == 4
