from abc import ABC, abstractmethod

class Customer(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def purchase(self, fruit, count=1):
        pass