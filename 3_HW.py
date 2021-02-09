a = 6
b = 2
c = 10


def my_func(c, b, a):
    my__list = [c,b,a] # 3 аргумента в list
    my__list.remove(min(my__list)) # удаление наименьшого
    answer = my__list[0]+my__list[1] # оставшиеся 2 суммируем
    return answer


print(my_func(a, b, c))
