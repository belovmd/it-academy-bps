"""Даны два списка чисел. Посчитайте, сколько различных
чисел входит только в один из этих списков"""
list_first = ('12 83 7 46 6 5 9 0 3').split()
list_secon = ('28 9').split()
print(list(set(list_first) - set(list_secon)))