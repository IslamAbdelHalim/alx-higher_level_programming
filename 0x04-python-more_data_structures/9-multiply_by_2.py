#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_a_dictionary = {}
    for ky, num in a_dictionary.items():
        new_a_dictionary[ky] = a_dictionary[ky] * 2
    return new_a_dictionary
