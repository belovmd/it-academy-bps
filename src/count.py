print('enter numbers:')
list = input()
list2 = []
for i in list:
    if list.count(i) >= 2:
        if list2.__contains__(i):
            continue
        else:
            list2.append(i)

print(list2)
