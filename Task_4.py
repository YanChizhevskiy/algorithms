# Определить, какое число в массиве встречается чаще всего.

import random

size = 10
min_item = 1
max_item = 5

a = list(random.randint(min_item, max_item) for _ in range(size))
print(a)
a_set = set(a)

most_com = 0
qty_most_com = 0

for i in a_set:
    qty = a.count(i)
    if qty > qty_most_com:
        qty_most_com = qty
        most_com = i

print(most_com)
