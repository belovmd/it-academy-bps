"""# 1 task:  Dict comprehensions: generator """

dct = {str(element + 1): (element + 1) ** 3 for element in range(20)}
print(dct)
