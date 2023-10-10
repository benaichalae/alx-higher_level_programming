#!/usr/bin/python3
"""inherite from Rectangle (9-rectangle.py)"""

class Square(Rectangle):
    """Square Class"""
    def __init__(self, size):
        """Intialize with size"""
        self.__size = size
        super().__init__(self.__size, self.__size)
