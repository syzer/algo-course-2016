import random


def quick_sort(a):
    if a == []:
        return []
    else:
        pivot = a[0]
        lesser = quick_sort([x for x in a[1:] if x < pivot])
        greater = quick_sort([x for x in a[1:] if x >= pivot])
        return lesser + [pivot] + greater


a = [int(1000 * random.random()) for i in range(10000)]
print(quick_sort(a))