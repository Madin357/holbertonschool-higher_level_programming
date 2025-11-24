#!/usr/bin/python3
"""
Module 0-lookup
Provides a function that returns the list of attributes and methods
of an object.
"""


def lookup(obj):
    """
    Return the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list: A list of strings representing the attributes and methods.
    """
    return dir(obj)
