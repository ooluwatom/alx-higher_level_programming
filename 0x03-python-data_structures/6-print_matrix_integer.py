#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for element in matrix:
        print('\n', end='')
        for int in element:
            print('{:d}'.format(int), end=' ')
