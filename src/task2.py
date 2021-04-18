"""1.2.3.4.5. Пункты согласно исходному условию, значит условие некорректно )"""
"""1.Используйте генератор списков чтобы получить следующий:
['ab', 'ac', 'ad', 'bb', 'bc', 'bd']."""
result_list = [item_frst + item_secd for item_frst in 'ab' for item_secd in 'bcd']
print(result_list)

"""2.Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc']."""
print(result_list[::2])

"""3.Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a']"""
result_list = [str(item_frst) + item_secd for item_frst in range(1, 5) for item_secd in ['a']]
print(result_list)

"""4.Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его."""
result_list = [item for item in result_list if item != '2a']
print(result_list)

"""5.Скопируйте список и добавьте в него элемент '2a'
так чтобы в исходном списке этого элемента не было."""
result_list = list(result_list[:2]) + ['2a'] + list(result_list[3:])
print(result_list)
