#!/usr/bin/python3
"""Defines a class Student."""
  

class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name: student's first name
            last_name: student's last name
            age: student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary representation of a Student.

        If attrs is a list of strings, only return the attributes
        listed in attrs. Otherwise, return all attributes.
        """
        if isinstance(attrs, list) and all(type(el) is str for el in attrs):
            return {key: getattr(self, key)
                    for key in attrs if hasattr(self, key)}
        return self.__dict__
