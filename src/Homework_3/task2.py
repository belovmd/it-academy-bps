"""List practice
Используйте генератор списков чтобы получить следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc'].
Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a'].
Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
Скопируйте список и добавьте в него элемент '2a' так чтобы в исходном списке этого элемента не было.
"""

import copy
list = [a + b for a in 'ab' for b in 'bcd']
print("list = ", list)
list_2 = list[0:6:2]
print("list_2 = ", list_2)
list_3 = [a + b for a in '1234' for b in 'a']
print("list_3 = ", list_3)
del list_3[1]    '#print(list_3.remove('2a')) - не работает'
print("list_3 (delete '2a') = ", list_3)
list_4 = copy.deepcopy(list_3)
print("list_4 = ", list_4)
list_5 = list_4.append('2a')    '# выводит None'
print(list_5)
