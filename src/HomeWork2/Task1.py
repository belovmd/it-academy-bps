""" 1. Напишите программу, которая считает общую цену.
Вводится M рублей и N копеек цена, а также количество S товара
Посчитайте общую цену в рублях и копейках за L товаров.
Пример:
Input: Цена одной вещи 3 рубля 20 копеек, посчитать 3 предмета.
Output: Общая цена 9 рублей 60 копеек """
import re


def output_amount(list_nums):  # for V_1, V_2 DRY
    if len(list_nums) >= 3:
        res_amount = list_nums[0] * list_nums[2] + list_nums[1] / 100 * list_nums[2]
        print('Amount to pay = {} Rub. {} Kop'.format(int(res_amount // 1), int(res_amount % 1 * 100)))
    else:
        print('Incorrect Input')


# V_1 if space between words
str_input = input("Input:")
word_list = str_input.split()
num_list = [int(num) for num in filter(lambda num: num.isnumeric(), word_list)]
output_amount(num_list)

# V_2
str_input = input("Input:")
str_nums = re.findall(r'\d+', str_input)
str_nums = [int(i) for i in str_nums]
output_amount(str_nums)

# V_3
price_rub = int(input('Price Rub:'))
price_kop = int(input('Price Kop:'))
count_product = int(input('Count Product:'))
print('Amount to pay = {}'.format(price_rub * count_product + price_kop / 100 * count_product))
amount = price_rub * count_product + price_kop / 100 * count_product
print('Amount to pay = {} Rub. {} Kop'.format(int(amount // 1), int(amount % 1 * 100)))
