#!/usr/bin/python3
"""
Module 7-base_geometry
Defines a BaseGeometry class with area() and integer_validator().
"""


class BaseGeometry:
    """Class BaseGeometry with validation methods."""

    def area(self):
        """
        Raise an exception because area() is not implemented.

        Raises:
            Exception: always with message 'area() is not implemented'
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that value is a positive integer.

        Args:
            name (str): the name of the parameter.
            value: the value to validate.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value <= 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
