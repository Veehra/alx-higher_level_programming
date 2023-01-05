#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    i = 0
    j = len(argv)

    if j == 2:
        print("{} argument:".format(j - 1))
    elif j == 1:
        print("{} arguments.".format(j - 1))
    else:
        print("{} arguments:".format(j - 1))

    for arg in argv:
        if i == 0:
            i += 1
            continue
        print("{}: {}".format(i, arg))
        i += 1
