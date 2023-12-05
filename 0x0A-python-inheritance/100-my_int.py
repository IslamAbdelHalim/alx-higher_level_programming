#!/usr/bin/python3
"""Int Module"""


class MyInt(int):
    """MyInt subclass"""
    def __init__(self, num):
        """
        initialize the variables
        """
        self.num = num
        int.__init__(self.num)

    def __eq__(self, other):
        """to make !="""
        return int(self) != other

    def __ne__(self, other):
        """TO make =="""
        return int(self) == other
