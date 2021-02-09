"""2. Найти самое длинное слово в введенном предложении.
Учтите что в предложении есть знаки препинания.
Подсказки:
my_string.split([chars]) возвращает список строк.
len(list) - количество элементов в списке
"""


st = input('Eenter string: ')
marks = (',', '.', '!', '?')
for char in st:
    if char in marks:
        st_new = st.replace(char, '')
format_str = st_new.split()
count = 0
for i in format_str:
    if len(i) > count:
         count = len(i)
         word = i
print('the longest word is: ', word)
