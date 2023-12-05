#!/usr/bin/python3
"""create an object from a json file"""

import json


def load_from_json_file(filename):
    """
    function that create an object from a json file

    Args:
        filename: the file which will crease an object
    """
    with open(filename, 'r', encoding="utf-8") as file:
        decode = json.load(file)
        return decode
