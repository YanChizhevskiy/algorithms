#Задача 1
a = int(input('Введите трехзначное число: '))
b = (a // 100) + ((a // 10) % 10) + (a % 10)
c = (a // 100) * ((a // 10) % 10) * (a % 10)
print(b, c)

#Задача 3
x0 = int(input('координату X0: '))
y0 = int(input('координату Y0: '))
x1 = int(input('координату X1: '))
y1 = int(input('координату Y1: '))
k = (y0 - y1) / (x0 - x1)
b = y1 - k * x1
print(f'y = {k}x + {b}')

#Задача 4
import random
min_int = int(input('Введите нижнюю границу диапазона целых чисел: '))
max_int = int(input('Введите верхнюю границу диапазона целых чисел: '))
rand_int = random.randint(min_int, max_int)
print(rand_int)

min_fl = float(input('Введите нижнюю границу диапазона вещественных чисел: '))
max_fl = float(input('Введите верхнюю границу диапазона вещественных чисел: '))
rand_fl = random.uniform(min_fl, max_fl)
print(rand_fl)

min_ord = ord(input('Введите нижнюю границу диапазона символов: '))
max_ord = ord(input('Введите верхнюю границу диапазона символов: '))
rand_ord = int(random() * (max_ord - min_ord + 1)) + min_ord
print(chr(rand_ord))

#Задача 5
a = ord(input('Введите первую букву: '))
b = ord(input('Введите вторую букву: '))
a = a - ord('a') + 1
b = b - ord('a') + 1
print(f"Позиции введенных букв {a}, {b}")
print(f"Количество символов между буквами {abs(a-b)-1} ")

#Задача 6
n = int(input('Введите номер буквы в алфавите: '))
n = ord('a') + n - 1
print(chr(n))

#Задача 8
x = int(input('Введите год '))
if x % 4 != 0 or (x % 100 == 0 and x % 400 != 0):
    print("Не високосный")
else:
    print("Високосный")