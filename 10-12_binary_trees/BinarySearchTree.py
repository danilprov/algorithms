from ITree import ITree


class _Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


class BinarySearchTree(ITree):
    def __init__(self, root=None):
        if root is None:
            self.height = 0
        else:
            self.height = self._get_node_height(root)
        self.root = root

    def insert(self, element):
        key = element
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

    def _insert(self, node, key):
        if node is None:
            return _Node(key)

        if key > node.key:
            node.right = self._insert(node.right, key)
        elif key < node.key:
            node.left = self._insert(node.left, key)

        # Return the (unchanged) node pointer
        return node

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

        return node

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

    def clear(self):
        self.root = None

    def to_string(self):
        return self._to_string(self.root)

    def _to_string(self, node):
        if node is None:
            return ""

        string_tree = ""
        string_tree += str(node.key)

        # if there are no children
        if node.left is None and node.right is None:
            return string_tree

        # for left subtree
        string_tree += '('
        string_tree += self._to_string(node.left)
        string_tree += ')'

        # for right subtree
        # only if right child is present to avoid extra parenthesis
        string_tree += '('
        if node.right is not None:
            string_tree += self._to_string(node.right)
        string_tree += ')'

        return string_tree


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

    n = 15000
    for shuffle in [True, False]:
        tree = BinarySearchTree()
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

#  shuffle True
# insert: time spent - 151 ms
# search: time spent - 72 ms
# remove: time spent - 66 ms
#  shuffle False
# insert: time spent - 41689 ms
# search: time spent - 22775 ms
# remove: time spent - 22875 ms
