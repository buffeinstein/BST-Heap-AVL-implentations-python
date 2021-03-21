import containers.range
import inspect 
import pytest

def test_range():
    assert inspect.isgeneratorfunction(containers.range.range)

def test_range_1():
    assert list(containers.range.range(10)) == list(range(10))

def test_range_2():
    assert list(containers.range.range(0)) == list(range(0))

def test_range_3():
    assert list(containers.range.range(1)) == list(range(1))

def test_range_4():
    assert list(containers.range.range(-1)) == list(range(-1))


def test_range2_1():
    assert list(containers.range.range(0,10)) == list(range(0,10))

def test_range2_2():
    assert list(containers.range.range(5,10)) == list(range(5,10))

def test_range2_3():
    assert list(containers.range.range(11,10)) == list(range(11,10))

def test_range2_4():
    assert list(containers.range.range(-11,10)) == list(range(-11,10))

def test_range2_5():
    assert list(containers.range.range(-11,10)) == list(range(-11,10))

def test_range2_6():
    assert list(containers.range.range(10,10)) == list(range(10,10))


def test_range3_1():
    assert list(containers.range.range(0,10,1)) == list(range(0,10,1))

def test_range3_2():
    assert list(containers.range.range(0,10,1)) == list(range(0,10,1))

def test_range3_3():
    assert list(containers.range.range(0,10,2)) == list(range(0,10,2))

def test_range3_4():
    assert list(containers.range.range(0,10,3)) == list(range(0,10,3))

def test_range3_5():
    assert list(containers.range.range(0,10,15)) == list(range(0,10,15))

def test_range3_6():
    assert list(containers.range.range(0,10,1)) == list(range(0,10,1))

def test_range3_7():
    assert list(containers.range.range(0,-10,-1)) == list(range(0,-10,-1))

def test_range3_8():
    assert list(containers.range.range(0,-10,-3)) == list(range(0,-10,-3))

def test_range3_9():
    assert list(containers.range.range(0,10,-1)) == list(range(0,10,-1))
