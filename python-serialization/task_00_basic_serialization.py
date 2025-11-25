#!/usr/bin/env python3
"""
Basic Serialization Module
Provides functions to serialize a Python dictionary to a JSON file
and deserialize a JSON file back into a Python dictionary.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary and save it to a JSON file.

    Parameters:
        data (dict): The dictionary to serialize.
        filename (str): The output JSON filename. Replaces the file if it exists.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load and deserialize JSON data from a file.

    Parameters:
        filename (str): The input JSON filename.

    Returns:
        dict: The deserialized dictionary.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
