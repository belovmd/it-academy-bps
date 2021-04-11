"""Пары элементов"""
"""Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг
другу. Считается, что любые два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. Входные данные - строка из чисел,
разделенная пробелами. Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар"""

str_num = '4 1 77 22 22 22 22 1'
str_temp = str_num.split(' ')
num = []
total = 0

for i in str_temp:
    num.append(int(i))

for c in range(len(num)):
    current_element = num[c]
    if c + 1 < len(num):
        for g in range(c + 1, len(num)):
            next_element = num[g]
            if next_element == current_element:
                total += 1
        print(total)
        