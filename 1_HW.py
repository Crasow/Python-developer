from script import salary

hours = int(input('Выработка в часах: '))
rph = int(input('Ставка в час: '))
award =  int(input('Премия: '))
print(salary(hours, rph, award))
