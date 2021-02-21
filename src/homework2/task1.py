prices1 = input('цена товара в руб. коп.')
quantity = int(input('количество товара'))
new_pr = prices1.split(',')
rub = int(new_pr[0])
cop = int(new_pr[1])
total_cop = (cop * quantity) % 100
total_rub = rub * quantity + (cop * quantity - total_cop) / 100
print("%d руб, %d коп." % (total_rub, total_cop))
