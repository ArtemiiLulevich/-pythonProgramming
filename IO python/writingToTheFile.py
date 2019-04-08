# cities = ['Donetsk', 'Kiev', 'London']
#
# with open("IO samples\\cities.txt", 'w') as city_file:
#     for city in cities:
#         print(city, file=city_file)

cities = []

with open("IO samples\\cities.txt", 'r') as city_file:
    for city in city_file:
        cities.append(city.strip('\n'))

print(cities)

for city in cities:
    print(city)
