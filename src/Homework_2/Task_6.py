"""Определите, является ли число палиндромом (читается слева направо и справа налево одинаково).
Число положительное целое, произвольной длины. Задача требует работать только с числами
(без конвертации числа в строку или что-нибудь еще)"""


def polyndrom(num):
    num_rev = 0
    while num // 10 != 0:
        num_rev = num_rev * 10 + num % 10
        num = num // 10
    else:
        num_rev = num_rev * 10 + num % 10
    return num_rev


num = int(input("Enter number: "))
if num == polyndrom(num):
    print("Polyndrom")
else:
    print("Not polyndrom")
