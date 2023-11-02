#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argc = len(sys.argv)
    count = 0

    if argc == 0:
        print('0')
    else:
        for i in range(1, argc):
            count += int(sys.argv[i])
        else:
            print(count)
