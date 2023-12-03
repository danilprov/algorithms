import ctypes
from abc import ABCMeta, abstractmethod


class IArray(metaclass=ABCMeta):
    @abstractmethod
    def get(self, index):
        raise NotImplementedError

    @abstractmethod
    def put(self, item):
        raise NotImplementedError

    # @abstractmethod
    # def put(self, item, index):
    #     raise NotImplementedError

    @abstractmethod
    def get_size(self):
        raise NotImplementedError

    @abstractmethod
    def is_empty(self):
        raise NotImplementedError


class SingleArray(IArray):
    def __init__(self):
        # “ctype” is library that allows us to access low level C implementations in python. Here we use it to get
        # instance of array of required size.
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


class VectorArray(IArray):
    def __init__(self, vector):
        self.vector = vector
        self.size = 0
        # “ctype” is library that allows us to access low level C implementations in python. Here we use it to get
        # instance of array of required size.
        self.array = (ctypes.py_object * vector)()
        # altrenatively we can just use list as a base
        # self.array = [None] * vector

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
        new_array = (ctypes.py_object * (self.size + self.vector))()
        if not self.is_empty():
            new_array[:self.get_size()] = self.array[:self.get_size()]
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
            raise ValueError(f'Index must be between 0 and {self.get_size() - 1}, {index} was provided.')


class FactorArray(IArray):
    def __init__(self):
        self.factor = 2
        self.size = 0
        # “ctype” is library that allows us to access low level C implementations in python. Here we use it to get
        # instance of array of required size.
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
            raise ValueError(f'Index must be between 0 and {self.get_size() - 1}, {index} was provided.')


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



if __name__ == "__main__":
    import time

    def testPut(array, total):
        start_time = time.time() * 1000.
        for j in range(0, total):
            array.put(j)

        print(f'{array} + testPut: {total} - {round(time.time() * 1000. - start_time)}')

    def testPutwithIndex(array, total, index=0):
        start_time = time.time() * 1000.
        for j in range(0, total):
            array.put(j, index)

        print(f'{array} + testPutwithIndex: {total} - {round(time.time() * 1000. - start_time)}')

    def testRemove(array, total, index=0):
        start_time = time.time() * 1000.
        for j in range(0, total):
            array.remove(index)

        print(f'{array} + testRemove: {total} - {round(time.time() * 1000. - start_time)}')

    single = SingleArray()
    vector = VectorArray(1000)
    factor = FactorArray()
    matrix = MatrixArray()

    for i in range(1, 6):
        for array in [single, vector, factor, matrix]:
            n = 10**i
            testPut(array, n)

            #testRemove(factor, n)
            #testPutwithIndex(factor, n)

    # testPut(factor, 100)
    # testPut(factor, 1000)
    # testPut(factor, 10000)
    # testPut(factor, 100000)

