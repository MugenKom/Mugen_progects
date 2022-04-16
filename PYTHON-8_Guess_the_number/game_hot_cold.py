"""Игра угадай число.
Компьютер генерирует число и сам угадывает его.

Используется алгоритм "Горячо-Холодно":
        Называем любое целое число predict_number от 1 до 100;
        Если это число равно задуманному, то мы угадали!;
        Если нет, то называем любое следующее число, в зависимости от того,
        больше или меньше predict_number загаданоого числа
        и продолжаем алгоритм. """

import numpy as np

number = np.random.randint(1, 101) # Загадываем число

# Количество попыток
count = 0

# Левая и правая границы поиска числа
left_num, right_num = 1, 101

while True:
    count+=1
    predict_number = np.random.randint(left_num, right_num)  # Предполагаемое число
    
    if predict_number > number:
        right_num = predict_number

    elif predict_number < number:
        left_num = predict_number + 1
    
    else:
        print(f"Вы угадали число! Это число = {number}, за {count} попыток")
        break # Конец игры выход из цикла
