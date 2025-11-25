#!/usr/bin/python3
"""
Module 6-base_geometry
Defines a BaseGeometry class with an unimplemented area() method.
"""


class BaseGeometry:
    """Class BaseGeometry."""

    def area(self):
        """
        Raise an exception because area() is not implemented.

        Raises:
            Exception: always with message 'area() is not implemented'
        """
        raise Exception("area() is not implemented")
