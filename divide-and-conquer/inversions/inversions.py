# Uses python3
# good for colobarative filtering
import sys

inversions = 0

def merge_sort2(a, length):
    # :(
    global inversions
    result = []

    if len(a) < 2:
        return a

    mid = int(len(a) / 2)
    right = merge_sort2(a[:mid], length)
    left = merge_sort2(a[mid:], length)
    i = 0
    j = 0

    while i < len(right) and j < len(left):
        if right[i] > left[j]:
            result.append(left[j])
            if i:
                inversions += i
            else:
                inversions += len(right)
            print((len(right) - i, len(left) - j))
            j += 1
        else:
            result.append(right[i])
            i += 1

    # copy rest of array
    result += right[i:]
    result += left[j:]

    # when done return inversions
    if len(result) == length:
        return inversions
    return result


def get_number_of_inversions(a, b, c, d):
    global inversions
    inversions = 0
    return merge_sort2(a, len(a))


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))
