"""Создайте список ['a', 'b', 'c'] и сделайте из него кортеж."""
abc_list = list(map(chr, range(ord('a'), ord('c')+1)))
print(abc_list)

"""Создайте кортеж ('a', 'b', 'c'), И сделайте из него список"""
abc_tuple = list(tuple(list(map(chr, range(ord('a'), ord('c')+1)))))
print(abc_tuple)

"""Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’."""
abc_tuple = ['a' if item == 'a' else '2' if item == 'b' else 'python' if item == 'c' else item for item in abc_tuple]
print(abc_tuple)

"""Создайте кортеж из одного элемента, чтобы при итерировании по этому элементы
 последовательно выводились значения 1, 2, 3. Убедитесь что len() исходного кортежа возвращает 1."""
tuple_oneel = ([1, 2, 3],)
print(tuple_oneel, len(tuple_oneel))
for item in tuple_oneel[0]:
    print(item)
