#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    else:
        mx = 0
        for x in my_list:
            if x > mx:
                mx = x
        return mx
