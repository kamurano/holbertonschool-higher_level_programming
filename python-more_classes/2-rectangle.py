#!/usr/bin/python3
"""Function for adding 2 integers"""


class Rectangle:
    """Class that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Method to initialize the rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Method to get the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Method to set the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Method to get the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Method to set the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Method to compute the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Method to compute the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
