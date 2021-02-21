my_str_reg = 'Hi my little Tim'
low_co = 0
hi_co = 0
for i in my_str_reg:
    if ord(i) in range(65, 90):
        hi_co += 1
    else:
        if ord(i) in range(97, 122):
            low_co += 1

print("%d %d" % (hi_co, low_co))
