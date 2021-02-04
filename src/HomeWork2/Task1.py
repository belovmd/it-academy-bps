""" 1. Напишите программу, которая считает общую цену.
Вводится M рублей и N копеек цена, а также количество S товара
Посчитайте общую цену в рублях и копейках за L товаров.
Пример:
Input: Цена одной вещи 3 рубля 20 копеек, посчитать 3 предмета.
Output: Общая цена 9 рублей 60 копеек """
import re

str_input = input("Input:")
str_nums = re.findall(r'\d+', str_input)
str_nums = [int(i) for i in str_nums]
if len(str_nums) >= 3:
    amount = str_nums[0] * str_nums[2] + str_nums[1] / 100 * str_nums[2]
    print('Amount to pay = {} Rub. {} Kop'.format(int(amount // 1), int(amount % 1 * 100)))
else:
    print('Incorrect Input')

price_rub = int(input('Price Rub:'))
price_kop = int(input('Price Kop:'))
count_product = int(input('Count Product:'))
print('Amount to pay = {}'.format(price_rub * count_product + price_kop / 100 * count_product))
amount = price_rub * count_product + price_kop / 100 * count_product
print('Amount to pay = {} Rub. {} Kop'.format(int(amount // 1), int(amount % 1 * 100)))
