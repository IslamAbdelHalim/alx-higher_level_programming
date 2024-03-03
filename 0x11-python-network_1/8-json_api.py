#!/usr/bin/python3
"""
Search API
"""

if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    resp = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})

    try:
        data = resp.json()

        if data:
            print(f"[{data['id']}] {data['name']}")
        else:
            print("No result")
    except ValueError:
        print("No a valid JSON")
