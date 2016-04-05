from different_summands import *

def test_1():
    assert optimal_summands(1) == [1]

def test_2():
    assert optimal_summands(2) == [2]

def test_3():
    assert optimal_summands(3) == [1, 2]

def test_4():
    assert optimal_summands(4) == [1, 3]

def test_5():
    assert optimal_summands(5) == [1, 4]

def test_6():
    assert optimal_summands(6) == [1, 2, 3]

def test_8():
    assert optimal_summands(8) == [1, 2, 5]

def test_10():
    assert optimal_summands(10) == [1, 2, 3, 4]

def test_11():
    assert optimal_summands(11) == [1, 2, 3, 5]

def test_13():
    assert optimal_summands(13) == [1, 2, 3, 7]

def test_14():
    assert optimal_summands(14) == [1, 2, 3, 8]

def test_15():
    assert optimal_summands(15) == [1, 2, 3, 4, 5]

def test_16():
    assert optimal_summands(16) == [1, 2, 3, 4, 6]

def test_17():
    assert optimal_summands(17) == [1, 2, 3, 4, 7]

def test_18():
    assert optimal_summands(18) == [1, 2, 3, 4, 8]

def test_19():
    assert optimal_summands(19) == [1, 2, 3, 4, 9]

def test_20():
    assert optimal_summands(20) == [1, 2, 3, 4, 10]

def test_21():
    assert optimal_summands(21) == [1, 2, 3, 4, 5, 6]