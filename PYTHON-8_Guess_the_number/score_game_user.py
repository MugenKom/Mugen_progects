"""Игра угадай число.
Компьютер сам загадывает и сам угадывает число.
Угадывает при помощи алгоритма "Горячо-Холодно".
"""

import numpy as np


def optimal_predict(number: int = 1) -> int:
    """ Угадываем число при помощи алгоритма "Горячо-Холодно":
    
    Алгоритм угадывания:
        Называем любое целое число predict_number от 1 до 100;
        Если это число равно задуманному, то мы угадали!;
        Если нет, то называем любое следующее число, в зависимости от того,
        больше или меньше predict_number загаданоого числа
        и продолжаем алгоритм.  
    Функция принимает загаданное число и возвращает число попыток.
    
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
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
