#!/usr/bin/python3
"""append a string"""


def append_write(filename="", text=""):
    """
    function that append string into a file

    Args:
        filename: The file name

        text: the which appended
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
