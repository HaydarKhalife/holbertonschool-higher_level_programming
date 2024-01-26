#!/usr/bin/python3
def uppercase(str):
    for lowstr in str:
        if ord(lowstr) >= 97 and ord(lowstr) <= 122:
            lowstr = chr(ord(lowstr) - 32)
        print("{}".format(lowstr), end='')
    else:
        print("")
