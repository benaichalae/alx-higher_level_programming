class Rectangle:
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__validate_dimension(value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__validate_dimension(value)
        self.__height = value

    def __validate_dimension(self, value):
        if not isinstance(value, int):
            raise TypeError("Dimension must be an integer")
        if value < 0:
            raise ValueError("Dimension must be >= 0")

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width > 0 and self.__height > 0:
            return 2 * (self.__width + self.__height)
        else:
            return 0

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width] * self.__height)

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)
