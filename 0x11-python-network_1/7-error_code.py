#!/usr/bin/python3
"""
Write a Python script that takes in a URL,
sends a request to the URL and displays the body of the response.
"""

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]

    resp = requests.get(url)

    if resp.status_code >= 400:
        print(f"Error code: {resp.status_code}")
    else:
        print(resp.text)
