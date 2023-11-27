#!/usr/bin/python3
"""Module For say my name method

The 'say_my_name()' function used to print full name

print name by this way My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """say_my_name is function that use to print name

    Args:
        first_name: The first parameter
        last_name: The second parameter

    Raises:
        TypeError: if first_name or last_name not string

    Return:
        nothing just print name by this way
        My name is <first name> <last name>
    """
    # Handle if first_name or last_name not string
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    elif type(last_name) is not str:
        raise TypeError('last_name must be a string')

    print(f"My name is {first_name} {last_name}")
