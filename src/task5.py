"""Каждый из N школьников некоторой школы знает Mi языков. Определите,
какие языки знают все школьники и языки, которые знает хотя бы один из школьников."""
import random
lst_lg = ('engl spani russian poland sweden turkey').split()
pupi = 3
dict = {i: [set(random.choices(lst_lg, k=random.randint(1, len(lst_lg))))] for i in range(0, pupi)}
uniq_lg = set(lst_lg)
for key in dict:
    for value in dict[key]:
        uniq_lg = set(uniq_lg) & set(value)
print("Кол-во языков {} языки {}".format(len(uniq_lg), uniq_lg))
