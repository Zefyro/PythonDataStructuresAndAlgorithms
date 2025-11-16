from tree import TreeInterface

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class BalanceTree(TreeInterface):
    def __init__(self):
        self.root = None

    def _height(self, node):
        if not node:
            return 0
        return node.height

    def _update_height(self, node):
        if node:
            node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _get_balance(self, node):
        if not node:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _right_rotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        self._update_height(y)
        self._update_height(x)
        return x

    def _left_rotate(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        self._update_height(x)
        self._update_height(y)
        return y

    def insert(self, value):
        self.root = self._insert_node(self.root, value)

    def _insert_node(self, node, value):
        if not node:
            return Node(value)
        elif value < node.value:
            node.left = self._insert_node(node.left, value)
        else:
            node.right = self._insert_node(node.right, value)

        self._update_height(node)
        balance = self._get_balance(node)

        if balance > 1 and value < node.left.value:
            return self._right_rotate(node)
        if balance < -1 and value > node.right.value:
            return self._left_rotate(node)
        if balance > 1 and value > node.left.value:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        if balance < -1 and value < node.right.value:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def delete(self, value):
        self.root = self._delete_node(self.root, value)

    def _delete_node(self, node, value):
        if not node:
            return node

        if value < node.value:
            node.left = self._delete_node(node.left, value)
        elif value > node.value:
            node.right = self._delete_node(node.right, value)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            temp = self._get_min_value_node(node.right)
            node.value = temp.value
            node.right = self._delete_node(node.right, temp.value)

        self._update_height(node)
        balance = self._get_balance(node)

        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._right_rotate(node)
        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._left_rotate(node)
        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def _get_min_value_node(self, node):
        if node is None or node.left is None:
            return node
        return self._get_min_value_node(node.left)

    def search(self, value):
        return self._search_node(self.root, value)

    def _search_node(self, node, value):
        if node is None or node.value == value:
            return node

        if value < node.value:
            return self._search_node(node.left, value)
        else:
            return self._search_node(node.right, value)