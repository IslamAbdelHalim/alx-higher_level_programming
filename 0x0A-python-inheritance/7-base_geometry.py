#!/usr/bin/python3
"""Base Geometry model"""


class BaseGeometry:
    """Base Class"""
    def area(self):
        """Instance method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        instance method that validate integer

        Args:
            self: instance object
            name: is a string
            value: is a integer
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
