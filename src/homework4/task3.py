"""# 3 task:  2 lists with different numbers both 1&2 """

a = [1, 2, 3, 4, 5, 5, 5]
b = [3, 4, 7, 8, 8]
diff_el = 0
for i in a:
    if i in b or a.count(i) != 1:
        continue
    else:
        diff_el += 1
for j in b:
    if j in a or b.count(j) != 1:
        continue
    else:
        diff_el += 1
print(diff_el)
