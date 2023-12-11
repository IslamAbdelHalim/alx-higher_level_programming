#!/usr/bin/python3
"""Base Module"""

import json


class Base:
    """This is a class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize the variable

        Args:
            self: instance variable
            id: is an integer
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        function that returns the JSON string representation
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []
        else:
            return json.dumps(list_dictionaries)
