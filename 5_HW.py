rating = [7, 5, 3, 3, 2]
print(rating)
user_num = int(input('Введи свое место:'))
pos = 0
for el in rating:
    if user_num > el:
        rating.insert(pos, user_num)
        break
    else:
        pos += 1
        if pos == len(rating):
            rating.append(user_num)
            break
print(rating)
