gain = int(input('Выручка: '))
cost = int(input('Издержки:'))
members = int(input('Кол-во сотрудников: '))
if gain > cost:
    earn = gain - cost
    rent = round(earn / gain, 2)
    formembers = earn / members
    print('Бизнесс прибыльный')
    print(f'Рентабельность выручки: {rent} ')
    print(f'На каждого учстника пологается: {formembers}')
else:
    print('Бизнес не прибыльный')
