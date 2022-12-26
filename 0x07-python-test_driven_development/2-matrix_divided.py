#!/usr/bin/python3
'''A function that divides all elements of a matrix'''


def matrix_divided(matrix, div):
    '''Matrix division function'''
    if(not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError('matrix must be a matrix (list of lists)\
of integers/floats')
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
    return [[round(x/div, 2) for x in row] for row in matrix]
