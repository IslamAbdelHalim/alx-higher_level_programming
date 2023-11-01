#!/usr/bin/python3
i = 122

while i >= 97:
    print(f"{i:c}", end="")
    print("{:c}".format((i-1) - 32), end="")
    i -= 2
