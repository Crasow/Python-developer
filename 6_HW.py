goods_num = int(input('Введите кол-во товаров: '))
goods_list = []
names = []
prices = []
qty = []
unit = []
n = 1
while goods_num >= n:
    goods_dict = {'Название': input('Название'), 'цена': input('цена'), 'кол-во': input('кол-во'), 'ед': input('ед')}
    names.append(goods_dict.get('Название'))
    prices.append(goods_dict.get('цена'))
    qty.append(goods_dict.get('кол-во'))
    unit.append(goods_dict.get('ед'))
    goods_tuple = (n, goods_dict)
    goods_list.append(goods_tuple)
    n += 1

print(goods_list)
analytics = {'название': names, 'цена': prices, 'кол-во': qty, 'ед': unit}
print(f'Аналитика: {analytics}')
