#!/usr/bin/python3
'''A function that divides all elements of a matrix'''


def matrix_divided(matrix, div):
    if type(matrix) is not list:
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
    return [[round(x/div, 2) for x in row] for row in matrix]
