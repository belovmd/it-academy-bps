"""# 4 task:  pairs of elements"""

str_num = '4 1 77 22 22 22 22 1'
str_temp = str_num.split(' ')
num = []
total = 0

for i in str_temp:
    num.append(int(i))

for c in range(0, len(num)):
    current_element = num[c]
    if c + 1 < len(num):
        for g in range(c + 1, len(num)):
            next_element = num[g]
            if next_element == current_element:
                total += 1
print(total)
