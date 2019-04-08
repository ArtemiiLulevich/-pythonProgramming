import shelve
#
# with shelve.open('shelveTests') as items:
#     items["lemon"] = "a sour, yellow, citrus fruit"
#     # items["numbers"] = range(0, 10, 2)
#     items["list"] = list("35178946")
#
#     print(sorted(items["list"]))
#     print(items["list"])
#     # print(items["number"])
#

fruit = shelve.open("shelveTests")

# print(fruit["lemon"])
# print(fruit["list"])
#
# del fruit["numbers"]

fruit["lime"] = "great with tequila"
fruit["number"] = 234.56
#
#
# while True:
#     fruit_input = input("What you want? \n")
#     if fruit_input == "quit":
#         break
#
#     print(fruit.get(fruit_input, "We don't have this " + fruit_input))

ord_keys = list(fruit.keys())
ord_keys.sort()

for i in ord_keys:
    print(i + "-" + str(fruit[i]))

fruit.close()

