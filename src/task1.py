"""Dict comprehensions Создайте словарь с помощью генератора словарей,
так чтобы его ключами были числа от 1 до 20, а значениями кубы этих чисел."""
num_dict = dict((item, item**3) for item in range(1, 21))
print(num_dict)
