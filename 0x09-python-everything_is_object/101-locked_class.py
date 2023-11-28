#!/usr/bin/python3
"""lock module"""


class LockedClass:
    """ locked class 
    hat prevents the user from dynamically creating new instance attributes,
    """
    __slots__ = ["first_name"]
