import random
from random import randint

def my_median(array, pivot_fn=random.choice):
    n = len(array)
    return quickselect(array, n/2, pivot_fn)

def quickselect(array, k, pivot_fn):
    if len(array) == 1:
        return array[0]
    
    pivot = pivot_fn(array)
    lows = [el for el in array if el < pivot]
    highs = [el for el in array if el > pivot]
    pivots = [el for el in array if el == pivot]

    if k < len(lows):
        return quickselect(lows, k, pivot_fn)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots), pivot_fn)
    
m = 5
N = 2*m + 1
array = [randint(0, 49) for i in range(N)]
print('Исходный массив: ')
print(array)
print('Медиана:')
print(my_median(array))