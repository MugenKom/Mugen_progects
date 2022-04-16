"""Игра угадай число.
Компьютер сам загадывает и сам угадывает число.
Угадывает при помощи оптимального алгоритма.
"""

import numpy as np


def optimal_predict(number: int = 1) -> int:
    """ Угадываем число при помощи следующего алгоритма:
    
    Оптимальный алгоритм угадывания:
        Положим left_num = 1 и rightt_num = 100.
        Называем число, равное middle = (left_num + right_num) // 2 ;
        Если это число равно задуманному, то мы угадали!;
        Если это число меньше задуманного, то положим left_num = middle + 1
        и продолжим алгоритм;
        Если это число больше задуманного, то положим right_num = middle - 1
        и продолжим алгоритм.
    Функция принимает загаданное число и возвращает число попыток
    
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
        middle = (left_num + right_num) // 2 
    
        if middle > number:
            right_num = middle - 1

        elif middle < number:
            left_num = middle + 1
    
        else:
           break # Конец игры выход из цикла
    return count


def score_game(optimal_predict) -> int:
    """Какое среднее количество попыток нужно алгоритму для угадывания числа 
    за 1000 проходов.
    
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
