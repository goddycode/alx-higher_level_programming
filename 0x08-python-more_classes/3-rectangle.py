#!/usr/bin/python

"""Defining an empty class"""


class Rectangle:
	"""Representing Rectangle class"""

	def __init__(self, width=0, height=0):
		"""Initialization method"""
		self.__width = width
		self.__height = height
	
	@property
	def width(self):
		return self.__width
	
	@width.setter
	def width(self, value):
		if not isinstance(value):
			raise TypeError("width must be an integer")
		elif(value <= 0):
			raise ValueError("width must be >= 0")
		
		return self.__width

	@property
	def height(self):
		return self.__height
	
	@height.setter
	def height(self, value):
		if not isinstance(value):
			raise TypeError("height must be an integer")
		elif (value <= 0):
			raise ValueError("height must be >= 0")
		return self.__width
	
	def area(self):
		"""This method with calculate the area of rectangle"""
		
		return self.__width * self.__height

	def perimeter(self):
		"""This method calculate the peri of rectangle"""

		if self.__width == 0 or self.__height == 0:
			return 0

		return ((self.__width * 2) + (self.__height * 2))
	
	def __str__(self):
        """Return the printable representation of the Rectangle.
        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))
