"""1-я  задачка"""


def email_gen(list_of_names):
    emails = []
    for i in list_of_names:
        letter = 1
        while i[1] + '.' + i[0][0:letter] + '@company.io' in emails:
            letter += 1
        emails.append(i[1] + '.' + i[0][0:letter] + '@company.io')
    return emails


strings = []
f = open('D:\\AlexeiKarnauhov\\task_file.txt', 'r')
for i in f:
    strings.append(i.split(','))
f.close()
list_of_names = []
n = 0
for i in strings:
    list_of_names.append([])
    if i[0] == 'EMAIL' or len(i[3].replace(' ', '')) != 7 or ' \n' in i or len(i[1]) <= 1 or \
            len(i[2]) <= 1 or i[3].replace(' ', '').isdigit() is False:
        list_of_names[n].append('no_email')
        list_of_names[n].append('no_email' + str(n))
    else:
        list_of_names[n].append(i[1].replace(' ', ''))
        list_of_names[n].append(i[2].replace(' ', ''))
    n += 1
emails = (email_gen(list_of_names))
print(strings)
n = 0
f = open('D:\\AlexeiKarnauhov\\task_file.txt', 'w')
for i in strings:
    if 'no_email' not in emails[n]:
        i[0] = emails[n]
    n += 1
    f.write(i[0] + ',' + i[1] + ',' + i[2] + ',' + i[3] + ',' + i[4])
f.close()

"""и еще задачка - бинарный поиск"""


def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))
print(binary_search(my_list, -1))
