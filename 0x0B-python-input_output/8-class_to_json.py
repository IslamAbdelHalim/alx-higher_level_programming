#!/usr/bin/python3
"""returns the dictionary description"""


def class_to_json(obj):
    """
    function that returns the dictionary description with simple data structure
    for JSON serialization of an object

    Args:
        obj:  is an instance of a Class

    Return:
        the dict description
    """
    return obj.__dict__
