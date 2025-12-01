#!/usr/bin/python3
"""
Sends a POST request to http://0.0.0.0:5000/search_user
with a letter as parameter and displays the result.

- If JSON is valid and not empty: [<id>] <name>
- If JSON is empty: No result
- If JSON is invalid: Not a valid JSON
"""

import sys
import requests

if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    url = "http://0.0.0.0:5000/search_user"

    try:
        response = requests.post(url, data={"q": letter})
        response_json = response.json()
        if response_json:
            print("[{}] {}".format(response_json.get("id"), response_json.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
