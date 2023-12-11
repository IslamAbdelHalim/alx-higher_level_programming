#!/usr/bin/python3
"""Square Module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialize Variable"""
        if type(size) is not int:
            raise TypeError("width must be an integer")
        if size < 0:
            raise ValueError("width must be > 0")
        self.size = size
        super().__init__(self.size, self.size, x, y, id)

    @property
    def size(self):
        """getter size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter size"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """function that update attributes"""
        if len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def __str__(self):
        """function that return string"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def to_dictionary(self):
        """
        function that  that returns
        the dictionary representation of a Square
        """
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
