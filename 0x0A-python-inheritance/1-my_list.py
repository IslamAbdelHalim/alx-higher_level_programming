#!/usr/bin/python3
"""List Module"""


class MyList(list):
    """
    MyList Class
    """
    def __init__(self):
        """initialize the parent method"""
        list.__init__(self)

    def print_sorted(self):
        """print_sorted method"""
        sort_list = sorted(self)
        print(sort_list)
