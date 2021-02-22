rus_dict = {'Один ': 'One', 'Два ': 'Two', 'Три ': 'Three', 'Четыре ': 'Four'}
split_line = []
with open('txt_for_4.txt') as file:
    for line in file:
        split_line.append(line.split(' ', 1))
    print(split_line)
    for key, value in rus_dict.items():
        for line in split_line:
            if value == line[0]:
                line[0] = key


with open('new_txt_for_4.txt', 'w') as new_file:
    for line in split_line:
        new_file.writelines(line)
