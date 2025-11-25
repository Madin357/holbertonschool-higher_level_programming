#!/usr/bin/python3
"""Defines a function to generate Pascal's triangle."""
  

def pascal_triangle(n):
    """Return a list of lists of integers representing Pascal’s triangle.

    If n <= 0: return an empty list.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        row = [1]

        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

        row.append(1)
        triangle.append(row)

    return triangle
