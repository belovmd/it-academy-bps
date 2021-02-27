str = 'asd dsag'
other = str.replace(' ', '')
str2 = other[::-1]
print(other == str2)
print(str2)

sent = 'my school gjgjjgjgjgjjgjgjg ggg fdxsdf hjj hh'
temp = ''
list = sent.split(' ')
for i in list:
    if len(i) > len(temp):
        temp = i
print(temp)

my_string = 'fhhfv nbnb ldld'
list_s = my_string.split(' ')
x = '.'.join(list_s)
print(x)

my_date = '05.06.1989'
list_ss = my_date.split('.')
print(list_ss)
temp_l = list_ss[0]
list_ss[0] = list_ss[1]
list_ss[1] = temp_l
print('/'.join(list_ss))
