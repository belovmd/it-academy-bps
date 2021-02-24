# 3. Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
# Например, если было введено "abc cde def", то должно быть выведено "abcdef"
s = input()
str_ = s.replace(' ', '')
s_new = ''
for i in range(len(str_)):
    if s_new.find(str_[i]) == -1:
        s_new += str_[i]
print(s_new)
