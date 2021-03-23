"""# 3 task:  Tuple practice"""

"""# paragraph 1:  list -> tuple"""

lst = ['a', 'b', 'c']
tpl = tuple(lst)
print(tpl)


"""# paragraph 2:  tuple -> list"""

tpl1 = ('a', 'b', 'c')
lst1 = list(tpl1)
print(lst1)


"""# paragraph 3:  appropriation"""

a, b, c = 'a', 2, 'python'
print(a, b, c)


"""# paragraph 4:  tuple with 1 element"""

tpl2 = (1,)
for i in tpl2 + (2, 3):
    print(i)
print(len(tpl2))
