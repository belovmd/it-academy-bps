"""# 2 task:  Dict comprehensions: city """

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
for g in range(0, city_number):
    city = input('Enter name of city')
    find_city.append(city)
for key, values in country_cities.items():
    for val in values:
        if val in find_city:
            print(key)
