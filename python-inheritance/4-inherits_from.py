#!/usr/bin/python3
"""
Module 4-inherits_from
Defines a function that checks if an object is an instance
of a class that inherited (directly or indirectly) from
a specified class.
"""


def inherits_from(obj, a_class):
    """
    Return True if obj is an instance of a class that inherited
    (directly or indirectly) from a_class; otherwise False.

    Args:
        obj: The object to inspect.
        a_class: The class to compare against.

    Returns:
        bool: True if obj inherits from a_class.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
