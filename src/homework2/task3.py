my_str = 'fhfh nnn dkls'
list = my_str.replace(' ', '')
list2 = []
for i in list:
    if list.count(i) >= 1:
        if list2.__contains__(i):
            continue
        else:
            list2.append(i)
print(''.join(list2))
