#!/usr.bin/python3

"""
Defining a square by: (based on 2-square.py)
"""


class Square:
    """Represent a square class"""

    def __init__(self, size=0):
        """Initiating Square class"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ calculating area"""

        return self.__size * self.__size
