#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    num_args = len(argv) - 1
    args = argv[1:]

    if num_args == 0:
        print("0 arguments.")
    else:
        plural_s = 's' if num_args > 1 else ''
        print("{:d} argument{:s}:".format(num_args, plural_s))

        for i, arg in enumerate(args, start=1):
            print("{:d}: {}".format(i, arg))
