#!/usr/bin/python3
"""
Sends a request to a URL and displays the X-Request-Id
value from the response headers.
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get("X-Request-Id"))
