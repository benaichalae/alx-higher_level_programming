#!/usr/bin/python3
"""square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """defines the class square"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializes a square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string representation of a square"""
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update square that assigns attributes to args"""
        attr_names = ["id", "size", "x", "y"]
        if args:
            for i, arg in enumerate(args):
                setattr(self, attr_names[i], arg)
        else:
            for key, value in kwargs.items():
                if key in attr_names:
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns dictionary representation of a square"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
