with open('txt_for_3.txt') as file:
    file_lines = file.readlines()
    salary_sum = 0
    losers = []
    for line in file_lines:
        file_split = line.split()
        if int(file_split[1]) < 20000:
            losers.append(file_split[0])
        salary_sum += int(file_split[1])
    for loser in losers:
        if loser == losers[-1]:
            print(f'{loser}', end=' ')
        else:
            print(f'{loser}', end=', ')
    print('имеют оклад менее 20к')
    print(f'Средняя зарплата в корпорации: {int(salary_sum/len(file_lines))} гривень')
