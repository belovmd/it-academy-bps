"""Даны: три стороны треугольника. Требуется: проверить, действительно ли это стороны треугольника.
Если стороны определяют треугольник, найти его площадь. Если нет,
вывести сообщение о неверных данных."""


from math import sqrt
side_a = float(input("Enter size of side_A: "))
side_b = float(input("Enter size of side_B: "))
side_c = float(input("Enter size of side_C: "))
poluper = (side_a + side_b + side_c) / 2
if side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a:
    square = sqrt(poluper * (poluper - side_a) * (poluper - side_b) * (poluper - side_c))
    print("Square of triangle is {}".format(square))
else:
    print("This is not a triangle!")
