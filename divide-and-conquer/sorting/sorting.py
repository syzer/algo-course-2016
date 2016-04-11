# Uses python3
import sys
import random


def part3(a, left, right):
    pivot = random.randint(left, right)
    a[left], a[pivot] = a[pivot], a[left]
    i = left + 1
    pivot = a[left]

    for j in range(left + 1, right + 1):
        if a[j] < pivot:
            a[j], a[i] = a[i], a[j]
            i += 1

    pos = i - 1
    a[left], a[pos] = a[pos], a[left]

    return pos


# 3-way partition
def randomized_quick_sort3(a, l, r):
    if l >= r:
        return

    m = part3(a, l, r)
    randomized_quick_sort3(a, l, m - 1)
    randomized_quick_sort3(a, m + 1, r)


#     :( modifies array
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort3(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
