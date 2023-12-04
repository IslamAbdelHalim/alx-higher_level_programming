#!/usr/bin/python3
"""Geometry model"""


class BaseGeometry(object):
    """Base Geometry"""

    def area(self):
        """instance method"""
        raise Exception("area() is not implemented")
