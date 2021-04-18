"""Пары элементов
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается,
что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар. Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар"""
str_num = '1 1 1'
list_num = [item for item in str_num if item != ' ']
count_pairs = 0
for item_x in range(len(list_num)):
    for item_y in range(item_x + 1, len(list_num)):
        if list_num[item_x] == list_num[item_y]:
            count_pairs += 1
print(count_pairs)
