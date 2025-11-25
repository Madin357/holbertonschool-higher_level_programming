#!/usr/bin/env python3
"""
Task 03: XML Serialization and Deserialization
Provides functions to convert between Python dictionaries and XML files.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to an XML file.

    Parameters:
        dictionary (dict): The dictionary to serialize.
        filename (str): Output XML file.

    Returns:
        bool: True if successful, False otherwise.
    """
    try:
        root = ET.Element("data")

        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)

        return True

    except Exception:
        return False


def _convert_type(value):
    """
    Attempt to convert a string back into int, float, or bool.
    Otherwise return the string itself.
    """
    if value is None:
        return None

    # Check for boolean
    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False

    # Check for int
    try:
        return int(value)
    except ValueError:
        pass

    # Check for float
    try:
        return float(value)
    except ValueError:
        pass

    # Fallback: keep string
    return value


def deserialize_from_xml(filename):
    """
    Deserialize an XML file back into a Python dictionary.

    Parameters:
        filename (str): Input XML file.

    Returns:
        dict: The reconstructed dictionary, or None if error occurs.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}

        for child in root:
            result[child.tag] = _convert_type(child.text)

        return result

    except Exception:
        return None
