#!/usr/bin/python3
"""
Defines a square class
"""
from rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that inherits from the Rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Square class constructor
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        String representation
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
