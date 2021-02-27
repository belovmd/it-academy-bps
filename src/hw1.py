# 18 li

BOARD_SIZE = 8  # my next task first line


def under_attack(col, queens):
    left = right = col

    for r, c in reversed(queens):
        left, right = left - 1, right + 1

        if c in (left, col, right):
            return True
    return False


def solve(n):
    if n == 0:
        return [[]]

    smaller_solutions = solve(n - 1)

    return [solution + [(n, i + 1)]
            for i in range(BOARD_SIZE)
            for solution in smaller_solutions
            if not under_attack(i + 1, solution)]


for answer in solve(BOARD_SIZE):
    print(answer)  # last line of previous task


# 4 lines: Fibonacci, tuple assignment

parents, babies = (1, 1)  # my next task first line
while babies < 100:
    print('This generation has {0} babies'.format(babies))
    parents, babies = (babies, parents + babies)  # last line of previous task


# 3 lines: For loop, built-in enumerate function, new style formatting

friends = ['john', 'pat', 'gary', 'michael']  # my next task first line
for i, name in enumerate(friends):
    print("iteration {iteration} is {name}".format(iteration=i, name=name))
    # last line of previous task


# 2 lines: Input, assignment

name = input('What is your name?\n')  # my next task first line
print('Hi, %s.' % name)  # last line of previous task


# 5 lines: Functions

def greet(name):  # my next task first lin
    print('Hello', name)


greet('Jack')
greet('Jill')
greet('Bob')  # last line of previous task


# 11 lines: Triple-quoted strings, while loop

REFRAIN = '''
    %d bottles of beer on the wall,
    %d bottles of beer,
    take one down, pass it around,
    %d bottles of beer on the wall!
    '''  # my next task first lin
bottles_of_beer = 9
while bottles_of_beer > 1:
    print(REFRAIN % (bottles_of_beer, bottles_of_beer,
                     bottles_of_beer - 1))
bottles_of_beer -= 1  # last line of previous task


# 7 lines: Dictionaries, generator expressions

prices = {'apple': 0.40, 'banana': 0.50}  # my next task first line
my_purchase = {
    'apple': 1,
    'banana': 6}
grocery_bill = sum(prices[fruit] * my_purchase[fruit]
                   for fruit in my_purchase)
print('I owe the grocer $%.2f' % grocery_bill)  # last line of previous task


# 33 lines: "Guess the Number" Game (edited) from

guesses_made = 0  # my next task first line

name = input('Hello! What is your name?\n')

number = (1, 20)
print('Well, {0}, I am thinking of a number between 1 and 20.'.format(name))

while guesses_made < 6:

    guess = int(input('Take a guess: '))

    guesses_made += 1

    if guess < number:
        print('Your guess is too low.')

    if guess > number:
        print('Your guess is too high.')

    if guess == number:
        break

if guess == number:
    print('Good job, {0}! You guessed my number in {1} guesses!'.format(name, guesses_made))
else:
    print('Nope. The number I was thinking of was {0}'.format(number))
    # last line of previous task


# 28 lines: 8-Queens Problem (define your own exceptions

BOARD_SIZE = 8  # my next task first line


class BailOut(Exception):
    pass


def validate(queens):
    left = right = col = queens[-1]
    for r in reversed(queens[:-1]):
        left, right = left - 1, right + 1
        if r in (left, col, right):
            raise BailOut


def add_queen(queens):

    for i in range(BOARD_SIZE):
        test_queens = queens + [i]
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
# last line of previous task


# 12 lines: Classes

class BankAccount(object):    # my next task first line
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def overdrawn(self):
        return self.balance < 0
my_account = BankAccount(15)
my_account.withdraw(50)


print(my_account.balance, my_account.overdrawn())  # last line of previous task
