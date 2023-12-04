#!/usr/bin/python3
"""recatangle method"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Recangle class"""
    def __init__(self, width, height):
        """
        initialize the variables

        Args:
            self: instance class
            width: The width of rectangle
            height: The height of rectangle
        """
        self.integer_validator("width", width)
        self.__widht = width
        self.integer_validator("height", height)
        self.__height = height
