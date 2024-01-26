#!/usr/bin/python3
for pos1 in range(0, 9):
    for pos2 in range(pos1 + 1, 10):
        if pos1 < 8:
            print("{}{}, ".format(pos1, pos2), end="")
        else:
            print("{}{}".format(pos1, pos2))
