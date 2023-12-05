#!/usr/bin/python3
"""read a text file"""


def read_file(filename=""):
    """
    function that read a text file

    Args:
        filename: The file which will read
    """
    with open(filename, encoding="utf-8") as f:
        text = f.read()
        print(text, end="")
