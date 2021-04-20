input_x = 10
rez = 2
while rez < input_x: #Не очень уверен в правильности , работает при x >= 2
    rez = rez << 2
print("Наим.Ст2 от {} = {}".format(input_x, rez >> 2))
