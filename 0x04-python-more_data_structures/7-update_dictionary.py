#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for ky in a_dictionary.copy():
        if ky == key:
            a_dictionary[ky] = value
        else:
            a_dictionary[key] = value
    return a_dictionary
