#!/usr/bin/python3
"""append after"""


def append_after(filename="", search_string="", new_string=""):
    """append after function"""
    with open(filename, 'r', encoding="utf-8") as f:
        line_lint = []
        while True:
            line = f.readline()
            if line == "":
                break
            line_lint.append(line)
            if search_string in line:
                line_lint.append(new_string)
    with open(filename, 'w', encoding="utf-8") as f:
        f.writelines(line_lint)
