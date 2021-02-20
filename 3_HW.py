user_month = int(input('Введи номер месяца: '))
season = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}
while user_month > 12:
    user_month = int(input('Такого месяца нет'))
if user_month == 12 or user_month == 1 or user_month == 2:
    print(season.get(1))
elif user_month == 3 or user_month == 4 or user_month == 5:
    print(season.get(2))
elif user_month == 6 or user_month == 7 or user_month == 8:
    print(season.get(3))
else:
    print(season.get(4))
