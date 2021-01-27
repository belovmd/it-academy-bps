print  ('Hello, world!')

parents, babies = (1, 1)
while babies < 100:
    print ('This generation has {0} babies'.format(babies))
    parents, babies = (babies, parents + babies)

friends = ['john', 'pat', 'gary', 'michael']
for i, name in enumerate(friends):
    print ("iteration {iteration} is {name}".format(iteration=i, name=name))

name = input('What is your name?\n')
print ('Hi, %s.' % name)

def greet(name):
    print ('Hello', name)

greet('Jack')
greet('Jill')
greet('Bob')

# This program adds up integers that have been passed as arguments in the command line
import sys
try:
    total = sum(int(arg) for arg in sys.argv[1:])
    print ('sum =', total)
except ValueError:
    print ('Please supply integer arguments')

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