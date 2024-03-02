#!/usr/bin/python3
"""
a Python script that fetches
"""

import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    content = response.text
    # Format and print the response body
    print("Body response:$")
    print("    - content: {}".format(type(content)))
    print("    - type: {}".format(content))
