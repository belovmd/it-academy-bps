"""2. Найти самое длинное слово в введенном предложении.
Учтите что в предложении есть знаки препинания.
Подсказки:
my_string.split([chars]) возвращает список строк.
len(list) - количество элементов в списке
"""


# st = input('enter string: ').split()
st = ("Верхняя строка не проходит через проверки CircleCI").split()
count = 0
for i in st:
    if len(i) > count:
        count = len(i)
        word = i
print('the longest word is: ', word)
