#!/usr/bin/python3
def element_at(my_list, idex):
    if idex < 0:
        return None
    elif idex > len(my_list):
        return None
    else:
        for x in my_list:
            if x == idex:
                return my_list[x]


# None: is a special value that represents the absence of a
# value or the concept of nothingness.
