# Uses python3
import sys
import random


def randomized_quick_sort3(a, left, right):
    if right - left < 2: return
    key = a[random.randrange(left, right)]
    i = left
    j = left
    pivot = right

    while j < pivot:
        if a[j] < key:
            a[j], a[i] = a[i], a[j]
            i += 1
            j += 1
        elif a[j] == key:
            j += 1
        else:
            pivot -= 1
            a[j], a[pivot] = a[pivot], a[j]

    randomized_quick_sort3(a, left, i)
    randomized_quick_sort3(a, pivot, right)


#     :( modifies array
if __name__ == '__main__':
    sys.setrecursionlimit(15000)
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort3(a, 0, n)
    for x in a:
        print(x, end=' ')
