"""Города
Дан список стран и городов каждой страны. Затем даны названия городов.
Для каждого города укажите, в какой стране он находится."""
list_ctry = []
list_ctry.append(('Russia Moscow Petersburg Novgorod Kaluga').split())
list_ctry.append(('Ukraine Kiev Donetsk Odessa').split())
dic_ctry = {list_ctry[i][0]: list_ctry[i][1:len(list_ctry[i])] for i in range(0, len(list_ctry))}
print(dic_ctry)
finds_ctry = ('Odessa Moscow Novgorod').split()
for key in dic_ctry:
    for item_fnd in finds_ctry:
        if item_fnd in dic_ctry[key]:
            print(key, item_fnd)
