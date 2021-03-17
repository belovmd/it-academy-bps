"""Найти самое длинное слово в введенном предложении.
Учтите что в предложении есть знаки препинания"""

D = dict()

for i in [",", ".", "!", "?"]:
    S = S.replace(i, "")

for w in S.replace(",", "").replace(".", "").split():
    D[w] = len(w)

max_val = max(D.values())

print("Слова с максимальной длиной: ")

for k, v in D.items():
    if v == max_val:
        print(k)
