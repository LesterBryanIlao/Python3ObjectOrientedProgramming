from abc import ABC, abstractmethod


class Component(ABC):

    @abstractmethod
    def traverse(self):
        pass


class File(Component):
    def __init__(self, name: str, size: int):
        self.__name = name
        self.__size = size

    def size(self) -> int:
        return self.__size


class Folder(Component):
    def __init__(self, name: str, components: list):
        self.__name = name
        self.__components = components

    def size(self) -> int:
        return sum([component.size() for component in self.__components])
