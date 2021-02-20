user_month = int(input('Введи номер месяца: '))
season = ['Зима', 'Весна', 'Лето', 'Осень']
# while user_month > 12:
#     user_month = int(input('Такого месяца нет'))
if user_month == 12 or user_month == 1 or user_month == 2:
    print(season[0])
elif user_month == 3 or user_month == 4 or user_month == 5:
    print(season[1])
elif user_month == 6 or user_month == 7 or user_month == 8:
    print(season[2])
else:
    print(season[3])
