#!/usr/bin/python3
""" Techniacl interview"""


def find_peak(list_of_integers):
    """ a function that find a peak"""

    if list_of_integers is None \
            or list_of_integers == [] \
            or len(list_of_integers) == 0:
        return None

    if len(list_of_integers) == 1:
        return list_of_integers[0]

    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return list_of_integers[left]
