# 6. Определите, является ли число палиндромом
# (читается слева направо и справа налево одинаково).
# Число положительное целое, произвольной длины.
# Задача требует работать только с числами (без конвертации числа в строку или что-нибудь еще)
n = int(input('Введите число: '))
num = n
obr = 0
while n > 0:
    obr = obr * 10 + n % 10
    n = n // 10
if num == obr:
    print('Число является палиндром')
else:
    print('Число не является палиндром')
