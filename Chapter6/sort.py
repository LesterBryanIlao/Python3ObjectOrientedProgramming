class WeirdSortee:

    def __init__(self, string, number, sort_num=True) -> None:
        self.string = string
        self.number = number
        self.sort_num = sort_num

    def __lt__(self, object):
        if self.sort_num:
            return self.number < object.number
        return self.string < object.string

    def __repr__(self) -> str:
        return f"{self.string}:{self.number}"


a = WeirdSortee('a', 4)
b = WeirdSortee("b", 3)
c = WeirdSortee("c", 2)
d = WeirdSortee("d", 1)
l1 = [a, b, c, d]
l2 = sorted(l1, reverse=True)
l1.sort()
print(l1)
print(l2)
