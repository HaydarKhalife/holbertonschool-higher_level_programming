#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    argc = len(argv) - 1
    plural = 's' if argc != 1 else ''
    print("{} argument{}{}{}".format(argc, plural, ':' if argc else '.', '' if argc == 0 else '\n'))
    
    for i, arg in enumerate(argv[1:], 1):
        print("{}: {}".format(i, arg))
