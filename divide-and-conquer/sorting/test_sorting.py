# nodemon -x 'py.test ./divide-and-conquer/sorting/test_sorting.py'
import random
from .sorting import *

random.seed(10)


def test_randomized_sort():
    a = [4, 3, 2, 5, 1]
    randomized_quick_sort3(a, 0, len(a) - 1)
    # :( modifies array
    assert a == sorted(a)


def test_randomized_sort_large():
    a = [2, 3, 9, 2, 2, 3, 5, 6, 7, 8, 10, 11, 3, 1, 2, 9, 8, 7, 8, 6, 6, 3, 2]
    randomized_quick_sort3(a, 0, len(a) - 1)  # :(
    assert a == sorted(a)


def test_on_random_list():
    a = [int(1000 * random.random()) for i in range(10000)]
    randomized_quick_sort3(a, 0, len(a) - 1)  # :(
    assert a == sorted(a)


if __name__ == '__main__':
    print('use pytest')
