#!/usr/bin/python3
"""
Uses GitHub API with Basic Authentication to display your GitHub user id.
Prints None if authentication fails.
"""

import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://api.github.com/user"

    try:
        response = requests.get(url, auth=(username, token))
        if response.status_code == 200:
            print(response.json().get("id"))
        else:
            print(None)
    except requests.exceptions.RequestException:
        print(None)
