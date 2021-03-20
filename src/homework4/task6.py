"""# 6 task:  different word in text """

my_string = "Hi, my little Tim. Sorry, Tim, for my last early call."




my_string = "vjvj. dhпрпррпрпрпрdh, ghhg djdjd?jdjdjdj"
mas = re.split(' ', my_string)
temp = ''
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in mas]
for char in stripped:
    if len(char) > len(temp):
        temp = char
print(temp)