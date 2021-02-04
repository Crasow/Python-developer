a = int(input('В первый день'))
b = int(input('В последний'))
day = 0
distance = a
print('Получается так:')
while distance < b:
    day += 1
    print('{}-й день: {:.2f}'.format(day,distance))
    distance = distance * 1.1
day += 1
print('{}-й день: {:.2f}'.format(day,distance))
print('Ответ: на {} день спорстмен пробежал более {} километров'.format(day, b))