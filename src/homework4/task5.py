# Языки
# Каждый из N школьников некоторой школы знает Mi языков.
# Определите, какие языки знают все школьники и языки, которые знает хотя бы один из школьников.
# Входные данные
# Первая строка входных данных содержит количество школьников N.
# Далее идет N чисел Mi, после каждого из чисел идет Mi строк,
# содержащих названия языков, которые знает i-й школьник.
lang1 = {'english', 'russian'}
lang2 = {'english', 'ukrainian', 'russian'}
lang3 = {'english', 'german', 'ukrainian', 'russian'}
all_stud = list(lang1 & lang2 & lang3)
any_stud = set(lang1 | lang2 | lang3)
print(len(all_stud))
for i in all_stud:
    print(i)
print(len(any_stud))
for J in any_stud:
    print(J)
