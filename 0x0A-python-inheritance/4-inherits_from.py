#!/usr/bin/python3
"""subclass module"""


def inherits_from(obj, a_class):
    """inherits function"""
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
