# 7. Даны: три стороны треугольника.
# Требуется: проверить, действительно ли это стороны треугольника.
# Если стороны определяют треугольник, найти его площадь.
# Если нет, вывести сообщение о неверных данных.
A = int(input('Введите значение стороны A: '))
B = int(input('Введите значение стороны B: '))
C = int(input('Введите значение стороны C: '))
P = (A + B + C) * 0.5
if A == B == C:
    S = (P * (P - A) * (P - B) * (P - C)) ** 0.5
    print('Это равносторонний треугольник площадью =', S)
elif A < (B + C) and B < (A + C) and C < (A + B):
    S = (P * (P - A) * (P - B) * (P - C)) ** 0.5
    print('Это треугольник площадью =', S)
else:
    print('Это не треугольник')
