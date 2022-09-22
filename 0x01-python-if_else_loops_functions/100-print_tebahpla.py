#!/usr/bin/python3
for i in reversed(range(97, 123)):
    if (i % 2 == 0):
        print(f'{i:c}', end='')
    else:
        print(f'{(i-32):c}', end='')
