from script_6_1 import generator
from script_6_2 import repeat
user_answer = int(input('Если нужно сгенерировать числа: нажмите 1\n'
                        'Если нужно повторить список: нажмите 2 '))
if user_answer == 1:
    print(generator())
else:
    print(repeat())
