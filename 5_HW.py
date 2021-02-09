def my_func():
    answer = 0
    count = 0
    while count == 0:
        my_list = input('Введи строку чисел')
        my_list = my_list.split()               # в list полученные числа
        for el in my_list:                          # проверка на "стоп слово"
            if el != 'stop':
                answer += int(el)
            else:
                count = +1                            # стоп цикла

        print(answer)


my_func()
