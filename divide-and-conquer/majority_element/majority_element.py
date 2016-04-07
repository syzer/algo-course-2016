# Uses python3
import sys
from collections import Counter


def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    # write your code here
    return -1


def get_majority_pythonic(a, left, n):
    most_common = Counter(a).most_common()[0]
    if most_common[1] > n / 2:
        return 1
    else:
        return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_pythonic(a, 0, n) != -1:
        print(1)
    else:
        print(0)
