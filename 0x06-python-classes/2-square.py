#!/usr/bin/python3

""" Defining a square class  by: (based on 1-square.py)"""


class Square:

    """Class initiation"""
    def __init__(self, size=0):
        self.size = size

    """Getter"""
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, val):
        if isinstance(val, int):
            if val < 0:
                raise ValueError("size must be >= 0")
            else:
                return self.__size
        else:
            raise TypeError("size must be an integer")
