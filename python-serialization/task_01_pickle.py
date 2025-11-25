#!/usr/bin/env python3
"""
Task 01: Serialization and deserialization using pickle
Defines a CustomObject class that supports saving and loading
instances using pickle.
"""

import pickle


class CustomObject:
    """A custom class representing a person."""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes in the required format."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current object instance to the given filename.

        Returns:
            True if successful, None if an error occurs.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
            return True
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize and return a CustomObject instance from file.

        Returns:
            CustomObject instance if successful, otherwise None.
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)

            # Ensure the loaded object is a CustomObject
            if isinstance(obj, cls):
                return obj
            return None
        except Exception:
            return None
