#!/usr/bin/python3

"""Defining a square class by: (based on 4-square.py)
"""


class Square:

    """Square class definitions"""

    def __init__(self, size):
        """.............."""
        self.size = size

    @property
    def size(self):
        """___________"""
        return self.__size

    @size.setter
    def size(self, val):
        """_____________"""
        if not isinstance(val, int):
            raise TypeError("size must be an integer")
        elif val < 0:
            raise ValueError("size must be >= 0")
        self.__size = val

    def area(self):
        """............"""

        return self.__size ** 2

    def my_print(self):
        """A function to printts #"""
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print("")
