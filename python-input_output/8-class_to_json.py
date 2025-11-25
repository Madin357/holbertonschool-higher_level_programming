#!/usr/bin/python3
"""Defines a function that returns the dictionary description
for JSON serialization of an object.
"""


def class_to_json(obj):
    """Return the dictionary description with simple data structures
    for JSON serialization of an object.

    Args:
        obj: instance of a class
    """
    return obj.__dict__
