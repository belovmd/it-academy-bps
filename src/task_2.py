"""Найти самое длинное слово в введенном предложении.
Учтите что в предложении есть знаки препинания"""

import string
s = input('Введите предложение: ')
for c in string.punctuation:
    s = s.replace(c, "")
str_ = s.split()
count = 0
word = ''
for i in str_:
    if len(i) > count:
        count = len(i)
        word = i
print('Самое длинное слово в предложении это: ', word)
