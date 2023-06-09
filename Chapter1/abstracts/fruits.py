from abc import ABC, abstractmethod
from datetime import datetime

from containers import Container, Basket, Barrel


class Fruit(ABC):
    def __init__(self, weight: float, date_picked: datetime):
        self.weight = weight
        self.date_picked = date_picked

    @abstractmethod
    def pick(self, container: Container):
        pass


class Orange(Fruit):
    def __init__(self, weight: float, orchard: str, date_picked: datetime, basket: Basket):
        super().__init__(weight, date_picked)
        self.orchard = orchard
        self.basket = basket

    def pick(self, basket: Basket):
        self.basket.add(self)


class Apple(Fruit):
    def __init__(self, weight: float, color: str, date_picked: datetime, barrel: Barrel):
        super().__init__(weight, date_picked)
        self.color = color
        self.barrel = barrel

    def pick(self, barrel: Barrel):
        self.barrel.add(self)
