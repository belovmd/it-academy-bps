# Output
print('Hello, world!')

# Input, assignment
name = input('What is your name?\n')
print('Hi, %s.' % name)

# For loop, built-in enumerate function, new style formatting
friends = ['john', 'pat', 'gary', 'michael']
for i, name in enumerate(friends):
    print("iteration {iteration} is {name}".format(iteration=i, name=name))

# Fibonacci, tuple assignment
parents, babies = (1, 1)
while babies < 100:
    print('This generation has {0} babies'.format(babies))
    parents, babies = (babies, parents + babies)


#  Functions
def greet(name_):
    print('Hello', name_)

    greet('Jack')
    greet('Jill')
    greet('Bob')


# Doctest-based testing
def median(pool):
    """Statistical median to demonstrate doctest.
    >>> median([2, 9, 9, 7, 9, 2, 4, 5, 8])
    6 #change to 7 in order to pass the test
    """
    copy = sorted(pool)
    size = len(copy)
    if size % 2 == 1:
        return copy[int((size - 1) / 2)]
    else:
        return (copy[int(size / 2 - 1)] + copy[int(size / 2)]) / 2


if __name__ == '__main__':
    import doctest

    doctest.testmod()

# Dictionaries, generator expressions
prices = {'apple': 0.40, 'banana': 0.50}
my_purchase = {
    'apple': 1,
    'banana': 6}
grocery_bill = sum(prices[fruit] * my_purchase[fruit]
                   for fruit in my_purchase)
print('I owe the grocer $%.2f' % grocery_bill)
