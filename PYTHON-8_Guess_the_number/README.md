# Проект 0. PYTHON-8. Угадай число

## Оглавление  
[1. Описание проекта](https://github.com/MugenKom/Mugen_progects/blob/main/PYTHON-8_Guess_the_number/README.md#Описание-проекта)  
[2. Какой кейс решаем?](https://github.com/MugenKom/Mugen_progects/blob/main/PYTHON-8_Guess_the_number/README.md#Какой-кейс-решаем)  
[3. Краткая информация о данных](https://github.com/MugenKom/Mugen_progects/blob/main/PYTHON-8_Guess_the_number/README.md#Краткая-информация-о-данных)  
[4. Этапы работы над проектом](https://github.com/MugenKom/Mugen_progects/blob/main/PYTHON-8_Guess_the_number/README.md#Этапы-работы-над-проектом)  
[5. Результат](https://github.com/MugenKom/Mugen_progects/blob/main/PYTHON-8_Guess_the_number/README.md#Результат)    
[6. Выводы](https://github.com/MugenKom/Mugen_progects/blob/main/PYTHON-8_Guess_the_number/README.md#Выводы) 

### Описание проекта    
Угадать загаданное компьютером число за минимальное число попыток.

:arrow_up:[к оглавлению](https://github.com/MugenKom/Mugen_progects/blob/main/PYTHON-8_Guess_the_number/README.md#Оглавление)


### Какой кейс решаем?    
Нужно написать программу, которая угадывает число за минимальное число попыток

**Условия соревнования:**
- Компьютер загадывает целое число от 0 до 100, и нам его нужно угадать. Под «угадать», подразумевается «написать программу, которая угадывает число».
- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.
- Необходимо добиться того, чтобы программа угадывала число меньше, чем за 20 попыток.

**Метрика качества**     
- Результаты оцениваются по среднему количеству попыток при 1000 повторений

**Что практикуем**     
- Учимся писать хороший код на python  
- Учимся работать с IDE
- Учимся работать с GitHub

:arrow_up:[к оглавлению](https://github.com/MugenKom/Mugen_progects/blob/main/PYTHON-8_Guess_the_number/README.md#Оглавление)  


### Краткая информация о данных

**Входные данные:**  
Загаданное компьютером число:  
- тип - int()

**Промежуточные данные:**  
Количество попыток угадывания загаданного числа :
- тип - int()

**Выходные данные:**  
Среднее количество попыток угадывания загаданного за 1000 повторений:
- тип - int()

  
:arrow_up:[к оглавлению](https://github.com/MugenKom/Mugen_progects/blob/main/PYTHON-8_Guess_the_number/README.md#Оглавление)


### Этапы работы над проектом  

[1. Напишем программу game_random.py.](https://github.com/MugenKom/Mugen_progects/blob/main/PYTHON-8_Guess_the_number/game_random.py)
- Компьютер генерирует целое число от 1 до 100.
- Программа сама угадывает загаданное число случайным образом. 
- На экран выводится загаданное число и количество попыток. 

[2. Напишем программу game_hot_cold.py.](https://github.com/MugenKom/Mugen_progects/blob/main/PYTHON-8_Guess_the_number/game_hot_cold.py)   
Программа использует алгоритм угадывания числа "Горячо-Холодно". 
- Компьютер генерирует целое число от 1 до 100.
- Программа сама угадывает загаданное число.  
- Используется алгоритм "Горячо-Холодно":  
        Называем любое целое число predict_number от 1 до 100;  
        Если это число равно задуманному, то мы угадали!;  
        Если нет, то называем любое следующее число, в зависимости от того, больше или меньше predict_number загаданоого числа и продолжаем алгоритм.   
- На экран выводится загаданное число и количество попыток.  

[3. Напишем программу game_optimal.py](https://github.com/MugenKom/Mugen_progects/blob/main/PYTHON-8_Guess_the_number/game_optimal.py)  
Программа использует алгоритм угадывания числа "Бинарный поиск".    
- Компьютер генерирует целое число от 1 до 100.
- Программа сама угадывает загаданное число.
- Используемый алгоритм:   
        Положим left_num = 1 и rightt_num = 100.  
        Называем число, равное middle = (left_num + right_num) // 2;  
        Если это число равно задуманному, то мы угадали!;  
        Если это число меньше задуманного, то положим left_num = middle + 1 и продолжим алгоритм;  
        Если это число больше задуманного, то положим right_num = middle - 1 и продолжим алгоритм.   
- На экран выводится загаданное число и количество попыток. 

[4. Напишем программу evaluation_game_algorithms.py](https://github.com/MugenKom/Mugen_progects/blob/main/PYTHON-8_Guess_the_number/evaluation_game_algorithms.py)  
Данная программа содержит оценочную функцию score_game(), которая определяет среднее количество попыток угадывания числа за 1000 проходов того или иного алгоритма и выводит полученное значение на экран.  
Аргументами данной функции выступают функции random_predict, hot_cold_predict, optimal_predict (также описанные в программе), реализующие три вышеописанных алгоритма.

[5. Запускаем оценочную функцию для каждого из алгоритмов и сравниваем результаты](https://github.com/MugenKom/Mugen_progects/blob/main/PYTHON-8_Guess_the_number/game_jupyter.ipynb)

:arrow_up:[к оглавлению](https://github.com/MugenKom/Mugen_progects/blob/main/PYTHON-8_Guess_the_number/README.md#Оглавление)


### Результаты:  
Результаты работы трёх алгоритмов поиска загаданного числа (Рандомный, "Горячо-Холодно" и "Бинарный поиск"):
 - Алгоритм Рандомный угадывает число в среднем за: 100 попыток.
 - Алгоритм "Горячо-Холодно" угадывает число в среднем за: 7 попыток;
 - Оптимальный алгоритм угадывает число в среднем за: 5 попыток;
 
:arrow_up:[к оглавлению](https://github.com/MugenKom/Mugen_progects/blob/main/PYTHON-8_Guess_the_number/README.md#Оглавление)


### Выводы:  
Наиболее быстрым и эффективным алгоритмом является алгоритм Бинарного поиска, описанный в программе [game_optimal.py](https://github.com/MugenKom/Mugen_progects/blob/main/PYTHON-8_Guess_the_number/game_optimal.py)  
Среднее количество угадываний данного алгоритма равняется 5, что в 1.4 раза лучше, чем у алгоритма Угадывания с коррекцией (Горячо-Хололдно) и в 20 раз лучше рандомного угадывания.

:arrow_up:[к оглавлению](https://github.com/MugenKom/Mugen_progects/blob/main/PYTHON-8_Guess_the_number/README.md#Оглавление)


Если информация по этому проекту покажется вам интересной или полезной, то я буду очень вам благодарна, если отметите репозиторий и профиль ⭐️⭐️⭐️-дами