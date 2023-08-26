#!/usr/bin/python3
"""Find the peak in list of unsorted integers
"""


def find_peak(list_of_integers):
    """Find peak in unsorted list
    """
    loi = list_of_integers
    size = len(loi)

    if size == 0:
        return None

    if size is 1:
        return loi[0]

    return recursive(loi, 0, size - 1)


def recursive(loi, left, right):
    """Recursive component
    """
    mid = int((left + right) / 2)

    if left > right:
        return loi[mid]

    if (mid == 0 or loi[mid] > loi[mid - 1])\
       and (mid == len(loi) - 1 or loi[mid] > loi[mid + 1]):
        return loi[mid]

    # recursive left
    elif (mid > 0) and loi[mid - 1] > loi[mid]:
        return recursive(loi, left, mid - 1)
    else:  # recursive right
        return recursive(loi, mid + 1, right)
