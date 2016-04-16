def merge_sort(arr):
    if len(arr) == 1:
        return arr

    split = len(arr) // 2

    # sort halves recursively
    left = merge_sort(arr[split:])
    right = merge_sort(arr[0:split])

    return merge(left, right)


def merge(left, right):
    output = []
    while left or right:
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


def merge_sort2(x):
    result = []
    if len(x) < 2:
        return x
    mid = int(len(x)/2)
    y = merge_sort2(x[:mid])
    z = merge_sort2(x[mid:])
    i = 0
    j = 0
    while i < len(y) and j < len(z):
        if y[i] > z[j]:
            result.append(z[j])
            j += 1
        else:
            result.append(y[i])
            i += 1
    result += y[i:]
    result += z[j:]

    return result


def merge_sort3(x):
    result = []
    if len(x) < 20:
        return sorted(x)
    mid = int(len(x) / 2)
    y = merge_sort3(x[:mid])
    z = merge_sort3(x[mid:])
    i = 0
    j = 0
    while i < len(y) and j < len(z):
        if y[i] > z[j]:
            result.append(z[j])
            j += 1
        else:
            result.append(y[i])
            i += 1
    result += y[i:]
    result += z[j:]

    return result


a = [7, 2, 5, 3, 7, 13, 1, 6]
test = merge_sort(a)
print(test)


def test_1():
    assert test == sorted(a)

def test_2():
    a = [7, 2, 5, 3, 7, 13, 1, 6]
    assert merge_sort2(a) == sorted(a)

def test_3():
    a = [7, 2, 5, 3, 7, 13, 1, 6]
    assert merge_sort3(a) == sorted(a)