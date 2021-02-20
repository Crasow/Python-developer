from itertools import cycle


def repeat():
    count = 0
    my_list = [23, 1, 3, 10, 4, 11]
    result = []
    repeats = int(input('Сколько раз повторить список? '))
    for el in cycle(my_list):
        if count == repeats*len(my_list):
            break
        count += 1
        result.append(el)
    return result
