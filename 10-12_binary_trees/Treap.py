class _Node:
    def __init__(self, key, priority, left=None, right=None):
        self.key = key
        self.priority = priority
        self.left = left
        self.right = right


class Treap:
    def __init__(self, node=None):
        self.root = node

    def _merge(self, t1, t2):
        if t1 is None or t2 is None:
            return t1 or t2

        if t1.priority < t2.priority:
            m = self._merge(t1, t2.left)
            return _Node(t2.key, t2.priority, m, t2.right)
        else:
            m = self._merge(t1.right, t2)
            return _Node(t1.key, t1.priority, t1.left, m)

    def _split(self, cur_node, key):
        if cur_node is None:
            return cur_node, cur_node

        if cur_node.key < key:
            t1, t2 = self._split(cur_node.right, key)
            return _Node(cur_node.key, cur_node.priority, cur_node.left, t1), t2
        else:
            t1, t2 = self._split(cur_node.left, key)
            return t1, _Node(cur_node.key, cur_node.priority, t2, cur_node.right)

    def insert(self, element):
        node = _Node(element[0], element[1])
        t1, t2 = self._split(self.root, node.key)
        t2 = self._merge(node, t2)
        self.root = self._merge(t1, t2)

    def remove(self, key):
        t1, t2 = self._split(self.root, key)
        _, t2 = self._split(t2, key + 1)
        self.root = self._merge(t1, t2)


if __name__ == '__main__':
    abc = Treap()
    abc.insert((6, 7))
    abc.insert((10, 2))
    abc.insert((14, 1))
    abc.insert((12, 4))
    abc.insert((20, 3))
    abc.insert((15, 6))
    abc.insert((8, 8))
    abc.insert((13, 5))
    abc.remove(13)
    print('a')