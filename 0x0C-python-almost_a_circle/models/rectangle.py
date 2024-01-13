#!/usr/bin/python3
"""
Defines a rectangle class
"""
from base import Base


class Rectangle(Base):
    """
    Rectangle class that inherits from the base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculate area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        Print size of rectangle using #
        """
        for _ in range(self.__y):
            print()

        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def update(self, *args):
        """
        Assign arguments to attributes based on their position.
        """
        if args:
            attributes = ["id", "width", "height", "x", "y"]

            for i, attr in enumerate(attributes):
                if i < len(args):
                    setattr(self, attr, args[i])
