#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for element in matrix:
        for int in element:
            print('{:d}'.format(int), end='')
