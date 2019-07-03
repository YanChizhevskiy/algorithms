from random import randint

def merge_sort(array):
    array_len = len(array)
    if array_len <= 1:
        return array
    middle_index = int(array_len/2)
    left_part = merge_sort(array[:middle_index])
    right_part = merge_sort(array[middle_index:])
    return merge(left_part, right_part)

def merge(left_part, right_part):
    result = []
    i, j = 0, 0
    while len(left_part) > i and len(right_part) > j:
        if left_part[i] <  right_part[j]:
            result.append(left_part[i])
            i += 1
        else:
            result.append(right_part[j])
            j += 1
    result += left_part[i:]
    result += right_part[j:]
    return result 

# длина массива
N = 15 
# массив
array = [randint(0, 49) for i in range(N)]
print('Исходный массив: ')
print(array)
print('Отсортированный массив: ')
print(merge_sort(array))