#!/usr/bin/python3

"""
===================================
module with class Rectangle
===================================
"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Method for calculated area"""
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
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Method to redefine an area method in the parent class"""
        return self.__width * self.__height

    def __str__(self):
        """__str__ method for returning the next string"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """Square class that inherits from Rectangle that inherits BaseGeometry"""

    def __init__(self, size):
        """Method for initializing the attributes"""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Square area"""
        return self.__size ** 2
