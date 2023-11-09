#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    bestScore = 0
    bestOne = ''
    for ky, value in a_dictionary.items():
        if value > bestScore:
            bestScore = value
            bestOne = ky
    return bestOne
