#!/usr/bion/python3
Rectangle = __import__('2-rectangle').Rectangle

myrectangle = Rectangle(2, 4)

print("Area: {} - perimeter: {}".format(myrectangle.area(), myrectangle.perimeter()))

print(str(myrectangle))
print(repr(myrectangle))

print("--")

myrectangle.width = 10
myrectangle.height = 6
print(myrectanngle)
print(repr(myrectangle))
