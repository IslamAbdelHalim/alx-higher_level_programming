#!/usr/bin/python3
"""write a string to a text file"""


def write_file(filename="", text=""):
    """
    function that write a text into a file

    Args:
        filename: The name of file

        text: The text which we adding
    """
    with open(filename, 'w', encoding="UTF-8") as file:
        return file.write(text)
