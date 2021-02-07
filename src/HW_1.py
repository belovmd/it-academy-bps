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


my_account = BankAccount(15)
my_account.withdraw(50)
print(my_account.balance, my_account.overdrawn())
