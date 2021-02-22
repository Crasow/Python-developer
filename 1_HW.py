with open('txt_for_1.txt', 'w') as user_file:
    user_line = []
    while user_line != ['\n']:
        user_line = [input('Введи строку, для окончания - пустая строка: ')]
        user_line[0] += '\n'
        user_file.writelines(user_line)
