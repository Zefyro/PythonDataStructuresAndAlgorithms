import pytest
from src.balance_tree import BalanceTree

def test_insert_and_search():
    tree = BalanceTree()
    tree.insert(10)
    tree.insert(20)
    tree.insert(30)
    tree.insert(40)
    tree.insert(50)
    tree.insert(25)

    assert tree.search(30) is not None
    assert tree.search(60) is None
    assert tree.root.value == 30

def test_inorder_traversal():
    tree = BalanceTree()
    tree.insert(10)
    tree.insert(20)
    tree.insert(30)
    tree.insert(40)
    tree.insert(50)
    tree.insert(25)
    
    expected = [10, 20, 25, 30, 40, 50]
    assert tree.inorder_traversal() == expected

def test_preorder_traversal():
    tree = BalanceTree()
    tree.insert(10)
    tree.insert(20)
    tree.insert(30)
    tree.insert(40)
    tree.insert(50)
    tree.insert(25)

    expected = [30, 20, 10, 25, 40, 50]
    assert tree.preorder_traversal() == expected

def test_postorder_traversal():
    tree = BalanceTree()
    tree.insert(10)
    tree.insert(20)
    tree.insert(30)
    tree.insert(40)
    tree.insert(50)
    tree.insert(25)

    expected = [10, 25, 20, 50, 40, 30]
    assert tree.postorder_traversal() == expected

def test_delete():
    tree = BalanceTree()
    nodes = [50, 30, 70, 20, 40, 60, 80]
    for node in nodes:
        tree.insert(node)

    tree.delete(20)
    assert tree.inorder_traversal() == [30, 40, 50, 60, 70, 80]
    assert tree.preorder_traversal() == [50, 30, 40, 70, 60, 80]

    tree.delete(30)
    assert tree.inorder_traversal() == [40, 50, 60, 70, 80]
    assert tree.preorder_traversal() == [50, 40, 70, 60, 80]

    tree.delete(50)
    assert tree.inorder_traversal() == [40, 60, 70, 80]
    assert tree.preorder_traversal() == [60, 40, 70, 80]

def test_left_left_case():
    tree = BalanceTree()
    tree.insert(30)
    tree.insert(20)
    tree.insert(10)
    assert tree.root.value == 20
    assert tree.preorder_traversal() == [20, 10, 30]

def test_left_right_case():
    tree = BalanceTree()
    tree.insert(30)
    tree.insert(10)
    tree.insert(20)
    assert tree.root.value == 20
    assert tree.preorder_traversal() == [20, 10, 30]

def test_get_balance_none_node():
    tree = BalanceTree()
    assert tree._get_balance(None) == 0

def test_delete_node_not_node():
    tree = BalanceTree()
    assert tree._delete_node(None, 10) is None

def test_delete_node_right_is_none():
    tree = BalanceTree()
    tree.insert(30)
    tree.insert(20)
    tree.insert(10)
    tree.delete(30)
    assert tree.inorder_traversal() == [10, 20]
    assert tree.preorder_traversal() == [20, 10]

    tree = BalanceTree()
    tree.insert(30)
    tree.insert(20)
    tree.insert(40)
    tree.insert(10)
    tree.delete(40)
    assert tree.inorder_traversal() == [10, 20, 30]
    assert tree.preorder_traversal() == [20, 10, 30]

def test_delete_node_only_left_child():
    tree = BalanceTree()
    tree.insert(30)
    tree.insert(20)
    tree.delete(30)
    assert tree.root.value == 20
    assert tree.inorder_traversal() == [20]
    assert tree.preorder_traversal() == [20]


def test_delete_node_left_left_case_rotation():
    tree = BalanceTree()
    tree.insert(40)
    tree.insert(20)
    tree.insert(50)
    tree.insert(10)
    tree.insert(30)
    tree.delete(50)
    assert tree.root.value == 20
    assert tree.preorder_traversal() == [20, 10, 40, 30]

def test_delete_node_left_right_case_rotation():
    tree = BalanceTree()
    nodes = [40, 20, 50, 10, 30, 25]
    for node in nodes:
        tree.insert(node)
    tree.delete(50)
    assert tree.root.value == 30
    assert tree.preorder_traversal() == [30, 20, 10, 25, 40]

def test_delete_node_right_right_case_rotation():
    tree = BalanceTree()
    nodes = [20, 10, 40, 30, 50, 60]
    for node in nodes:
        tree.insert(node)
    tree.delete(10)
    assert tree.root.value == 40
    assert tree.preorder_traversal() == [40, 20, 30, 50, 60]

def test_delete_node_right_left_case_rotation():
    tree = BalanceTree()
    nodes = [20, 10, 40, 50, 30, 25, 35]
    for node in nodes:
        tree.insert(node)
    tree.delete(10)
    assert tree.root.value == 30
    assert tree.preorder_traversal() == [30, 20, 25, 40, 35, 50]

def test_search_node_less_than_node_value():
    tree = BalanceTree()
    tree.insert(50)
    tree.insert(30)
    tree.insert(70)
    result_node = tree._search_node(tree.root, 30)
    assert result_node is not None
    assert result_node.value == 30

