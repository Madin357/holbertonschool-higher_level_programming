#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for item in my_list:
        if not isinstance(item, int):
            raise TypeError("list must contain only integers")
        print("{:d}".format(item))

list=[1,2,3]
print_list_integer(list)
