"""1. Напишите программу, которая считает общую цену.
Вводится M рублей и N копеек цена,
а также количество S товара Посчитайте общую цену в рублях и копейках за L товаров.
Пример:
Input: Цена одной вещи 3 рубля 20 копеек, посчитать 3 предмета.
Output: Общая цена 9 рублей 60 копеек"""


price_in_rubles = int(input("Enter price in rubles:  "))
price_in_cop = float(input("Enter price in cop: "))
quantity_goods = int(input("Enter quantity of goods: "))
total_price = (price_in_rubles + price_in_cop) * quantity_goods

print(total_price)
