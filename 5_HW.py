with open('new_file_5.txt', 'w') as new_file:
    new_file.write('5 4 3 2 1 4 6 7 42 3')  # 77

with open('new_file_5.txt') as file:
    line = file.readline()
    line_list = line.split()
    summary = 0
    for el in line_list:
        summary += int(el)
    print(summary)
