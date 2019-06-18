# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random
import cProfile
import timeit


size = 100000000
min_item = 1
max_item = 10000000
a = [random.randint(min_item, max_item) for _ in range(size)]
# print(f'В массиве {a}')

# Исходный вариант
# def task_3_v1():
#     min_ind = 0
#     max_ind = 0
#     min_num = a[0]
#     max_num = a[0]
#     for i in list(range(size)):
#         if min_num > a[i]:
#             min_num = a[i]
#             min_ind = i
#     for j in list(range(size)):
#         if max_num < a[j]:
#             max_num = a[j]
#             max_ind = j
#     # print(f'минимальное число {min_num} с индексом {min_ind} меняем с максимальным {max_num} с индексом {max_ind}')
#     store = a[max_ind]
#     a[max_ind] = a[min_ind]
#     a[min_ind] = store
#     return (a)
# # cProfile.run('task_3_v1()')
"""
Для size = 100000

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.016    0.016 <string>:1(<module>)
        1    0.016    0.016    0.016    0.016 HW_3_Task_3.py:14(task_3_v1)
        1    0.000    0.000    0.016    0.016 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

Для size = 1000000
 
       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    1    0.000    0.000    0.167    0.167 <string>:1(<module>)
    1    0.167    0.167    0.167    0.167 HW_3_Task_3.py:14(task_3_v1)
    1    0.000    0.000    0.168    0.168 {built-in method builtins.exec}
    1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

Для size = 10000000
 
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    1.810    1.810 <string>:1(<module>)
        1    1.810    1.810    1.810    1.810 HW_3_Task_3.py:14(task_3_v1)
        1    0.000    0.000    1.810    1.810 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

python -m timeit -s "import HW_3" "HW_3.task_3_v1()"
20 loops, best of 5: 16.1 msec per loop для size = 1000000
2 loops, best of 5: 176 msec per loop для size = 1000000
1 loop, best of 5: 1.78 sec per loop для size = 10000000

Выводы: 
Функциональная зависимость вида O(n), 
т.к. 10-кратное уведичение размера массива в 10 раз увеличивает вермя обработки функции.
"""

# # Вариант 2
# def task_3_v2():
#     min_ind = 0
#     max_ind = 0
#     for i in (range(len(a))):
#         if a[i] < a[min_ind]:
#             min_ind = i
#         elif a[i] > a[max_ind]:
#             max_ind = i
# #     print(f'''минимальное число {a[min_ind]} с индексом {min_ind} меняем
# # с максимальным {a[max_ind]} с индексом {max_ind}''')
#     store = a[max_ind]
#     a[max_ind] = a[min_ind]
#     a[min_ind] = store
#     return(a)
# # # cProfile.run('task_3_v2()')

"""
Для size = 100000

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.020    0.020 <string>:1(<module>)
        1    0.020    0.020    0.020    0.020 HW_3_Task_3.py:35(task_3_v2)
        1    0.000    0.000    0.020    0.020 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        
Для size = 1000000

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.180    0.180 <string>:1(<module>)
        1    0.180    0.180    0.180    0.180 HW_3_Task_3.py:35(task_3_v2)
        1    0.000    0.000    0.180    0.180 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        
Для size = 10000000

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    1.842    1.842 <string>:1(<module>)
        1    1.842    1.842    1.842    1.842 HW_3_Task_3.py:35(task_3_v2)
        1    0.000    0.000    1.842    1.842 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

python -m timeit -s "import HW_3" "HW_3.task_3_v1()"
10 loops, best of 5: 21.2 msec per loop для size = 100000
2 loops, best of 5: 200 msec per loop для size = 1000000
1 loop, best of 5: 1.99 sec per loop для size = 10000000
Функциональная зависимость вида O(n), 
т.к. 10-кратное уведичение размера массива в 10 раз увеличивает вермя обработки функции 
"""

# # Вариант 3
def task_3_v3():
    min_num = min(a)
    max_num = max(a)
    min_ind = a.index(min_num)
    max_ind = a.index(max_num)
    a[min_ind], a[max_ind] = a[max_ind], a[min_ind]
    # print(f'минимальное число {min_num} с индексом {min_ind} меняем с максимальным {max_num} с индексом {max_ind}')
    return(a)
# # cProfile.run('task_3_v3()')
"""
Для size = 100000

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.005    0.005 <string>:1(<module>)
        1    0.000    0.000    0.005    0.005 HW_3_Task_3.py:52(task_3_v3)
        1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
        1    0.002    0.002    0.002    0.002 {built-in method builtins.max}
        1    0.002    0.002    0.002    0.002 {built-in method builtins.min}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        2    0.001    0.001    0.001    0.001 {method 'index' of 'list' objects}


Для size = 1000000

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.042    0.042 <string>:1(<module>)
        1    0.000    0.000    0.042    0.042 HW_3_Task_3.py:52(task_3_v3)
        1    0.000    0.000    0.042    0.042 {built-in method builtins.exec}
        1    0.018    0.018    0.018    0.018 {built-in method builtins.max}
        1    0.019    0.019    0.019    0.019 {built-in method builtins.min}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        2    0.006    0.003    0.006    0.003 {method 'index' of 'list' objects}
        
Для size = 10000000
 
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.411    0.411 <string>:1(<module>)
        1    0.000    0.000    0.411    0.411 HW_3_Task_3.py:52(task_3_v3)
        1    0.000    0.000    0.411    0.411 {built-in method builtins.exec}
        1    0.174    0.174    0.174    0.174 {built-in method builtins.max}
        1    0.179    0.179    0.179    0.179 {built-in method builtins.min}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        2    0.058    0.029    0.058    0.029 {method 'index' of 'list' objects}

В отличии от 1-ого и 2-ого вариантов, в 3-ем варианте время также затрачивается обработку методов 'index' 
и 'list', а также встроенные методы "min" и "max", что делает данный алгоритм наименее эффективным.

python -m timeit -s "import HW_3" "HW_3.task_3_v3()"
50 loops, best of 5: 5.5 msec per loop для size = 100000
5 loops, best of 5: 55.4 msec per loop для size = 1000000
1 loop, best of 5: 438 msec per loop для size = 10000000
Функциональная зависимость вида O(n), 
т.к. 10-кратное уведичение размера массива в 10 раз увеличивает вермя обработки функции 
"""

"""
Общие выводы:
Все 3 алгоритма имеют функциональный вид O(n), третий алгоритм является наименее эффективным;
Вопреки ожиданиям 1-й алгоритм с 2 циклами работает быстрее, чем 2-й алгоритм с вложенными условиями. 
"""
