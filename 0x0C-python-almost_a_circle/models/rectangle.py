#!/usr/bin/python3

import json
import csv
"""Defining a rectangle class. """
from models.base import Base

"""Rectangle Class.
It inherits from Base.
"""
class Rectangle(Base):
    """a rectangle representation"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """New Rectangle initialization.
    Args:
        width (int): new Rectangle's width
        height (int): new Rectangle's height
        x (int): new Rectangle's x coordinate
        y (int): new Rectangle's y coordinate
    Raises:
    TypeError: If either of width/height or x/y is not an int
    ValueError: If either of width/height or x/y <= 0.
    """
    self.width = width
    self.height = height
    self.x = x
    self.y =y
    supper().__init__(id)

@property
def width(self):
    """set/get the Rectangle's width"""
    return self.__width

@width.setter
def width(self, value):
    if type(value) != int:
        raise TypeError("Width must be an Integer")
    if value <= 0:
        raise ValueError("Width must be > 0")
    self.__width = value

@property
def height(self):
    """set/get the Rectangle's width"""
    return self.__height

@height.setter
def height(self, value):
    if type(value) != int:
        raise TypeError("Height must be an Integer")
    if value <= 0:
        raise ValueError("Height must be an Integer")
    self.__height = value

@property
def x(self):
    """set/get the Rectangle's x coordinate"""
    return self.__x
@x.setter
def x (self, value):
    if type(value) != int:
        raise TypeError("x must be an Integer")
    if value <= 0:
        raise ValueError("x must be >= 0")
    self.__x = value

@property
def y(self):
    """set/get the Rectangle's y coordinate"""
    return self.__x
@y.setter
def y(self, value):
    if type(value) !=int:
        raise TypeError("y must be an Integer")
    if value <= 0:
        raise ValueError("y must be >=0")
    self.__y = value

def area(self):
        """Return the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """Print the Rectangle using the `#` character."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """Update the Rectangle.
        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
