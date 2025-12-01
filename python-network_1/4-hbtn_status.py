#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status using the requests package
and displays information about the response body.
"""

import requests

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"

    response = requests.get(url)
    text = response.text

    print("Body response:")
    print("\t- type: {}".format(type(text)))
    print("\t- content: {}".format(text))
