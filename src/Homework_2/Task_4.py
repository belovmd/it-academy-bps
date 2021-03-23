"""Посчитать количество строчных (маленьких) и прописных (больших)
букв в введенной строке. Учитывать только английские буквы."""


str_ = input("Enter string: ")
small_letters = 0
big_letters = 0
for i in str_:
    if 'a' <= i <= 'z':
        small_letters += 1
    elif 'A' <= i <= 'Z':
        big_letters += 1
print("Quantity of small_letters = {} and big_letters = {}".format(small_letters, big_letters))
