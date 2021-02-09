name = input('Имя: ')
surname = input('Фамилия: ')
born_year = input('Год рождения: ')
city = input('Город проживания:')
email = input('Твой email: ')
phone = input('Номер телефона:')


def user(el1, el2, el3, el4, el5, el6):
    print(name, surname, born_year, city, email, phone)


user(el1=name, el2=surname, el3=born_year, el4=city, el5=email, el6=phone)
