# 5. Выведите n-ое число Фибоначчи,
# используя только временные переменные, циклические операторы и условные операторы.
# n - вводится
a = 0
b = 1
n = int(input('введите целое число: '))
if n < 0:
    print('Неверное значение: введите положительное число')
elif n == 0:
    print(a)
elif n == 1:
    print(a)
else:
    for i in range(int(n - 2)):
        a, b = b, a+b
    print('элемент последовательности равен ', b)
