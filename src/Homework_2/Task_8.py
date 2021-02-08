"""Зарегистрируйтесь на одном (или нескольких) из сайтов:
https://py.checkio.org/ , https://www.codewars.com,
https://www.hackerrank.com/,
https://acmp.ru И решите 1-5 задач уровня Elementary и advanced.
Поместите 3 простых и 2 сложных задачи на Ваш выбор в пул реквест."""

"""Complete the function that accepts a string parameter, and reverses each word in the string.
All spaces in the string should be retained."""


def reverse_words(text):
    b = text.split(' ')
    c = []
    d = ' '
    for i in b:
        i = i[::-1]
        c.append(i)
    d = ' '.join(c)
    return d


"""Build Tower by the following given argument:
number of floors (integer and always greater than 0)."""


def tower_builder(n_floors):
    floors = []
    n = n_floors
    for i in range(n_floors):
        n -= 1
        floors.append(' ' * n + '*' * (i * 2 + 1) + ' ' * n)
    return floors


"""Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string, the longest possible,
containing distinct letters - each taken only once - coming from s1 or s2."""


def longest(s1, s2):
    temp_set_1 = set(s1)
    temp_set_2 = set(s2)
    new_string_1 = ''.join(temp_set_1)
    new_string_2 = ''.join(temp_set_2)
    new_string_3 = new_string_1 + new_string_2
    temp_set_3 = set(new_string_3)
    new_4 = sorted(''.join(temp_set_3))
    new_5 = ''.join(new_4)
    return new_5


"""Given two integers a and b, which can be positive or negative,
find the sum of all the integers between including them too and return it.
If the two numbers are equal return a or b."""


def get_sum(a,b):
    if b > a:
        c = [int(i) for i in range(a,b + 1)]
        get_sum = sum(c)
        return get_sum
    elif a > b:
        c = [int(i) for i in range(b,a + 1)]
        get_sum = sum(c)
        return get_sum
    elif a == b:
        return a


"""Write simple .camelCase method (camel_case function in PHP,
CamelCase in C# or camelCase in Java) for strings.
All words must have their first letter capitalized without spaces."""


def camel_case(string):
    import re
    string_1 = string.title()
    result = re.findall(r'\w+', string_1)
    result_1 = ''.join(result)
    return result_1
