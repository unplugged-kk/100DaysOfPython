import numbers
import re
from typing import MutableMapping


def multiply(x, y):
    return x * y


result = multiply(3, 4)
print(result)
print(multiply(3, 4))
print(multiply(7, y=5))


def multiplyy(*numbers):
    return numbers


print(multiplyy(1, 2, 3, 4))


def multiplyyy(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiplyyy(4, 5, 6, 7))
