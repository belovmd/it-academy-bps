a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
poluper = (a + b + c) / 2
s = poluper * (poluper - a) * (poluper - b) * (poluper - c)

if a + b > c and a + c > b and b + c > a:
    print(s ** .5)
else:
    print('Это не треугольник')
