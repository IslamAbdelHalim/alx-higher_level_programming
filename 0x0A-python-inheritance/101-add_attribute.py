#!/usr/bin/python3
"""Add Atribout module"""


def add_attribute(obj, attr, value):
    """
    function that add atribute to the object

    Arg:
        obj: It is the object
        attr: the attribute
        value: the value of attrbnute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
