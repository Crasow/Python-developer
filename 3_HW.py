user_month = int(input('Введи номер месяца: '))
seasons_dict = {'зима': [12, 1, 2], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}
seasons_list = [[12, 1, 2, 'зима'], [3, 4, 5, 'весна'], [6, 7, 8, 'лето'], [9, 10, 11, 'осень']]
print('\nРешение через list\n')

for el in seasons_list:
    if user_month in el:
        print(f'Это {el[3]}')

print('\nРешение через dict\n')

for key, value in seasons_dict.items():
    if user_month in value:
        print(f'Это {key}')
