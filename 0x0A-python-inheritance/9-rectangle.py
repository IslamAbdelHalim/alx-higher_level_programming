#!/usr/bin/python3
"""Rectangle module"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Subclass BaseGeometry"""
    def __init__(self, width, height):
        """
        initialization of variables

        Args:
            self: The instance object
            width: The Rectangle width
            height: The Rectangle height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        function that return the area
        """
        return self.__width * self.__height

    def __str__(self):
        """
        function that return a string
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
