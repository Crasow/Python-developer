from itertools import count


def generator():
    my_list = []
    start = int(input('Введите начало отсчета: '))
    stop = int(input('Введите конец отсчета: '))
    for el in count(start):
        if el == stop:
            break
        my_list.append(el)
    return my_list
