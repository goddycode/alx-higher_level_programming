#!/usr/bin/python3

"""Defining a square by: (based on 3-square.py"""


class Square:

    """Represent square class"""
    def __init__(self, size=0):

        """Initiating class"""

        self.size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def (size, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ working on area of a square """

        return (self.__size * self.__size)
