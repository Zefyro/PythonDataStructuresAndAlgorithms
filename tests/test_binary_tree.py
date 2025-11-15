import pytest
from src.binary_tree import BinaryTree


def test_insert_and_find():
    tree = BinaryTree()
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(3)
    tree.insert(7)

    assert tree.find(10) is True
    assert tree.find(5) is True
    assert tree.find(15) is True
    assert tree.find(3) is True
    assert tree.find(7) is True
    assert tree.find(1) is False
    assert tree.find(20) is False


def test_inorder_traversal():
    tree = BinaryTree()
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(3)
    tree.insert(7)
    assert tree.inorder_traversal() == [3, 5, 7, 10, 15]


def test_preorder_traversal():
    tree = BinaryTree()
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(3)
    tree.insert(7)
    assert tree.preorder_traversal() == [10, 5, 3, 7, 15]


def test_postorder_traversal():
    tree = BinaryTree()
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(3)
    tree.insert(7)
    assert tree.postorder_traversal() == [3, 7, 5, 15, 10]


def test_empty_tree():
    tree = BinaryTree()
    assert tree.find(10) is False
    assert tree.inorder_traversal() == []
    assert tree.preorder_traversal() == []
    assert tree.postorder_traversal() == []


def test_recursive_insert():
    tree = BinaryTree()
    tree.insert(5)
    tree.insert(4)
    tree.insert(6)
    tree.insert(6)