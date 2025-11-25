#!/usr/bin/python3
"""Square class that inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a square using Rectangle's validation."""

    def __init__(self, size):
        """Initialize a Square with a validated size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the Square."""
        return self.__size * self.__size

    def __str__(self):
        """Return the string representation of the Square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
