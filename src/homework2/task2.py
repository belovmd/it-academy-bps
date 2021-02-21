import re

my_string = "vjvj. dhпрпррпрпрпрdh,ghhg djdjd?jdjdjdj"
mas = re.split('[,.;:!? ]', my_string)
temp = ''
for char in mas:
    if len(char) > len(temp):
        temp = char
print(temp)
