#!/usr/bin/python3
"""Defines a class Student."""
  

class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the Student.

        If attrs is a list of strings, return only the attributes
        listed in attrs. Otherwise, return all attributes.
        """
        if isinstance(attrs, list) and all(type(el) is str for el in attrs):
            return {key: getattr(self, key)
                    for key in attrs if hasattr(self, key)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student using a dictionary."""
        for key, value in json.items():
            setattr(self, key, value)
