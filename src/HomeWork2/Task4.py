"""4. Посчитать количество строчных (маленьких)
и прописных (больших) букв в введенной строке.
Учитывать только английские буквы."""

input_str = "asdЛЛdfддjjv cfFfcc ffжжkSskf fkfjgdd. slk. ffjg"
count_upper = 0
count_small = 0
for char in input_str:
    if ord(char) in range(ord('A'), ord('z') + 1):
        if char.isupper():
            count_upper += 1
        else:
            count_small += 1
print('Count EN Upper Char = {} Count EN small char {} Kop'.format(count_upper, count_small))
