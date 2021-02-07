"""5. Выведите n-ое число Фибоначчи, используя только временные переменные,
циклические операторы и условные операторы. n - вводится"""


def fibonac(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b


list_num = list(fibonac(10))
print(list_num)
