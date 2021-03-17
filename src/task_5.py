"""Выведите n-ое число Фибоначчи, используя только временные переменные,
циклические операторы и условные операторы. n - вводится"""

fibona4i_1 = fibona4i_2 = 1

num = int(input("Введите номер элемента ряда Фибоначчи: "))

if num < 2:
    quit()

print(fibona4i_1, end=' ')
print(fibona4i_2, end=' ')
for i in range(2, num):
    fibona4i_1, fibona4i_2 = fibona4i_2, fibona4i_1 + fibona4i_2
    print(fibona4i_2, end=' ')

print()
