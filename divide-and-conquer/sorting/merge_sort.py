from collections import Counter


def merge_sort(arr):
    if len(arr) == 1:
        return arr

    if len(arr) == 2:
        if arr[0] > arr[1]:
            return [arr[1], arr[0]]
        else:
            return arr

    split = len(arr) // 2

    # sort halves recursively
    # left = merge_sort(arr[split:])
    # right = merge_sort(arr[0:split])

    # merge left/right
    # merge(left, right)
    return merge(sorted(arr[0:split]), sorted(arr[split:]))


def merge(left, right):
    output = []
    while left  or right :
        if left:
            min_left = left[0]
        else:
            return output + right
        if right:
            min_right = right[0]
        else:
            return output + left

        if min_left <= min_right:
            output.append(left.pop(0))
        else:
            output.append(right.pop(0))

    return output


a = [7, 2, 5, 3, 7, 13, 1, 6]
test = merge_sort(a)
print(test)
def test_1():
    assert test == sorted(a)
