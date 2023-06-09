from abc import ABC, abstractmethod

from Chapter1.abstracts.fruits import Orange, Apple


class Container(ABC):
    def __init__(self):
        self.contents = []

    def add(self, fruit):
        self.contents.append(fruit)

    def take(self):
        return self.contents.pop()


class Basket(Container):
    def __init__(self, location: str, oranges: list[Orange] = []):
        super().__init__()
        self.location = location
        self.contents = oranges


class Barrel(Container):
    def __init__(self, location: str, apples: list[Apple] = []):
        super().__init__()
        self.location = location
        self.contents = apples
