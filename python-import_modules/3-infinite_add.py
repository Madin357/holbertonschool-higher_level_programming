#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    total = 0
    args = sys.argv[1:]

    for arg in args:
        total += int(arg)

    print(total)
