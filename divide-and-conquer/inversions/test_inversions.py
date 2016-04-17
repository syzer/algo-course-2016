# nodemon -x 'py.test test_inversions.py'
from .inversions import *


# inversions [3,2], [9,3]
def test_small():
    a = [2, 3, 9, 2, 9]
    b = len(a) * [0]
    assert get_number_of_inversions(a, b, 0, len(a) - 1) == 2


def test_sorted():
    a = [1, 2, 3, 10, 11]
    b = len(a) * [0]
    assert get_number_of_inversions(a, b, 0, len(a) - 1) == 0


# inversions =  [3,2], [5,2], [5,4]
def test_3():
    a = [1, 3, 5, 2, 4, 6]
    b = len(a) * [0]
    assert get_number_of_inversions(a, b, 0, len(a) - 1) == 3


# max num of inversion its (n over  2) = n(n-1) / 2
def test_out_of_order():
    a = [11, 10, 9, 5, 2, 1]
    b = len(a) * [0]
    assert get_number_of_inversions(a, b, 0, len(a) - 1) == 15


def test_4():
    a = [11, 2, 3, 4, 5]
    b = len(a) * [0]
    assert get_number_of_inversions(a, b, 0, len(a) - 1) == 4


def test_big():
    a = [4, 80, 70, 23, 9, 60, 68, 27, 66, 78, 12, 40, 52, 53, 44, 8, 49, 28, 18, 46, 21, 39, 51, 7, 87, 99, 69, 62, 84,
         6, 79, 67, 14, 98, 83, 0, 96, 5, 82, 10, 26, 48, 3, 2, 15, 92, 11, 55, 63, 97, 43, 45, 81, 42, 95, 20, 25, 74,
         24, 72, 91, 35, 86, 19, 75, 58, 71, 47, 76, 59, 64, 93, 17, 50, 56, 94, 90, 89, 32, 37, 34, 65, 1, 73, 41, 36,
         57, 77, 30, 22, 13, 29, 38, 16, 88, 61, 31, 85, 33, 54]
    b = len(a) * [0]
    assert get_number_of_inversions(a, b, 0, len(a) - 1) == 2372


if __name__ == '__main__':
    test_4()
    print('use pytest')
