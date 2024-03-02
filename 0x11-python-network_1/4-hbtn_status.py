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
    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")
