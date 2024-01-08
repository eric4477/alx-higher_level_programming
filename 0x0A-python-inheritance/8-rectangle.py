#!/usr/bin/python3

"""
===================================
module with class Rectangle
===================================
"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """method for calculated area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method for validating if a num is an integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self._width = width
        self.integer_validator("height", height)
        self._height = height
