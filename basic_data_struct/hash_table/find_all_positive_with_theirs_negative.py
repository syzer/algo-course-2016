# Problem statement:
# Given: N a list of integers.
# Design a function that finds all positive numbers in the array that have their opposites in it as well.
# Describe approaches for solving optimal worst case and optimal average case performance, respectively.


before = [-7, 4, -3, 2, 2, -8, -2, 3, 3, 7, -2, 3, -2]


def find_all_positive_with_negative():
    found = {}

    for val in before:
        if abs(val) in found:
            found[abs(val)] = [-abs(val), abs(val)]
        else:
            found[abs(val)] = val

    return filter_is_array(found.values())


# TODO lambda/filter is_array
def filter_is_array(arr):
    test = []

    for val in arr:
        if type(val) is list:
            test.append(val)

    return test

print(find_all_positive_with_negative())
# [[-2, 2], [-3, 3], [-7, 7]]


# TODO when needs to be sorted, and not just filtered
# Sorted: -2 -2 -2 2 2 -3 3 3 4 -7 7 -8
