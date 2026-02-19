import os, sys


unused_var = 42


def add(a, b):
    return a+b


def long_line():
    return "this is a very long line that should trigger linting rules because it is way beyond typical line length limits used by many linters"


class foo:
    def __init__(self):
        pass
