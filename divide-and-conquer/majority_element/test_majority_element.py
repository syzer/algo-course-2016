# use py.test
# nodemon -x 'py.test ./divide-and-conquer/majority_element/test_majority_element.py'
from majority_element import *


# def test_majority2():
#     assert get_majority_pythonic([2, 3, 9, 2, 2], 0, 5) == 1
#     assert get_majority_pythonic([1, 2, 3, 4], 0, 4) == 0
#     assert get_majority_pythonic([1, 2, 3, 1], 0, 4) == 0

def test_get_majority_element():
    assert get_maj_el([2, 3, 9, 2, 2], 0, 5) == 1
    assert get_maj_el([2, 10, 12, 12, 3, 9, 2, 2, 2, 2, 2], 0, 11) == 1
    assert get_maj_el([1, 2, 3, 4, 5], 0, 5) == 0
    assert get_maj_el([1, 2, 3, 1], 0, 4) == 0


if __name__ == '__main__':
    print('Use py.test')
    test_majority2()
