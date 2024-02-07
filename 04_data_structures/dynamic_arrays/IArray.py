from abc import ABCMeta, abstractmethod


class IArray(metaclass=ABCMeta):
    @abstractmethod
    def get(self, index):
        raise NotImplementedError

    @abstractmethod
    def put(self, item):
        raise NotImplementedError

    @abstractmethod
    def get_size(self):
        raise NotImplementedError

    @abstractmethod
    def is_empty(self):
        raise NotImplementedError