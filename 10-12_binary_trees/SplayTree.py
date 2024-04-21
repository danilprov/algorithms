from ITree import ITree

class _Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


class SplayTree(ITree):
    def __init__(self, root=None):
        self.root = root

    def insert(self, element):
        key = element
        self.root = self._insert(self.root, key)

    def remove(self, key):
        self.root = self._remove(self.root, key)

    def search(self, key):
        node = self._search(key)
        # if element is found, move it up
        # we cannot move absent element up that's why it is done in 2 steps
        if node:
            self.root = self.move_up(self.root, key)

        return node

    def _search(self, key):
        node = self.root
        while node:
            if node.key == key:
                return node
            if node.key < key:
                node = node.right
            else:
                node = node.left

        return False

    def _insert(self, node, key):
        if node is None:
            return _Node(key)

        if node.key > key:
            node.left = self._insert(node.left, key)
            node = self._right_rotation(node)
        else:
            node.right = self._insert(node.right, key)
            node = self._left_rotation(node)

        return node

    def _remove(self, node, key):
        if node is None:
            return

        if node.key > key:
            node.left = self._remove(node.left, key)
        elif node.key < key:
            node.right = self._remove(node.right, key)
        else:
            # 2 kids
            if node.left and node.right:
                max_left_node = self.find_max(node.left)
                node.key = max_left_node.key
                node.left = self._remove(node.left, max_left_node.key)
            # 1 kid
            elif node.left or node.right:
                node = node.left or node.right
            # 0 kids
            else:
                node = None

        return node

    def find_max(self, node):
        if node is None:
            return None
        if node.right is None:
            return node

        return self.find_max(node.right)

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

    def move_up(self, node, key):
        if node is None:
            return node

        if node.key == key:
            return node

        if key > node.key:
            node.right = self.move_up(node.right, key)
            node = self._left_rotation(node)
        else:
            node.left = self.move_up(node.left, key)
            node = self._right_rotation(node)

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

    def clear(self):
        self.root = None


if __name__ == '__main__':
    node1 = _Node(5)
    node2 = _Node(9)
    node = _Node(7, left=node1, right=node2)
    tree = SplayTree(node)
    print(tree.to_string())
    tree.insert(8)
    print(tree.to_string())
    tree.insert(3)
    tree.insert(12)
    tree.insert(4)
    tree.insert(1)
    print(tree.search(7))
    print(tree.to_string())
    tree.remove(7)
    print(tree.to_string())

    tree2 = SplayTree()
    tree2.insert(30)
    tree2.insert(20)
    tree2.insert(10)
    tree2.insert(40)

    print(tree2.to_string())
    tree2.insert(15)
    print(tree2.to_string())
    tree2.search(30)
    print(tree2.to_string())

    print(tree2.find_max(None))
