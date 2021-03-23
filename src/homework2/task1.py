"""# 1 task: Посчитайте общую цену в рублях и копейках за L товаров. """
rub = int(input('цена товара в руб. '))
cop = int(input('цена товара в коп.'))
quantity = int(input('количество товара'))
total_cop = (cop * quantity) % 100
total_rub = rub * quantity + (cop * quantity - total_cop) / 100
print("%d руб, %d коп." % (total_rub, total_cop))
