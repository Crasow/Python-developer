number = input('Введи число: ')
result = 0
for i in number:
    if int(i) > int(result):
        result = i
print(f'Наибольшее число: {result}')
