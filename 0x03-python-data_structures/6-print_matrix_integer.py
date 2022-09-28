#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for element in matrix:
        print('\n', end='')
        for int in element:
            if element[-1] != int:
                print('{:d}'.format(int), end=' ')
            else:
                print('{:d}'.format(int), end='')
                