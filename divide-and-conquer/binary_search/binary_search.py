# Uses python3
import sys


def binary(a, left, right, x):
    # NOT FOUND
    if right < left:
        # should be initial left - 1
        return - 1

    mid = left + (right - left) // 2

    if a[mid] == x:
        return mid
    if x < a[mid]:
        return binary(a, left, right - 1, x)
    else:
        return binary(a, left + 1, right, x)


# adapter for binary
def binary_search(a, x):
    left, right = 0, len(a) - 1
    return binary(a, left, right, x)


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


if __name__ == '__main__':
    sys.setrecursionlimit(15000)
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1: n + 1]
    for x in data[n + 2:]:
        print(binary_search(a, x), end=' ')
