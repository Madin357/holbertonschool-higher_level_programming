#!/usr/bin/env python3
"""
Task 02: Convert CSV to JSON
Reads a CSV file and converts the data into JSON format.
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file into JSON format and save the output to data.json.

    Parameters:
        csv_filename (str): Path to the CSV file.

    Returns:
        bool: True if conversion succeeds, False if an error occurs.
    """
    try:
        data_list = []

        # Read CSV file using DictReader
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                data_list.append(row)

        # Write JSON output to data.json
        with open("data.json", mode='w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file)

        return True

    except Exception:
        return False
