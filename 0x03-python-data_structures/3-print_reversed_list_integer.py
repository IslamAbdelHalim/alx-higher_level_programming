#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    # Make The reverse first befor you use it
    my_list.reverse()
    for x in my_list:
        print("{:d}".format(x))
