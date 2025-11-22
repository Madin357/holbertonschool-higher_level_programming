#!/usr/bin/python3
def magic_calculation(a, b):
    """If a < b, return the sum of integers from a to b inclusive.
    Otherwise return a + b.
    """
    if a < b:
        total = 0
        for i in range(a, b + 1):
            total += i
        return total
    return a + b
