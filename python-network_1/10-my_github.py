#!/usr/bin/python3
"""
Uses GitHub API with Basic Authentication to display your GitHub user id.
"""

import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://api.github.com/user"

    try:
        response = requests.get(url, auth=(username, token))
        response.raise_for_status()
        print(response.json().get("id"))
    except requests.exceptions.RequestException as e:
        print("Error:", e)
