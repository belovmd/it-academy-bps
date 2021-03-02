"""FizzBuzz
Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел, кратных 3 пишет Fizz,
вместо чисел кратный 5 пишет Buzz, а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz
Задачу поместите в файл task1.py в папке src/homework3."""


def FizzBuzz_4ange(n):

    if n % 3 == 0 and n % 5 == 0:
        return ("FizzBuzz")
    elif n % 3 == 0:
        return ("Fizz")
    elif n % 5 == 0:
        return ("Buzz")
    else:
        return str(n)


print(' '.join(FizzBuzz_4ange(n) for n in range(1, 101)))
