#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dicit = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 20,
            'C': 100,
            'D': 500,
            'M': 1000
            }
    if not roman_string:
        return None

    num = 0
    total = 0

    for x in reversed(roman_string):
        num = roman_dicit[x]
        total += num if total < num * 5 else -num
    return total
