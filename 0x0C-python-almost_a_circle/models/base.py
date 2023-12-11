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
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        function  that writes the JSON string
        representation of list_objs to a file

        Args:
            cls - refer to the main class
            list_objs - list of objects
        """
        file_name = cls.__name__ + ".json"  # to get the class name
        dicts = []  # dict to save the object dicts on it
        with open(file_name, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                for obj in list_objs:
                    # add object dicts to list of dicts
                    dicts.append(obj.to_dictionary())
                # add the list dict to json file
                file.write(cls.to_json_string(dicts))

    @staticmethod
    def from_json_string(json_string):
        """
         function that returns the list of the JSON string
         representation json_string

         Args:
            json_string; is a string representing a list of dictionaries
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        function that returns an instance with all
        attributes already set

        Args:
            dictionary: the attribute of new object
        Return:
            new instance
        """
        if dictionary is not None:
            if cls.__name__ == "Rectangle":
                obj = cls(5, 10)
            if cls.__name__ == "Square":
                obj = cls(9)
            obj.update(**dictionary)
            return obj
