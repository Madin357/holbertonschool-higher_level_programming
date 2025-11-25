#!/usr/bin/python3
"""
This module adds all command-line arguments to a list and saves
the list as a JSON array into the file 'add_item.json'.

It uses:
    save_to_json_file  - from 5-save_to_json_file.py
    load_from_json_file - from 6-load_from_json_file.py
"""

import sys

# Import required functions using __import__ (because filenames start with numbers)
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"

try:
    items = load_from_json_file(filename)
except Exception:
    items = []

items.extend(sys.argv[1:])

save_to_json_file(items, filename)
