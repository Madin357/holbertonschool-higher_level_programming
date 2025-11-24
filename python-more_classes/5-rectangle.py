#!/usr/bin/python3
"""
This module defines a Rectangle class that can compute area,
perimeter, print itself using `#`, recreate itself using repr,
and print a message when deleted.
"""


class Rectangle:
    """Represents a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize the Rectangle instance."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the rectangle area."""
        return self.width * self.height

    def perimeter(self):
        """Return the rectangle perimeter."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return a string representation of the rectangle using `#`."""
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join("#" * self.width for _ in range(self.height))

    def __repr__(self):
        """Return a string that can recreate the rectangle."""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Print a message when a Rectangle instance is deleted."""
        print("Bye rectangle...")
