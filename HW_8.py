# Task_8
import hashlib
s = input('Введите строку: ')
a = set()
for i in range(len(s)):
    if i == 0:
        length = len(s) - 1
    else:
        length = len(s)
    for j in range(length, i, -1):
        a.add(hashlib.sha1(s[i:j].encode('utf-8')).hexdigest())
print('Количество подстрок: ', len(a))
