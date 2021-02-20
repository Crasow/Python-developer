from itertools import count
from math import factorial


def fact():
    for el in count(1):
        yield factorial(el)


num = int(input('Сколько нужно факториалов? '))
x = 0
for el in fact():
    if x < num:
        print(el)
        x += 1
    else:
        break
