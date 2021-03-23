"""# 6 task:  ordered list """

list_num = [1, 0, 7, 9, 0, 8, 0, 1, 9, 0]
current_null_index = 0
for i in range(0, len(list_num)):
    current_num = list_num[i]
    if current_num == 0 and i < len(list_num):
        current_null_index = i
        for j in range(i + 1, len(list_num)):
            if list_num[j] != 0:
                temp = list_num[current_null_index]
                list_num[current_null_index] = list_num[j]
                list_num[j] = temp
                current_null_index = j
print(list_num)
