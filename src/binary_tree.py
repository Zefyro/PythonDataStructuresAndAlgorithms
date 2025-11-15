from container import ContainerInterface

class Node:
    """A node in a binary tree."""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    """A binary search tree implementation."""

    size = 0

    def __init__(self):
        self.root = None

    def insert(self, value):
        """Inserts a new value into the binary tree."""
        self.size += 1
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursive(current_node.left, value)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursive(current_node.right, value)

    def find(self, value):
        """
        Finds a value in the binary tree.
        Returns True if found, False otherwise.
        """
        return self._find_recursive(self.root, value)

    def _find_recursive(self, current_node, value):
        if current_node is None:
            return False
        if current_node.value == value:
            return True
        elif value < current_node.value:
            return self._find_recursive(current_node.left, value)
        else:
            return self._find_recursive(current_node.right, value)

    def inorder_traversal(self):
        """
        Performs an in-order traversal of the tree.
        Returns a list of values.
        """
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

    def preorder_traversal(self):
        """
        Performs a pre-order traversal of the tree.
        Returns a list of values.
        """
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.value)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    def postorder_traversal(self):
        """
        Performs a post-order traversal of the tree.
        Returns a list of values.
        """
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node, result):
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)
