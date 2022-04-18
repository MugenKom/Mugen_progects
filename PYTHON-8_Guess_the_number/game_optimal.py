"""Игра угадай число. 
Компьютер генерирует число и сам угадывает его.

Программа использует алгоритм угадывания числа "Бинарный поиск":
    Положим left_num = 1 и rightt_num = 100.
    Называем число, равное middle = (left_num + right_num) // 2 ;
    Если это число равно задуманному, то мы угадали!;
    Если это число меньше задуманного, то положим left_num = middle + 1
    и продолжим алгоритм;
    Если это число больше задуманного, то положим right_num = middle - 1
    и продолжим алгоритм."""

import numpy as np

number = np.random.randint(1, 101) # Загадываем число

# Количество попыток
count = 0

# Левая и правая границы поиска числа
left_num, right_num = 1, 100

while True:
    count+=1
    middle = (left_num + right_num) // 2 
    
    if middle > number:
        right_num = middle - 1

    elif middle < number:
        left_num = middle + 1
    
    else:
        print(f"Вы угадали число! Это число = {number}, за {count} попыток")
        break # Конец игры выход из цикла
