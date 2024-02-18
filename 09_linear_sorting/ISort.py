from abc import ABC, abstractmethod


class ISort(ABC):
    def __init__(self, array):
        self.array = array
        self.N = len(array)

    @abstractmethod
    def sort(self):
        NotImplementedError
