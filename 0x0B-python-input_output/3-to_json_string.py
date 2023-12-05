#!/usr/bin/python3
"""function that return json"""

import json


def to_json_string(my_obj):
    """
    function that return json representation of the object

    Args:
        my_obj: The object which return the json
    """

    return json.dumps(my_obj)
