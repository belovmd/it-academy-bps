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


# Functions
def greet(name_):
    print('Hello', name_)
    greet('Jack')
    greet('Jill')
    greet('Bob')


# Dictionaries, generator expressions
prices = {'apple': 0.40, 'banana': 0.50}
my_purchase = {
    'apple': 1,
    'banana': 6}
grocery_bill = sum(prices[fruit] * my_purchase[fruit]
                   for fruit in my_purchase)
print('I owe the grocer $%.2f' % grocery_bill)


# Classes
class BankAccount(object):
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def overdrawn(self):
        return self.balance < 0


# Doctest-based testing
def median(pool):
    """ Statistical median to demonstrate doctest.
     median([2, 9, 9, 7, 9, 2, 4, 5, 8])
    6 #change to 7 in order to pass the test"""
    copy = sorted(pool)
    size = len(copy)
    if size % 2 == 1:
        return copy[int((size - 1) / 2)]
    else:
        return (copy[int(size / 2 - 1)] + copy[int(size / 2)]) / 2


if __name__ == '__main__':
    import doctest

    doctest.testmod()

# Queens Problem (recursion)
BOARD_SIZE = 8


def under_attack(col, queens_):
    left = right = col

    for r, c in reversed(queens_):
        left, right = left - 1, right + 1

        if c in (left, col, right):
            return True
    return False


def solve(n):
    if n == 0:
        return [[]]

    smaller_solutions = solve(n - 1)

    return [solution + [(n, c + 1)]
            for c in range(BOARD_SIZE)
            for solution in smaller_solutions
            if not under_attack(c + 1, solution)]


for answer in solve(BOARD_SIZE):
    print(answer)

# 8-Queens Problem (define your own exceptions)
BOARD_SIZE = 8


class BailOut(Exception):
    pass


def validate(queens_):
    left = right = col = queens_[-1]
    for r in reversed(queens_[:-1]):
        left, right = left - 1, right + 1
        if r in (left, col, right):
            raise BailOut


def add_queen(queens_):
    for c in range(BOARD_SIZE):
        test_queens = queens_ + [c]
        try:
            validate(test_queens)
            if len(test_queens) == BOARD_SIZE:
                return test_queens
            else:
                return add_queen(test_queens)
        except BailOut:
            pass
    raise BailOut


queens = add_queen([])
print(queens)
print("\n".join(". " * q + "Q " + ". " * (BOARD_SIZE - q - 1) for q in queens))
