#В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

size = 10
min_item = 1
max_item = 10

a = list(random.randint(min_item, max_item) for _ in range(size))
print(f'В массиве {a}')
min_num = a[0]
max_num = a[0]
min_ind = 0
max_ind = 0

for i in list(range(size)):
    if min_num > a[i]:
        min_num = a[i]
        min_ind = i
for j in list(range(size)):
    if max_num < a[j]:
        max_num = a[j]
        max_ind = j
print(f'минимальное число {min_num} с индексом {min_ind}; максимальное - {max_num} с индексом {max_ind}')
if min_ind < max_ind:
    a = a[min_ind + 1 : max_ind]
else:
    a = a[max_ind + 1: min_ind]
sum_a = 0
for j in a:
    sum_a += j
print(f'Сумма чисел в массиве между - {sum_a}')