# use py.test
from majority_element import *


def test_majority2():
    print(get_majority_pythonic([2, 3, 9, 2, 2], 0, 5))
    print(get_majority_pythonic([1, 2, 3, 4], 0, 4))
    print(get_majority_pythonic([1, 2, 3, 1], 0, 4))



if __name__ == '__main__':
    print('Use py.test')
    test_majority2()
