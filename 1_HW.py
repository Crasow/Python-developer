x = int(input('Первое число: '))
y = int(input('Второе число: '))


def division(x, y):
    if y == 0:
        return '(-∞ ; +∞)'
    else:
        return x / y


print(division(x, y))
