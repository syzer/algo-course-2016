# Uses python3
import sys


def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    # write your code here
    return -1


def get_majority2(a, left, right):
    return max(a, key=a.count)
    # can also use Counter(d).most_common()[0]


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority2(a, 0, n) != -1:
        print(1)
    else:
        print(0)
