"""Города"""
"""Дан список стран и городов каждой страны. Затем даны
названия городов. Для каждого города укажите,в какой стране он находится.
Входные данные Программа получает на вход количество стран N. Далее
идет N строк, каждая строка начинается с названия страны, затем идут
названия городов этой страны. В следующей строке записано число M,
далее идут M запросов — названия каких-то M городов, перечисленных
выше. Выходные данные Для каждого из запроса выведите название страны,
в котором находится данный город"""

n = int(input('Enter numbers of country ='))
m = ()
find_city = []
country_cities = {}
current_country_city = {}
for i in range(0, n):
    m = input('Enter country name and cities')
    mass = m.split(' ')
    current_country_city = {mass[0]: mass[1:len(mass)]}
    country_cities.update(current_country_city)
    city_number = int(input('Enter numbers of city ='))
    for g in range(city_number):
        city = input('Enter name of city')
        find_city.append(city)
    for key, values in country_cities.items():
        for val in values:
            if val in find_city:
                print(key)
