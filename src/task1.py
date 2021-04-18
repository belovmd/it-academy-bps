"""Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел, кратных 3 пишет Fizz,
вместо чисел кратный 5 пишет Buzz, а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz"""

result = []
for num_range in range(1, 101):
    if not num_range % 15:
        result.append('FizzBuzz')
    elif not num_range % 3:
        result.append('Fizz')
    elif not num_range % 5:
        result.append('Buzz')
    else:
        result.append(num_range)
print(result)
