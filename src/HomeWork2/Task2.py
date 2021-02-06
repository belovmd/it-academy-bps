"""2. Найти самое длинное слово в введенном предложении.
Учтите что в предложении есть знаки препинания.
Подсказки: my_string.split([chars]) возвращает список строк.
len(list) - количество элементов в списке"""

import re

input_str = "fdkjfjd  dlk124fqassjd.   dfkdkjfl, ff dfdhjlk,ff! preved_medvedqa"
pattern_p = r'[,;.,–!]'
format_str = re.sub(pattern_p, " ", input_str)
list_words = format_str.split()
print(list_words)

# V_1
print(max(list_words, key=lambda word_item: len(word_item)))

# V_2
pos_word_max = 0
count = 0
for word in list_words:
    if len(word) > len(list_words[pos_word_max]):
        pos_word_max = count
    count += 1
print(list_words[pos_word_max])
