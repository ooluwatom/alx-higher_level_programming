#!/usr/bin/python3
import sys

if __name__ == '__main__':
    '''
    Prints the number of and list of arguments
    '''

    if len(sys.argv) == 0:
        print('{:d} arguments.'.format(len(sys.argv)))
    else:
        print('{:d} arguments:'.format(len(sys.argv)))
        for i in range(1, len(sys.argv) + 1):
            print('{:d}:{}'.format(i, sys.argv[i]))
