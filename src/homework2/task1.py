# Напишите программу, которая считает общую цену.
# Вводится M рублей и N копеек цена, а также количество S товара
# Посчитайте общую цену в рублях и копейках за L товаров.
# Пример:
# Input: Цена одной вещи 3 рубля 20 копеек, посчитать 3 предмета.
# Output: Общая цена 9 рублей 60 копеек

m = int(input('Введите цену товара, руб.: '))
n = int(input('Введите цену товара, коп.: '))
s = int(input('Введите количество товара, шт.: '))
print('Общая цена:', (m * 100 + n) * s // 100, 'рублей', (m * 100 + n) * s % 100, 'копеек')
