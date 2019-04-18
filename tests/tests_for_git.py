def return_few_func_value():
    return 7, 8, 9
    # return 7, 8


def print_with_semicolon():
    print(7, 8, 10, 20, sep=':')


def squares(x):
    for x in range(x+1):
        print(x ** 2)


def fib(x):
    a, b = 0, 1
    while a < x:
        print(a, end=' ')
        a, b = b, a+b
    print()

# x, y, z = return_few_func_value()
#
# print("x: ", x)
# print("y: ", y)
# print("z: ", z)


#print_with_semicolon()

# squares(10)
fib(1457)
