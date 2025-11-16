#!/usr/bin/python3

def uppercase(str):
    result = ""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:   # a–z
            result += chr(ord(c) - 32)      # convert to uppercase
        else:
            result += c
    print("{}".format(result))
