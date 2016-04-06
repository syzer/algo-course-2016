from binary_search import *
import random
import sys


def test_linear():
    a = [1, 5, 8, 12, 13]
    assert linear_search(a, 8) == 2
    assert linear_search(a, 1) == 0
    assert linear_search(a, 23) == -1
    assert linear_search(a, 1) == 0
    assert linear_search(a, 11) == -1


def test_binary():
    a = [1, 5, 8, 12, 13]
    assert binary_search(a, 8) == 2
    assert binary_search(a, 1) == 0
    assert binary_search(a, 23) == -1
    assert binary_search(a, 1) == 0
    assert binary_search(a, 11) == -1


def test_stress_binary():
    a = list(range(0, 101))
    for i in range(200):
        assert binary_search(a, i) == linear_search(a, i)


def stress():
    MAX_EL = 1000
    MAX_I = 20000

    a = list(range(MAX_EL, 10000 + MAX_EL))
    i = random.randint(1, MAX_I)

    bin = binary_search(a, i)
    lin = linear_search(a, i)
    if bin != lin:
        print(i)
        print(a)

    while bin == lin:
        if i < 1500:
            print(i, len(a))
        a = list(range(MAX_EL, 10000 + MAX_EL))
        i = random.randint(1, MAX_I)
        bin = binary_search(a, i)
        lin = linear_search(a, i)

    print(i)
    print(a)


if __name__ == '__main__':
    sys.setrecursionlimit(15000)
    stress()
