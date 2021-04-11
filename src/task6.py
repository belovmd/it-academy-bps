"""Упорядоченный список"""
"""Дан список целых чисел. Требуется переместить все ненулевые элементы
в левую часть списка, не меняя их порядок, а все нули - в правую часть.
Порядок ненулевых элементов изменять нельзя, дополнительный список
использовать нельзя, задачу нужно выполнить за один проход по списку.
Распечатайте полученный список"""

list_num = [6, 4, 0, 2, 7, 0, 4, 0, 3, 1, 9]
current_null_index = 0
for i in range(len(list_num)):
    current_num = list_num[i]
    if not current_num == 0 and i < len(list_num):
        current_null_index = i
        for j in range(i + 1, len(list_num)):
            if not list_num[j] != 0:
                temp = list_num[current_null_index]
                list_num[current_null_index] = list_num[j]
                list_num[j] = temp
                current_null_index = j
            print(list_num)
            