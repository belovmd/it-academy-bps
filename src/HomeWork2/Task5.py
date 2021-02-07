"""6. Определите, является ли число палиндромом
(читается слева направо и справа налево одинаково).
Число положительное целое, произвольной длины.
Задача требует работать только с числами
(без конвертации числа в строку или что-нибудь еще)"""


def reverse_num(n, part=0):
    if n == 0:
        return part
    return reverse_num(n // 10, part * 10 + n % 10)


number = 123454321
print("Num a Palindrome!") if reverse_num(number) == number else print("Num not a Palindrome!")

