"""# 5 task:  unique elements"""

list1 = [1, 2, 3, 3, 5]
list2 = []
for i in list1:
    if list1.count(i) == 1:
        list2.append(i)
print(list2)
