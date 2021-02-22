from codecs import open

result_dict = {}
with open('txt_for_6.txt', encoding='utf-8') as file:
    for line in file:
        line = line.split()
        print(line)
        subject = line[0]
        lec, pr, lab = 0, 0, 0
        for el in line:
            if '(л)' in el:
                lec = int(el[:-3])
            elif '(пр)' in el:
                pr = int(el[:-4])
            elif '(лаб)' in el:
                lab = int(el[:-5])
            result_dict[subject] = lec + pr + lab
    print(result_dict)
