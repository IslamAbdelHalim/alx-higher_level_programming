#!/usr/bin/python3
"""
My GitHub
"""

if __name__ == "__main__":
    import requests
    import sys

    user_name = sys.argv[1]
    password = sys.argv[2]

    api = 'https://api.github.com/user'

    resp = requests.get(api, auth=(user_name, password))

    data = resp.json()

    print(data.get('id'))
