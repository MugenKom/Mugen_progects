"""Игра угадай число.
Компьютер сам загадывает и сам угадывает число.
Угадывает при помощи оптимального алгоритма.
"""

import numpy as np


def optimal_predict(number: int = 1) -> int:
    """ Угадываем число при помощи оптимального алгоритма.
    :arrow_up:[к оглавлению](https://github.com/MugenKom/Mugen_progects/blob/main/PYTHON-8_Guess_the_number/README.md#Оглавление)
    
    

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Количество попыток
    count = 0

    # Левая и правая границы поиска числа
    left_num, right_num = 1, 100

    while True:
        count+=1
        predict_number = (left_num + right_num) // 2 
    
        if predict_number > number:
            right_num = predict_number - 1

        elif predict_number < number:
            left_num = predict_number + 1
    
        else:    
           break # Конец игры выход из цикла
    return count


def score_game(optimal_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        optimal_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # Фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # Загадали список чисел

    for number in random_array:
        count_ls.append(optimal_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score


#if __name__ == "__main__":
    # RUN
score_game(optimal_predict)
