# nodemon -x 'py.test ./divide-and-conquer/test_sort_whitout_comparition.py'
from count_sort import sort_count
import random

# Count sort
# works for small int
a = [2, 3, 2, 1, 3, 2, 2, 3, 2, 2, 2, 1]

# 3 digits
# left-> right
# count apperances
counts = [2, 7, 3]

# we put 1 twice
# 2 seven times
# 3 three times
b = [1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3]


def test_1():
    assert sort_count(a) == b

def test_2():
    rnd_sample = random.sample(range(30), 4)
    assert sort_count(rnd_sample) == sorted(rnd_sample)


if __name__ == '__main__':
    print('use pytest')


# def most_common(lst):
#     return max(set(lst), key=lst.count)
