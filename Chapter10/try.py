
class UndecoratedObject:

    @staticmethod
    def get():
        return "UndecoratedObject"


class DecoratedObject:

    def __init__(self, undecorated: UndecoratedObject) -> None:
        self.undecorated = undecorated

    def get(self):
        return self.undecorated.get().replace("Undecorated", "Decorated")


print("sdas?dasdas".find("?"))
