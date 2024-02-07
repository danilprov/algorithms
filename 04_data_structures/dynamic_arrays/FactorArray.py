import ctypes
from IArray import IArray


class FactorArray(IArray):
    def __init__(self):
        self.factor = 2
        self.size = 0
        # “ctype” is library that allows us to access low level C implementations in python.
        # Here we use it to get instance of array of required size.
        # self.array = (ctypes.py_object * 10)()
        # altrenatively we can just use list as a base
        self.array = [None] * 10

    def get(self, index):
        self._check_index(index)
        return self.array[index]

    def put(self, item, index=None):
        if self.size == len(self.array):
            self.resize()
        if index is None:
            self.array[self.size] = item
        else:
            self.array[index + 1: self.get_size() + 1] = self.array[index: self.get_size()]
            self.array[index] = item
        self.size += 1

    def resize(self):
        #new_array = (ctypes.py_object * (self.size * self.factor + 1))()
        new_array = [None] * (self.size * self.factor + 1)
        if not self.is_empty():
            new_array[:self.size] = self.array[:self.size]

        self.array = new_array

    def remove(self, index):
        self._check_index(index)
        element = self.get(index)
        if not self.is_empty():
            self.array[index: self.get_size() - 1] = self.array[index + 1: self.get_size()]
        self.size -= 1

        return element

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def list_elements(self):
        """
        list elements of array
        """
        for items in self.array:
            return " ".join(str(self.array[x]) for x in range(self.size))

    def _check_index(self, index):
        if not 0 <= index < self.get_size():
            raise ValueError(f'Index must be between 0 and {self.get_size() - 1}, '
                             f'{index} was provided.')


if __name__ == '__main__':
    import unittest
    from ArrayTest import TestFactorArray

    suite = unittest.TestLoader().loadTestsFromTestCase(TestFactorArray)
    # Run the tests
    unittest.TextTestRunner().run(suite)