from codecs import open
from json import dump

profit = []
a = 0
b = 0
avg_profit = 0
profit_dict = {}
avg_dict = {}
with open('txt_for_7.txt', encoding='utf-8') as file:
    for line in file:
        line_list = line.split()
        profit.append(int(line_list[2]) - int(line_list[3]))
        if profit[b] > 0:
            avg_profit += profit[b]
            a += 1
        profit_dict[line_list[0]] = profit[b]
        b += 1
    avg_profit = avg_profit / a
    avg_dict['avg profit'] = int(avg_profit)
    result = [profit_dict, avg_dict]
    print(result)

with open('txt_for_7.json', 'w', encoding='utf-8') as json_file:
    dump(result, json_file)
    # Вроде как и все работает, но с русским json явно не дружит
