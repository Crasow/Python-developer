with open('txt_for_2.txt') as file:
    line_count = 0
    file.seek(0)
    file_lines = file.readlines()
    print(f'Кол-во строк: {len(file_lines)}')
    for num, line in enumerate(file_lines):
        line_count += 1
        line_list = line.split()
        print(f'В {line_count}-ой строке {len(line_list)} слов')
