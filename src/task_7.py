"""Даны: три стороны треугольника. Требуется: проверить,
действительно ли это стороны треугольника. Если стороны определяют
треугольник, найти его площадь.
Если нет, вывести сообщение о неверных данных."""

from math import sqrt
side_a = float(input("Введите длину стороны A: "))
side_b = float(input("Введите длину стороны B: "))
side_c = float(input("Введите длину стороны C: "))
poluper = (side_a + side_b + side_c) / 2
if side_a + side_b > side_c and side_a + side_c > side_b \
        and side_b + side_c > side_a:
    square = sqrt(poluper * (poluper - side_a) * (poluper - side_b) *
                  (poluper - side_c))
    print("Площадь треугольника {}".format(square))
else:
    print("Это не треугольник")
