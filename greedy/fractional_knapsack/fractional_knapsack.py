#!/usr/bin/env python
# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    value = 0.

    ratio = [x / y for x, y in zip(values, weights)]
    all_items = list(zip(values, weights, ratio))
    all_items.sort(key=lambda tup: -tup[2])

    for i in all_items:
        left_load = capacity / i[1]
        if left_load > 1:
            left_load = 1
        if left_load > 0:
            capacity -= i[1]
            value += i[0] * left_load

    return round(value, 4)


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
