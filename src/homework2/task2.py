# Найти самое длинное слово в введенном предложении. Учтите что в предложении есть знаки препинания.
# Подсказки:
# my_string.split([chars]) возвращает список строк.
# len(list) - количество элементов в списке

str_ = input('Введите строку: ')
marks = (',', '.', '!', '?')
for char in str_:
    if char in marks:
        str_new = str_.replace(char, '')
format_str = str_new.split()
counter = 0
for i in format_str:
    if len(i) > counter:
        counter = len(i)
        word = i
print('Самое длинное слово - : ', word)
