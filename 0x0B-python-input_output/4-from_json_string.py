#!/usr/bin/python3
"""function that returns an object
    represented by json string """

import json


def from_json_string(my_str):
    """
    function that returns an object

    Args:
        my_str: The string which returns
    """
    return json.loads(my_str)
