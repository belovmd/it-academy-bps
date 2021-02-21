palindrom = 1221
is_palindrom = palindrom
rever = 0
remainder = 0

while is_palindrom != 0:
    remainder = is_palindrom % 10
    rever = rever * 10 + remainder
    is_palindrom = is_palindrom // 10

if int(palindrom == rever):
    print('True')
else:
    print('False')
