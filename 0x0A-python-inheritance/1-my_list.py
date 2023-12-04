#!/usr/bin/python3
"""List Module"""


class MyList(list):
    """
    MyList Class
    """

    def print_sorted(self):
        """print_sorted method"""
        sort_list = sorted(self)
        print(sort_list)
