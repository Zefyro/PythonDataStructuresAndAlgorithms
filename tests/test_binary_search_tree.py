import pytest
from src.binary_search_tree import BinarySearchTree, Node


def test_insert_and_find():
    tree = BinarySearchTree()
    tree.insert(10)
    tree.insert(3)
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
    tree = BinarySearchTree()
    tree.insert(10)
    tree.insert(3)
    tree.insert(5)
    tree.insert(15)
    tree.insert(3)
    tree.insert(7)
    assert tree.inorder_traversal() == [3, 3, 5, 7, 10, 15]


def test_preorder_traversal():
    tree = BinarySearchTree()
    tree.insert(10)
    tree.insert(5)
    tree.insert(3)
    tree.insert(15)
    tree.insert(3)
    tree.insert(7)
    assert tree.preorder_traversal() == [10, 5, 3, 3, 7, 15]


def test_postorder_traversal():
    tree = BinarySearchTree()
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(3)
    tree.insert(7)
    tree.insert(3)
    assert tree.postorder_traversal() == [3, 3, 7, 5, 15, 10]


def test_empty_tree():
    tree = BinarySearchTree()
    assert tree.find(10) is False
    assert tree.inorder_traversal() == []
    assert tree.preorder_traversal() == []
    assert tree.postorder_traversal() == []


def test_delete_leaf_node():
    tree = BinarySearchTree()
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    tree.delete(15)
    assert tree.inorder_traversal() == [5, 10]


def test_delete_node_with_one_child():
    tree = BinarySearchTree()
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(12)
    tree.delete(15)
    assert tree.inorder_traversal() == [5, 10, 12]


def test_delete_node_with_two_children():
    tree = BinarySearchTree()
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(12)
    tree.insert(17)
    tree.delete(15)
    assert tree.inorder_traversal() == [5, 10, 12, 17]
    assert tree.find(15) is False


def test_delete_root_node():
    tree = BinarySearchTree()
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    tree.delete(10)
    assert tree.inorder_traversal() == [5, 15]
    assert tree.find(10) is False


def test_delete_value_not_in_tree():
    tree = BinarySearchTree()
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    tree.delete(100)
    assert tree.inorder_traversal() == [5, 10, 15]


def test_delete_all_occurrences():
    tree = BinarySearchTree()
    tree.insert(10)
    tree.insert(5)
    tree.insert(10)
    tree.insert(15)
    tree.insert(10)
    assert tree.inorder_traversal() == [5, 10, 10, 10, 15]
    tree.delete(10)
    assert tree.inorder_traversal() == [5, 15]
    assert tree.find(10) is False
    tree.delete(None)

@pytest.fixture
def tree_for_delete_one():
    t = BinarySearchTree()
    t.insert(10)
    t.insert(5)
    t.insert(15)
    t.insert(3)
    t.insert(7)
    t.insert(12)
    t.insert(17)
    return t

def test_delete_one_node_with_no_left_child():
    t = BinarySearchTree()
    t.insert(10)
    t.insert(5)
    t.insert(15)
    t.insert(17)
    
    t.root = t._delete_one_recursive(t.root, 15)
    
    assert t.inorder_traversal() == [5, 10, 17]
    assert t.find(15) is False

def test_delete_one_node_with_no_right_child():
    t = BinarySearchTree()
    t.insert(10)
    t.insert(5)
    t.insert(15)
    t.insert(3)

    t.root = t._delete_one_recursive(t.root, 5)
    
    assert t.inorder_traversal() == [3, 10, 15]
    assert t.find(5) is False

def test_delete_one_node_with_two_children(tree_for_delete_one):
    tree = tree_for_delete_one
    tree.root = tree._delete_one_recursive(tree.root, 10)
    
    assert tree.root.value == 12
    assert tree.inorder_traversal() == [3, 5, 7, 12, 15, 17]
    assert tree.find(10) is False

def test_delete_one_value_in_left_subtree(tree_for_delete_one):
    tree = tree_for_delete_one
    tree.root = tree._delete_one_recursive(tree.root, 3)
    
    assert tree.inorder_traversal() == [5, 7, 10, 12, 15, 17]
    assert tree.find(3) is False

def test_delete_one_value_in_right_subtree(tree_for_delete_one):
    tree = tree_for_delete_one
    tree.root = tree._delete_one_recursive(tree.root, 17)
    
    assert tree.inorder_traversal() == [3, 5, 7, 10, 12, 15]
    assert tree.find(17) is False

def test_delete_leaf_node_one_recursive(tree_for_delete_one):
    tree = tree_for_delete_one
    tree.root = tree._delete_one_recursive(tree.root, 3)
    assert tree.inorder_traversal() == [5, 7, 10, 12, 15, 17]
    assert tree.find(3) is False

def test_delete_nonexistent_node_one_recursive(tree_for_delete_one):
    tree = tree_for_delete_one
    initial_traversal = tree.inorder_traversal()
    with pytest.raises(AttributeError):
        tree.root = tree._delete_one_recursive(tree.root, 99)