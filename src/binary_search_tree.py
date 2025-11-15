class Node:
    """A node in a binary tree."""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    """A binary search tree implementation."""

    def __init__(self):
        self.root = None

    def insert(self, value):
        """
        Inserts a new value into the binary tree.
        Duplicate values are inserted into the right side of the tree.
        """
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
        elif value >= current_node.value:
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

    def delete(self, value):
        """Deletes all occurrences of a value from the tree."""
        self.root = self._delete_all_recursive(self.root, value)

    def _find_min(self, node):
        current = node
        while current.left != None:
            current = current.left
        return current

    def _delete_all_recursive(self, node, value):
        if node is None:
            return None

        node.left = self._delete_all_recursive(node.left, value)
        node.right = self._delete_all_recursive(node.right, value)

        if node.value == value:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            successor = self._find_min(node.right)
            node.value = successor.value
            node.right = self._delete_one_recursive(
                node.right, successor.value)

        return node

    def _delete_one_recursive(self, node, value):
        if value < node.value:
            node.left = self._delete_one_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_one_recursive(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            successor = self._find_min(node.right)
            node.value = successor.value
            node.right = self._delete_one_recursive(node.right, successor.value)
        return node
