#!/usr/bin/python3
import calculator_1
if __name__ == "__main__":
    '''
    Prints operations on two numbers
    '''
    a = 10
    b = 5
    print('{:d} + {:d} = {:d}'.format(a, b, add(a, b)))
    print('{:d} - {:d} = {:d}'.format(a, b, sub(a, b)))
    print('{:d} * {:d} = {:d}'.format(a, b, mul(a, b)))
    print('{:d} / {:d} = {:d}'.format(a, b, div(a, b)))
