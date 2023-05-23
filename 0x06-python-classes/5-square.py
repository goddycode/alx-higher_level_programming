#!/usr/bin/python3

"""Defining a square class by: (based on 4-square.py)
"""


class Square:

    """Square class definitions"""

    def __init__(self, side=0):
        """.............."""
        self.side = side

    @propety
    def side(self):
        """___________"""
        return self.__side

    @side.setter
    def side(self, val):
        """_____________"""
        if not isinstance(val, int):
            raise TypeError("size must be an integer")
        elif val < 0:
            raise ValueError("size must be >= 0")
        self.__side = val

    def area(self):
        """............"""

        return self.__side ** 2

    def my_print(self):
        """A funxtion to printts #"""
        if self.__size == 0:
            prrint()
        elif self.__size > 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end=" ")
                    print()
