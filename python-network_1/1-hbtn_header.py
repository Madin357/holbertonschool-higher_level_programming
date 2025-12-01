#!/usr/bin/python3
"""
Sends a request to a URL and displays the X-Request-Id
value found in the response header.
"""

import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        headers = response.headers
        print(headers.get("X-Request-Id"))
