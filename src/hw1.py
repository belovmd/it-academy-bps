from itertools import groupby

lines = '''
    This is the

    first paragraph.
    This is the second.
    '''.splitlines()
# Use itertools.groupby and bool to return groups of
# consecutive lines that either have content or don't.
for has_chars, frags in groupby(lines, bool):
    if has_chars:
        print(' '.join(frags))
# PRINTS:
# This is the first paragraph.
# This is the second.
print('Hello, world!')

parents, babies = (1, 1)
while babies < 100:
    print('This generation has {0} babies'.format(babies))
    parents, babies = (babies, parents + babies)

friends = ['john', 'pat', 'gary', 'michael']
for i, name in enumerate(friends):
    print("iteration {iteration} is {name}".format(iteration=i, name=name))

name = input('What is your name?\n')
print('Hi, %s.' % name)


def greet(name):
    print('Hello', name)


greet('Jack')
greet('Jill')
greet('Bob')

REFRAIN = '''
    %d bottles of beer on the wall,
    %d bottles of beer,
    take one down, pass it around,
    %d bottles of beer on the wall!
    '''
bottles_of_beer = 9
while bottles_of_beer > 1:
    print(REFRAIN % (bottles_of_beer, bottles_of_beer,
                         bottles_of_beer - 1))
        bottles_of_beer -= 1


prices = {'apple': 0.40, 'banana': 0.50}
my_purchase = {
    'apple': 1,
    'banana': 6}
grocery_bill = sum(prices[fruit] * my_purchase[fruit]
                   for fruit in my_purchase)
print('I owe the grocer $%.2f' % grocery_bill)
