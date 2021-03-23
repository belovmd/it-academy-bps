# Упорядоченный список.
# Дан список целых чисел.
# Требуется переместить все ненулевые элементы в левую часть списка, не меняя их порядок,
# а все нули - в правую часть.
# Порядок ненулевых элементов изменять нельзя, дополнительный список использовать нельзя,
# задачу нужно выполнить за один проход по списку. Распечатайте полученный список.
lst = input().split()
for i in reversed(range(len(lst))):
    if lst[i] == '0':
        lst.append(lst.pop(i))
    else:
        print(lst[i])
print(*lst)
