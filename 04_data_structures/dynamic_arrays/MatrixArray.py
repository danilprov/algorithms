import ctypes
from IArray import IArray
from FactorArray import FactorArray


class MatrixArray(IArray):
    def __init__(self):
        self.len_row = 3
        self.size = 0
        self.array = FactorArray()

    def get(self, index):
        self._check_index(index)
        index_x = index % self.len_row
        index_y = index // self.len_row
        return self.array.get(index_y)[index_x]

    def get_size(self):
        return self.size

    def put(self, item, index=None):
        if index is not None:
            return ValueError("Put at index doesn't work yet :(")
        if self.size == self.array.get_size() * self.len_row:
            self.array.put([None] * self.len_row)

        index_x = self.size % self.len_row
        index_y = self.size // self.len_row
        self.array.get(index_y)[index_x] = item
        self.size += 1

    def is_empty(self):
        return self.get_size() == 0

    def _check_index(self, index):
        if not 0 <= index < self.get_size():
            raise ValueError(f'Index must be between 0 and {self.get_size() - 1}, {index} was provided.')

    def _print(self):
        for i in range(self.array.get_size()):
            print(" ".join(str(self.array.get(i)[x]) for x in range(len(self.array.get(i)))))
            self.array.list_elements()
            #print('\n')


if __name__ == '__main__':
    import unittest
    from ArrayTest import TestMatrixArray
    """
    put at index is not working for matrix array
    2 tests are failing therefore
    """
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMatrixArray)
    # Run the tests
    unittest.TextTestRunner().run(suite)