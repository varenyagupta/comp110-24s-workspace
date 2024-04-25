"""Mutating functions!"""


__author__ = "730567934"


def manual_append(numbers: list[int], num: int) -> None:
    """Appends numbers!"""
    numbers.append(num)


def double(numbers: list[int]) -> None:
    """Indexing numbers!"""
    i = 0
    while i < len(numbers):
        numbers[i] *= 2
        i += 1
x: list[float] = [1.0, 2.0]
y: list[float] = [3.0, 4.0]
y = x
x[0] = 3.0
