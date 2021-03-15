""" 1. Напишите программу, которая считает общую цену.
Вводится M рублей и N копеек цена, а также количество S товара
Посчитайте общую цену в рублях и копейках за L товаров.
Пример:
Input: Цена одной вещи 3 рубля 20 копеек, посчитать 3 предмета.
Output: Общая цена 9 рублей 60 копеек """


def output_amount(list_nums):  # for V_1, V_2 DRY
    if len(list_nums) >= 3:
        res_am = list_nums[0] * list_nums[2] + list_nums[1] / 100 * list_nums[2]
        print('Amount to pay = {} Rub. {} Kop'.format(int(res_am // 1), int(res_am % 1 * 100)))
    else:
        print('Incorrect Input')


str_input = input("Input:")
word_list = str_input.split()
num_list = [int(num) for num in filter(lambda num: num.isnumeric(), word_list)]
output_amount(num_list)
