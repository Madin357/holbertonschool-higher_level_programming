#!/usr/bin/python3
"""
This script adds all command-line arguments to a Python list
and saves the list to a JSON file named add_item.json.

It uses the functions:
    save_to_json_file  - from 5-save_to_json_file.py
    load_from_json_file - from 6-load_from_json_file.py
"""

import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"

try:
    # Try to load the existing list
    items = load_from_json_file(filename)
except Exception:
    # If file doesn't exist, start with an empty list
    items = []

# Add all command-line arguments (except the script name)
items.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(items, filename)
