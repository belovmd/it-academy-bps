"""# 6 task:  different word in text """
import re
import string

my_string = "Hi, my little Tim. Sorry,    Tim, for my last early call."
mas = re.split(' ', my_string)
diff_word = 0
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in mas]
for i in stripped:
    if i == '':
        continue
    if stripped.count(i) != 1:
        continue
    else:
        diff_word += 1
print(diff_word)
