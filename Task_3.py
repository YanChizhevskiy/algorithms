# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

size = 10
min_item = 1
max_item = 100

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
print(f'минимальное число {min_num} с индексом {min_ind} меняем с максимальным {max_num} с индексом {max_ind}')
store = a[max_ind]
a[max_ind] = a[min_ind]
a[min_ind] = store
print(a)
