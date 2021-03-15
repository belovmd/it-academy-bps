"""7. Даны: три стороны треугольника. Требуется: проверить,
действительно ли это стороны треугольника.
Если стороны определяют треугольник, найти его площадь.
Если нет, вывести сообщение о неверных данных."""

len_AB = 23.5
len_BC = 34.6
len_CA = 45.2
if len_AB + len_BC > len_CA and len_AB + len_CA > len_BC and len_BC + len_CA > len_AB:
    p = (len_AB + len_BC + len_CA) / 2.0  # Полупериметр
    s_triangel = (p * (p - len_AB) * (p - len_BC) * (p - len_CA)) ** 0.5
    print(u"Area of a triangle = {0:.2f}".format(s_triangel))
else:
    print("Incorrect length")
