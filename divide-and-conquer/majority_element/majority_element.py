# Uses python3
import sys
from collections import Counter


def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]

    mid = left + (right - left) // 2
    print(a, left, right,get_majority_element(a, left, mid-1) )
    if get_majority_element(a, left, mid - 1) == get_majority_element(a, mid + 1, right):
        return 1

    return -1


# proxy
def get_maj_el(a, left, right):
    if get_majority_element(a, left, right) == 1:
        return 1
    else:
        return 0


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
    if get_majority_pythonic(a, 0, n) != -1:
        print(1)
    else:
        print(0)
