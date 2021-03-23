"""# 7 task:  2 numbers by  algorithm Euclid """

a = 24
b = 15

while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a
print(a + b)
