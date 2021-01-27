print('Hello, world!')

# name = input('What is your name?\n')
name = 'john'
print('Hi, %s.' % name)

friends = ['john', 'pat', 'gary', 'michael']
for i, name in enumerate(friends):
    print("iteration {iteration} is {name}".format(iteration=i, name=name))


class Rectangle:
    color = "green"
    width = 100
    height = 100

    def square(self):
        return self.width * self.height


rect_A = Rectangle()
print(rect_A.color)
print(rect_A.square())
rect_B = Rectangle()
rect_B.width = 200
rect_B.color = "brown"
print(rect_B.color)
print(rect_B.square())


def max2(a, b):
    if a > b:
        return a
    else:
        return b


print(max(3, 1))


def max3(x, y, z):
    return max2(x, max2(y, z))


print(max3(45, 3, 54))

str1 = "mn3" * 3 + "\n"
str2 = "fdc" * 4 + "\n"
print(str1 + str2)
