import unittest
from BinarySearchTree import BinarySearchTree


class BinarySearchTreeTest(unittest.TestCase):
    def setUp(self):
        self.tree = BinarySearchTree()

    def tearDown(self):
        self.tree.clear()

    def test_insert_random(self):
        values = [4, 7, 1, 9, 5, 3, 2]
        for value in values:
            self.tree.insert(value)
        self.assertEqual("4(1()(3(2)()))(7(5)(9))", self.tree.to_string())

    def test_insert_increasing(self):
        values = [1, 2, 3, 4, 5, 6, 7]
        for value in values:
            self.tree.insert(value)
        self.assertEqual("1()(2()(3()(4()(5()(6()(7))))))", self.tree.to_string())

    def test_remove(self):
        values = [1, 2, 3, 4, 5, 6, 7]
        for value in values:
            self.tree.insert(value)
        self.assertTrue(self.tree.search(3))
        self.tree.remove(3)
        self.assertEqual("1()(2()(4()(5()(6()(7)))))", self.tree.to_string())
        self.assertFalse(self.tree.search(3))


if __name__ == '__main__':
    unittest.main()
