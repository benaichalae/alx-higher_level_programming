#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""
    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
        width (int): The width of the new rectangle.
        height (int): The height of the new rectangle.
        """
        self.__set_dimensions(width, height)

    def __set_dimensions(self, width, height):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get/set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        self.__set_dimensions(value, self.__height)

    @property
    def height(self):
        """Get/set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        self.__set_dimensions(self.__width, value)

    def area(self):
        """Return the area of the Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width > 0 and self.__height > 0:
            return 2 * (self.__width + self.__height)
        else:
            return 0

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width] * self.__height)

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        print("Bye rectangle...")
