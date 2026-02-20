from math import sqrt


def concat(a: int, b: int) -> str:
    return str(a) + str(b)


def needs_indent():
    print("no indent")


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
