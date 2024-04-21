from abc import ABC, abstractmethod


class ITree(ABC):
    @abstractmethod
    def search(self, key):
        NotImplementedError

    @abstractmethod
    def insert(self, element):
        NotImplementedError

    @abstractmethod
    def remove(self, key):
        NotImplementedError
