#!/usr/bin/python3

"""Defining a square by: (based on 1-square.py)"""


class Square:
    """Representing square class"""

    def __init__(self, size=0):
        """Initiating"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
