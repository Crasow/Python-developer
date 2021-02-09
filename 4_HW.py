x = 5
y = -3


def my_func(x, y):
    result = 1                      # для дальнейшого умножения
    while y != 0:                 # умножается столько раз само на себя столько,
        result = result * x    # сколько 1 можно прибавить к y до того, как y станет 0
        y += 1
    result = 1 / result         # финальный штрих
    print(result)


my_func(x, y)
