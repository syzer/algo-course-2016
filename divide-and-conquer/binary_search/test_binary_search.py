from binary_search import *
import random

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
