from abc import ABC, abstractmethod


class ISort(ABC):
    def __init__(self, array):
        self.array = array
        self.N = len(array)
        self.cmp = 0
        self.asg = 0

    @abstractmethod
    def sort(self, left, right):
        NotImplementedError

    def swap(self, i, j):
        self.asg += 3
        x = self.array[i]
        self.array[i] = self.array[j]
        self.array[j] = x

    def more(self, i, j):
        # compare elements by indexes
        self.cmp += 1
        return self.array[i] > self.array[j]

    def moreK(self, i, k):
        # compare elements by index and a value
        self.cmp += 1
        return self.array[i] > k

    def toString(self):
        return f'N:  {self.N} \ncmp: {self.cmp} \nasg: {self.asg}'