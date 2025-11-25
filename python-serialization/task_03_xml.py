#!/usr/bin/env python3
"""
Task 03: XML Serialization and Deserialization
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary into XML and save it to a file.

    Parameters:
        dictionary (dict): Dictionary to serialize.
        filename (str): Destination XML filename.
    """
    try:
        # Create root element
        root = ET.Element("data")

        # Add children
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        # Build the tree and write to file
        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)

        return True
    except Exception:
        return False


def deserialize_from_xml(filename):
    """
    Deserialize XML data from a file into a Python dictionary.

    Parameters:
        filename (str): XML filename to read.

    Returns:
        dict: Deserialized dictionary, or None if an error occurs.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result_dict = {}

        for element in root:
            # All XML values are strings; user decides type handling later
            result_dict[element.tag] = element.text

        return result_dict

    except Exception:
        return None
