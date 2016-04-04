# Uses python3

import sys


def min_dot_product(a, b):
    res = 0
    for i in range(len(a)):
        max_a = max(x for x in a[i:])
        min_b = min(x for x in b[i:])
        print('m', max_a, min_b)
        res += max_a * min_b

    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(min_dot_product(a, b))
