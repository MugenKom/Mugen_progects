"""Игра угадай число.
Компьютер сам загадывает и сам угадывает число.
Угадывает случайным образом.
"""

import numpy as np

number = np.random.randint(1, 101) # Загадываем число

# Количество попыток
count = 0

while True:
    count += 1
    predict_number = np.random.randint(1, 101)  # Предполагаемое число
    
    if number == predict_number:
        print(f"Вы угадали число! Это число = {number}, за {count} попыток")
        break  # Выход из цикла если угадали