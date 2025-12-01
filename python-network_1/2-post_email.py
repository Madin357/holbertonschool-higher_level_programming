#!/usr/bin/python3
"""
Sends a POST request to a given URL with an email parameter
and displays the response body (decoded in UTF-8).
"""

import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({"email": email}).encode("utf-8")

    with urllib.request.urlopen(url, data=data) as response:
        body = response.read().decode("utf-8")
        print(body)
