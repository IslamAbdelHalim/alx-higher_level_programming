#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for ky in a_dictionary.copy():
        if ky == key:
            del a_dictionary[ky]
    return a_dictionary
