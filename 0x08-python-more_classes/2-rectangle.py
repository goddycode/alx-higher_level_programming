#!/usr/bin/python

"""Defining an empty class"""


class Rectangle:
	"""Class declaration"""

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

		return ((self.__width * 2) + (self.__height * 2))
