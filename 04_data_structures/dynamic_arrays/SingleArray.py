import ctypes
from IArray import IArray


class SingleArray(IArray):
    def __init__(self):
        # “ctype” is library that allows us to access low level C implementations.
        # Here we use it to get instance of array of required size.
        self.array = (ctypes.py_object * 0)()
        # altrenatively we can just use list as a base
        # self.array = [None] * 0

    def get(self, index):
        # normally we should also check if index is between 0 and self.size
        self._check_index(index)
        return self.array[index]

    def put(self, item, index=None):
        self.resize(index)
        if index is None:
            self.array[self.get_size() - 1] = item
        else:
            self._check_index(index)
            self.array[index] = item

    def resize(self, index=None):
        new_array = (ctypes.py_object * (self.get_size() + 1))()
        if not self.is_empty():
            if index is None:
                new_array[:self.get_size()] = self.array[:self.get_size()]
            else:
                new_array[:index] = self.array[:index]
                new_array[index + 1:] = self.array[index:]
        self.array = new_array

    def remove(self, index):
        self._check_index(index)
        element = self.get(index)
        new_array = (ctypes.py_object * (self.get_size() - 1))()
        if not self.is_empty():
            new_array[:index] = self.array[:index]
            new_array[index:] = self.array[index + 1:]
        self.array = new_array

        return element

    def get_size(self):
        return len(self.array)

    def is_empty(self):
        return self.get_size() == 0

    def _check_index(self, index):
        if not 0 <= index < self.get_size():
            raise ValueError(f'Index must be between 0 and {self.get_size() - 1}, {index} was provided.')


if __name__ == '__main__':
    import unittest
    from ArrayTest import TestSingleArray

    suite = unittest.TestLoader().loadTestsFromTestCase(TestSingleArray)
    # Run the tests
    unittest.TextTestRunner().run(suite)
