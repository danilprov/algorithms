class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


class AVLTree:
    def __init__(self, root=None):
        if root is None:
            self.height = 0
        else:
            self.height = self._get_node_height(root)
        self.root = root

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def remove(self, key):
        self.root = self._remove(self.root, key)

    def search(self, key):
        node = self.root

        while node:
            if node.key == key:
                return node
            elif key > node.key:
                node = node.right
            elif key < node.key:
                node = node.left

        return False

    def _left_rotation(self, node):
        if node is None:
            return

        x = node.right
        node.right = x.left
        x.left = node

        return x

    def _right_rotation(self, node):
        if node is None:
            return

        y = node.left
        node.left = y.right
        y.right = node

        return y

    def _rebalance(self, node):
        if node is None:
            return node

        node.left = self._rebalance(node.left)
        node.right = self._rebalance(node.right)

        node_balance = self._get_node_balance(node)
        if node_balance >= 2:
            if self._get_node_balance(node.right) < 0:
                node.right = self._right_rotation(node.right)
            node = self._left_rotation(node)
        elif node_balance <= -2:
            if self._get_node_balance(node.right) > 0:
                node.left = self._left_rotation(node.left)
            node = self._right_rotation(node)

        return node

    def _get_node_balance(self, node):
        if node is None:
            return 0
        else:
            return self._get_node_height(node.right) - self._get_node_height(node.left)

    def _insert(self, node, key):
        if node is None:
            return Node(key)

        if key > node.key:
            node.right = self._insert(node.right, key)
        elif key < node.key:
            node.left = self._insert(node.left, key)

        # Return the (unchanged) node pointer
        return self._rebalance(node)

    def _remove(self, node, key):
        if node is None:
            return node

        if key > node.key:
            node.right = self._remove(node.right, key)
        elif key < node.key:
            node.left = self._remove(node.left, key)
        else:
            # 2 kid
            if node.left and node.right:
                target_node = self._find_max(node.left)
                temp_key = node.key
                node.key = target_node.key
                target_node.key = temp_key
                node.left = self._remove(node.left, temp_key)
            # 0 or 1 kid
            else:
                node = node.left or node.right

        return self._rebalance(node)

    def _find_max(self, node):
        if node is None:
            return None
        if node.right is None:
            return node

        return self._find_max(node.right)

    def _get_node_height(self, node):
        if node is None:
            return -1
        return 1 + max(self._get_node_height(node.left), self._get_node_height(node.right))

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

    def clear(self):
        self.root = None


if __name__ == '__main__':
    import random
    import time
    import numpy as np
    import sys
    sys.setrecursionlimit(100000)

    def create_array(size, shuffle=True):
        array = list(range(size))
        random.seed(123)
        if shuffle:
            random.shuffle(array)
            return array
        else:
            return array

    n = 500
    for shuffle in [True, False]:
        tree = AVLTree()
        start_time = time.time() * 1000.
        array1 = create_array(n, shuffle=shuffle)
        for i in range(n):
            tree.insert(array1[i])
        print(f' shuffle {shuffle}')
        print(f'insert: time spent - {round(time.time() * 1000. - start_time)} ms')

        random_elements = np.random.choice(np.arange(n), size=n//2, replace=False)
        start_time = time.time() * 1000.
        for elem in random_elements:
            tree.search(elem)
        print(f'search: time spent - {round(time.time() * 1000. - start_time)} ms')

        random_elements = np.random.choice(np.arange(n), size=n // 2, replace=False)
        start_time = time.time() * 1000.
        for elem in random_elements:
            tree.remove(elem)
        print(f'remove: time spent - {round(time.time() * 1000. - start_time)} ms')

# n = 500
#  shuffle True
# insert: time spent - 1721 ms
# search: time spent - 2 ms
# remove: time spent - 1411 ms
#  shuffle False
# insert: time spent - 1582 ms
# search: time spent - 1 ms
# remove: time spent - 1203 ms

# n = 1500
#  shuffle True
# insert: time spent - 11037 ms
# search: time spent - 4 ms
# remove: time spent - 8669 ms
#  shuffle False
# insert: time spent - 11091 ms
# search: time spent - 4 ms
# remove: time spent - 8654 ms

# n = 3000
#  shuffle True
# insert: time spent - 87180 ms
# search: time spent - 15 ms
# remove: time spent - 65317 ms
#  shuffle False
# insert: time spent - 85766 ms
# search: time spent - 16 ms
# remove: time spent - 65086 ms
