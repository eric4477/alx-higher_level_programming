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

    @property
    def size(self):
        """
        Getter for width
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for width and height
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updating and assigning attributes based on arguments position
        """
        if args:
            for count, arg in enumerate(args):
                if count == 0:
                    self.id = arg
                elif count == 1:
                    self.size = arg
                elif count == 2:
                    self.x = arg
                elif count == 3:
                    self.y = arg
                else:
                    break
        elif kwargs:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == "size":
                    self.width = value
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
                else:
                    break
