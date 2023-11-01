#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    nstr = ""
    for c in str:
        if i == n:
            i += 1
            continue
        else:
            nstr += c
            i += 1
    return nstr
