import unittest
from SingleArray import SingleArray
from VectorArray import VectorArray
from FactorArray import FactorArray
from MatrixArray import MatrixArray


class TestDynamicArray(unittest.TestCase):
    def test_put_and_get(self):
        # Test putting elements into the dynamic array and getting them back
        self.dynamic_array.put(1)
        self.assertEqual(self.dynamic_array.get(0), 1)

        self.dynamic_array.put(2)
        self.assertEqual(self.dynamic_array.get(1), 2)

        self.dynamic_array.put(3, 1)
        self.assertEqual(self.dynamic_array.get(1), 3)

    def test_put_at_end(self):
        # Test putting elements at the end of the dynamic array
        self.dynamic_array.put(1)
        self.dynamic_array.put(2)
        self.assertEqual(self.dynamic_array.get(1), 2)

    def test_put_at_index(self):
        # Test putting elements at a specific index
        self.dynamic_array.put(1)
        self.dynamic_array.put(2)
        self.dynamic_array.put(3, 1)
        self.assertEqual(self.dynamic_array.get(1), 3)

    # def test_invalid_index(self):
    #     # Test handling invalid index
    #     with self.assertRaises(IndexError):
    #         self.dynamic_array.put(1, 10)
    #
    # def test_get_empty_array(self):
    #     # Test getting from an empty array
    #     with self.assertRaises(IndexError):
    #         self.dynamic_array.get(0)


class TestSingleArray(TestDynamicArray):
    def setUp(self):
        self.dynamic_array = SingleArray()

class TestVectorArray(TestDynamicArray):
    def setUp(self):
        self.dynamic_array = VectorArray(10)

class TestFactorArray(TestDynamicArray):
    def setUp(self):
        self.dynamic_array = FactorArray()

class TestMatrixArray(TestDynamicArray):
    def setUp(self):
        self.dynamic_array = MatrixArray()
