from collections import defaultdict, Counter


def letter_frequency1(sentence: str) -> dict:
    frequencies = {}

    for letter in sentence:
        frequency = frequencies.setdefault(letter, 0)
        frequencies[letter] = frequency + 1

    return frequencies


def letter_frequency2(sentence: str) -> dict:
    frequencies = defaultdict(int)

    for letter in sentence:
        frequencies[letter] += 1

    return frequencies


normDict = letter_frequency1("Hello World")
defDict = letter_frequency2("Hello World")

num_items = 0


def tuple_counter():
    global num_items
    num_items += 1
    return (num_items, [])


d = defaultdict(tuple_counter)
d['a'][1].append("hello")
d['b'][1].append('world')
# print(d)

responses = [
    "chocolate",
    "caramel",
    "strawberry",
    "vanilla",
    "strawberry",
    "vanilla",
]
