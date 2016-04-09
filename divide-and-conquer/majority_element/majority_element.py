# Uses python3
import sys
from builtins import *
from collections import Counter

# checks if its just a mode or real mojority
def check_majority(arr, candidate):
    counter = 0
    for i in arr:
        if i == candidate:
            counter += 1
    if counter > len(arr) / 2:
        return 1
    else:
        return -1

# cals mode most common i array
def majority2(arr):
    counter, candidate = 0, None
    for i in arr:
        if counter == 0:
            candidate, counter = i, 1
        elif i == candidate:
            counter += 1
        else:
            counter -= 1

    return candidate


# adapter
def get_maj_el(a, left, right):
    return check_majority(a, majority2(a))

# this one uses stdlib
def get_majority_pythonic(a, left, n):
    most_common = Counter(a).most_common()[0]
    if most_common[1] > n / 2:
        return 1
    else:
        return 0


if __name__ == '__main__':
    sys.setrecursionlimit(15000)
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_maj_el(a, 0, n) != -1:
        print(1)
    else:
        print(0)
