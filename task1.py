from random import randint

# функция сортировки
def bubble_sort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(n-1-i):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

# длина массива
N = 15 
# массив
array = [randint(-100, 99) for i in range(N)]
print('Исходный массив: ')
print(array)
print('Отсортированный массив: ')
print(bubble_sort(array))