#!/usr/bin/python3i
def square_matrix_map(matrix=[]):
    return list(map(lambda row: list(map(lambda x: x * x, row)), matrix))
