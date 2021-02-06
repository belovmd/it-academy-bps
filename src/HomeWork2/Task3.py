"""3. Вводится строка. Требуется удалить из нее повторяющиеся символы
и все пробелы. Например, если было введено "abc cde def",
то должно быть выведено "abcdef"."""

input_str = "asddfjjjv cfffcc ffkksdskf fkfjgdd. slk. ffjg"
buffer_str = []
result_str = ""
for char in input_str:
    if not(char in buffer_str or char.isspace()):
        result_str += char
        buffer_str.append(char)
print(result_str)
