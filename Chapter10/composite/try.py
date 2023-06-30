# Demonstrate composite pattern
class Component:
    def __init__(self, name):
        self.name = name

    def traverse(self):
        print(self.name, end=' ')


class Leaf(Component):
    def __init__(self, name):
        Component.__init__(self, name)

    def traverse(self):
        Component.traverse(self)


class Composite(Component):
    def __init__(self, name):
        Component.__init__(self, name)
        self.children = []

    def add(self, child):
        self.children.append(child)

    def remove(self, child):
        self.children.remove(child)

    def traverse(self):
        Component.traverse(self)
        for child in self.children:
            child.traverse()
