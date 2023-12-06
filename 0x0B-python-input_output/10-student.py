#!/usr/bin/python3
"""student module"""


class Student:
    """Class student"""
    def __init__(self, first_name, last_name, age):
        """initialize variables"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation
        of a Student instance"""

        if attrs is None:
            return self.__dict__

        if all(type(a) is str for a in attrs):
            return {a: getattr(self, a)
                    for a in attrs if hasattr(self, a)}
