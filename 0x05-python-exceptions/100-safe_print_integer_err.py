#!/usr/bin/python3
import sysi


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as err:
        sys.stderr.write("Exception: {}\n".format(err))
        return False
