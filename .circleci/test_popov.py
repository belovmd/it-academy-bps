#test1
print("Hello, World")

#test2
a, b = 2, 3
print(a**b)

#test3
a=2
b=8
print(b/a)

#test4
friends = ['john', 'pat', 'gary', 'michael']
for i, name in enumerate(friends):
    print ("iteration {iteration} is {name}".format(iteration=i, name=name))

#test4
parents, babies = (1, 1)
while babies < 100:
    print ('This generation has {0} babies'.format(babies))
    parents, babies = (babies, parents + babies)

#test5
def greet(name):
    print ('Hello', name)

greet('Jack')
greet('Jill')
greet('Bob')
