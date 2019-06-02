# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

min_item_a = 2
max_item_a = 9
min_item_b = 2
max_item_b = 99

a = list(range(min_item_a, max_item_a + 1))
b = list(range(min_item_b, max_item_b + 1))
c = [0] * 8

for i in b:
    for j in a:
        if i % j == 0:
            c[j - 2] += 1
i = 0
while i < len(a):
    print(f"Количество чисел от 2 и до 99, которые делятся на {i+2} составляет: {c[i]}")
    i += 1
