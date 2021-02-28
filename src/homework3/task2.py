import copy
"""# 2 task:  List practice"""

"""# paragraph 1:  generator of list"""

list = [list1 + list2 for list1 in 'ab' for list2 in 'bcd']
print(list)

"""# paragraph 2:  slice"""

list3 = list[0:6:2]
print(list3)

"""# paragraph 3:  generator of list with number """

list4 = [list_num + list_a for list_num in '1234' for list_a in 'a']
print(list4)

"""# paragraph 4:  delete element """

del list4[1]
print(list4)


"""# paragraph 5:  copy and append """

list5 = copy.deepcopy(list4)
list5.append('2a')
print('list4 =', list4, 'newlist =', list5)
