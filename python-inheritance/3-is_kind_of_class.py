#!/usr/bin/python3
"""
Module 3-is_kind_of_class
Provides a function that checks if an object is an instance of
a class, or of a class that inherited from it.
"""


def is_kind_of_class(obj, a_class):
    """
    Return True if obj is an instance of a_class or an instance
    of a class that inherited from a_class; otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance or inherited instance.
    """
    return isinstance(obj, a_class)
