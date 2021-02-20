from functools import reduce


def func(el1, el2):
    result = el1 * el2
    return result


my_list = [el for el in range(100, 1001) if el % 2 == 0]

print(reduce(func, my_list))
print(len(my_list))
