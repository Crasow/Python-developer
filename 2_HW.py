list1 = [15, 2, 3, 1, 7, 5, 4, 10]
list2 = [el for num, el in enumerate(list1) if list1[num - 1] < list1[num]]
print(f'Исходный список {list1}')
print(f'Новый список {list2}')