user_str = input('Введи строку: ')
my_list = user_str.split()
word_num = 0
for el in my_list:
    word_num += 1
    if len(el) < 10:
        print(f'{word_num}. {el}')
    else:
        print(f'{word_num}. {el[:10]}')

