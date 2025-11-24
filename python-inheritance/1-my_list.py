#!/usr/bin/python3
"""
Module 1-my_list
Defines a class MyList that inherits from list and
adds the ability to print the list sorted.
"""


class MyList(list):
    """
    A subclass of list that provides a method to print
    the list sorted in ascending order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        The original list is not modified.
        """
        print(sorted(self))
