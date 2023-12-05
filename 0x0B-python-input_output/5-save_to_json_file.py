#!/usr/bin/python3
"""save object to a file"""

import json


def save_to_json_file(my_obj, filename):
    """
    function that use to save a object json to a file

    Args:
        my_obj: The object which will add to the file

        filename: The file which added
    """
    with open(filename, 'w', encoding="UTF-8") as file:
        json.dump(my_obj, file)
