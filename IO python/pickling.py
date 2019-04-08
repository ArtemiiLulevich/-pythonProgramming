import pickle

# items = ('PC gears', "2019", (
#     ('Mouse', 'Rivals 500'),
#     ('Keyboard', 'Apex M750'), ('Headphones', 'Artice 5')))
# with open('IO samples\\PCGears.pickle', 'wb') as pickle_file:
#     pickle.dump(items, pickle_file)

# with open('IO samples\\PCGears.pickle', 'rb') as unpickled_file:
#     unpickled_items = pickle.load(unpickled_file)
#
# gears, year, gear_list = unpickled_items
# print(gears)
# print(year)
# for gear in gear_list:
#     gear_type, name = gear
#     print(gear_type, '-', name)


items = ('PC gears', "2019", (
    ('Mouse', 'Rivals 500'),
    ('Keyboard', 'Apex M750'), ('Headphones', 'Artice 5')))

intNumber = 2345167

floatNum = 1245.1457

set1 = {'x', 'y'}

with open('IO samples\\someInfo.pickle', 'wb') as pickle_file:
    pickle.dump(items, pickle_file)
    pickle.dump(intNumber, pickle_file)
    pickle.dump(floatNum, pickle_file)
    pickle.dump(set1, pickle_file)

with open('IO samples\\someInfo.pickle', 'rb') as unpickled_file:
    items_unpickled = pickle.load(unpickled_file)
    intNumber_un = pickle.load(unpickled_file)
    floatNum_un = pickle.load(unpickled_file)
    set1_un = pickle.load(unpickled_file)

gears, year, gear_list = items_unpickled
print(gears)
print(year)
for gear in gear_list:
    gear_type, name = gear
    print(gear_type, '-', name)

print('-'*40)
print(intNumber_un)
print('-'*40)
print(floatNum_un)
print('-'*40)

for i in set1_un:
    print(i)

print('-'*40)
