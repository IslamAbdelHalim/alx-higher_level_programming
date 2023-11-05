#!/usr/bin/python3
def element_at(my_list, idex):
    if idex < 0:
        return None
    elif idex > len(my_list) - 1:
        return None
    else:
        return my_list[idex]
