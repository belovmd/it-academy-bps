"""Уникальные элементы в списке
Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
Элементы нужно выводить в том порядке, в котором они встречаются в списке."""

list_num = list('1234324567')
uniq_num = []
for num in list_num:
    if num in uniq_num:
        continue
    else:
        uniq_num.append(num)
print(uniq_num)
