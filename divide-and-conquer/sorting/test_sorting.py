# nodemon -x 'py.test ./divide-and-conquer/sorting/test_sorting.py'
import sys
import random
from .sorting import randomized_quick_sort, partition2, partition3


def test_randomized_sort():
    a = [4, 3, 2, 5, 1]
    assert randomized_quick_sort(a, 0, len(a) - 1) == sorted(a)


if __name__ == '__main__':
    print('use pytest')
