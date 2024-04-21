import random
from ITree import ITree


class _Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        self.size = self._get_node_size(self.left) + self._get_node_size(self.right) + 1

    def _get_node_size(self, node):
        if node is None:
            return 0

        result_l = self._get_node_size(node.left)
        result_r = self._get_node_size(node.right)

        return result_l + result_r + 1


class RandTree(ITree):
    def __init__(self, node=None):
        self.root = node

    def insert(self, element):
        key = element
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return _Node(key)

        if random.random() < 1 / (node.size + 1):
            return self._insert_root(node, key)

        if key > node.key:
            node.right = self._insert(node.right, key)
        else:
            node.left = self._insert(node.left, key)

        node.size = node._get_node_size(node)
        return node

    def _insert_root(self, node, key):
        if node is None:
            return _Node(key)

        if key > node.key:
            node.right = self._insert_root(node.right, key)
            node = self._left_rotation(node)
        elif key < node.key:
            node.left = self._insert_root(node.left, key)
            node = self._right_rotation(node)
        else:
            raise ValueError('element already exists')

        return node

    def _left_rotation(self, node):
        x = node.right
        node.right = x.left
        x.left = node

        return x

    def _right_rotation(self, node):
        y = node.left
        node.left = y.right
        y.right = node

        return y

    def _remove(self, node, key):
        if node is None:
            return node

        if key > node.key:
            node.right = self._remove(node.right, key)
        elif key < node.key:
            node.left = self._remove(node.left, key)
        else:
            if node.left and node.right:
                temp_node = self.find_max(node.left)
                node.key = temp_node.key
                node.left = self._remove(node.left, temp_node.key)
            elif node.left or node.right:
                node = node.left or node.right
            else:
                node = None

        return node

    def remove(self, key):
        self.root = self._remove(self.root, key)

    def find_max(self, node):
        if node is None:
            return

        while node.right:
            node = node.right

        return node

    def to_string(self):
        return self._to_string(self.root)

    def _to_string(self, node):
        if node is None:
            return ""

        string_tree = ""
        string_tree += str(node.key)

        if node.left is None and node.right is None:
            return string_tree

        # add left subtree
        string_tree += '('
        string_tree += self._to_string(node.left)
        string_tree += ')'

        # add right subtree (only if right child exists)
        string_tree += '('
        if node.right is not None:
            string_tree += self._to_string(node.right)
        string_tree += ')'

        return string_tree


if __name__ == '__main__':
    random.seed(1)

    node1 = _Node(5, _Node(3))
    node2 = _Node(9, None, _Node(12))
    node = _Node(7, left=node1, right=node2)
    tree = RandTree(node)
    print(tree.root.size)

    tree2 = RandTree()
    for i in range(10):
        tree2.insert(i)
    print(tree2.root.size)
    print(tree2.to_string())