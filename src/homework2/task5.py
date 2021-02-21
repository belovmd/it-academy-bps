num_fibo = int(input('enter number'))
preprev = 0
prev = 1
current = 0
i = 2
if num_fibo == 1:
    print(preprev)
elif num_fibo == 2:
    print(prev)
elif num_fibo >= 3:
    while num_fibo != i:
        current = prev + preprev
        preprev = prev
        prev = current
        i += 1
    print(current)
