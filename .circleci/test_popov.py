# test 1
print('Hello, world')

# test 2
# name = input('What is your name?\n)
name = 'john'
print('Hi, %s.' % name)

# test 4
friends = ['john', 'pat', 'gary', 'michael']
for i, name in enumerate(friends):
    print ("iteration {iteration} is {name}".format(iteration=i, name=name))

# test 5
def greet(name):
    print ('Hello', name)

greet('Jack')
greet('Jill')
greet('Bob')

# test 6
parents, babies = (1, 1)
while babies < 100:
    print ('This generation has {0} babies'.format(babies))
    parents, babies = (babies, parents + babies)

# test 7
prices = {'apple': 0.40, 'banana': 0.50}
my_purchase = {
    'apple': 1,
    'banana': 6}
grocery_bill = sum(prices[fruit] * my_purchase[fruit]
                   for fruit in my_purchase)
print ('I owe the grocer $%.2f' % grocery_bill)

# test 8
def max(a, b):
    if a > b:
        return a
    else:
        return b
print(max(5, 3))
