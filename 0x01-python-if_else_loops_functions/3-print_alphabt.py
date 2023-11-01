#!/usr/bin/python3
for w in range(97, 122):
    if w == 101:
        continue
    elif w == 113:
        continue
    else:
        print("{:c}".format(w), end="")
