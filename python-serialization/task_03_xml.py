def deserialize_from_xml(filename):
    """
    Deserialize an XML file back into a Python dictionary.

    Returns:
        dict: The reconstructed dictionary or None on error.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}

        for child in root:
            result[child.tag] = child.text  # keep as STRING

        return result

    except Exception:
        return None
