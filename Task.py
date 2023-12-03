from abc import ABC, abstractmethod

class ITask(ABC):
    @abstractmethod
    def run(self, input_data):
        pass