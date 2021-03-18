# 3. Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
# Например, если было введено "abc cde def", то должно быть выведено "abcdef"
st = input()
st_new = ''
for i in st:
    if i not in st_new and i != ' ':
        st_new += i
print(st_new)
