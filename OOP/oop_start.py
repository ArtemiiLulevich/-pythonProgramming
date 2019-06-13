class Kettle(object):

    power_source = "Electricity"

    def __init__(self, make, price):  # __init__ method is a constructor
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)

print("Models: {0.make} - {0.price}, "
      "{1.make} - {1.price}".format(kenwood, hamilton))

kenwood.switch_on()

print(kenwood.on)

Kettle.switch_on(hamilton)
print(hamilton.on)

print("*" * 50)
Kettle.power = 1.5

saturn = Kettle("Saturn", 6)
print(saturn.power)
print(kenwood.power)

print(Kettle.power_source)
print("Switch kenwood power")
kenwood.power_source = "Gas"
print(kenwood.power_source)
print(saturn.power_source)

print(Kettle.__dict__)
print(kenwood.__dict__)
print(saturn.__dict__)
