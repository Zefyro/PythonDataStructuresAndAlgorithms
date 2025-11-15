import pytest
from src.hash_table import HashTable


def test_hash_table_set_and_get():
    h_table = HashTable()
    h_table["string"] = "example"
    h_table["int"] = 30
    assert h_table["string"] == "example"
    assert h_table["int"] == 30


def test_hash_table_update_value():
    h_table = HashTable()
    h_table["string"] = "example"
    h_table["string"] = "test"
    assert h_table["string"] == "test"


def test_hash_table_delete_item():
    h_table = HashTable()
    h_table["string"] = "example"
    del h_table["string"]
    with pytest.raises(KeyError):
        _ = h_table["string"]


def test_hash_table_key_error():
    h_table = HashTable()
    with pytest.raises(KeyError):
        _ = h_table["non_existent"]
    with pytest.raises(KeyError):
        del h_table["non_existent"]


def test_hash_table_len():
    h_table = HashTable()
    assert len(h_table) == 0
    h_table["a"] = 1
    assert len(h_table) == 1
    h_table["b"] = 2
    assert len(h_table) == 2
    h_table["a"] = 3
    assert len(h_table) == 2
    del h_table["a"]
    assert len(h_table) == 1


def test_hash_table_iter():
    h_table = HashTable()
    items = {"a": 1, "b": 2, "c": 3}
    for k, v in items.items():
        h_table[k] = v
    
    retrieved_keys = list(h_table)
    assert sorted(retrieved_keys) == sorted(items.keys())


def test_hash_table_collision():
    h_table = HashTable(capacity=2) # Small capacity to force a collision
    
    h_table[0] = "zero" 
    h_table["one"] = 1  
    h_table[2] = "two"  
    h_table[3] = "three"
    h_table["four"] = 4

    assert len(h_table) == 5
    assert h_table[0] == "zero"
    assert h_table["one"] == 1
    assert h_table[2] == "two"
    assert h_table[3] == "three"
    assert h_table["four"] == 4

    del h_table[2]
    assert len(h_table) == 4
    with pytest.raises(KeyError):
        _ = h_table[2]
    
    assert h_table[0] == "zero"
    assert h_table["four"] == 4
