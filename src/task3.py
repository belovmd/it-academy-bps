"""Tuple practice"""
"""Создайте список ['a', 'b', 'c'] и сделайте из него кортеж"""
lst = ['a', 'b', 'c']
tpl = tuple(lst)
print(lst)
print(tpl)

"""Создайте кортеж ('a', 'b', 'c'), и сделайте из него список"""
tpl2 = ('a', 'b', 'c')
lst2 = list(tpl2)
print(tpl2)
print(lst2)

"""Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’"""
lst = ['a', 'b', 'c']
a, b, c = 'a', 2, 'python'
print(a, b, c)

"""Создайте кортеж из одного элемента, чтобы при итерировании по этому
элементы последовательно выводились значения 1, 2, 3. Убедитесь что
len() исходного кортежа возвращает 1"""
b = ([1, 2, 3],)
for i in b:
    for j in i:
        print(j)
print(len(b))
