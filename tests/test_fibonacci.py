from containers.fibonacci import fibs,fib,Fib,FibIter,fib_yield
import inspect 
import pytest

################################################################################
# FibIter
################################################################################

def test_FibIter_1():
    x = FibIter(1)
    assert next(x) == 1
    assert pytest.raises(StopIteration)


def test_FibIter_2():
    x = FibIter(2)
    assert next(x) == 1
    assert next(x) == 1
    assert pytest.raises(StopIteration)


def test_FibIter_3():
    x = FibIter(3)
    assert next(x) == 1
    assert next(x) == 1
    assert next(x) == 2
    assert pytest.raises(StopIteration)


def test_FibIter_4():
    x = FibIter(10)
    assert next(x) == 1
    assert next(x) == 1
    assert next(x) == 2
    assert next(x) == 3
    assert next(x) == 5
    assert next(x) == 8
    assert next(x) == 13
    assert next(x) == 21
    assert next(x) == 34
    assert next(x) == 55
    assert pytest.raises(StopIteration)


def test_FibIter_5():
    x = FibIter(None)
    assert next(x) == 1
    assert next(x) == 1
    assert next(x) == 2
    assert next(x) == 3
    assert next(x) == 5
    assert next(x) == 8
    assert next(x) == 13
    assert next(x) == 21
    assert next(x) == 34
    assert next(x) == 55
    for i in range(100000):
        next(x)

################################################################################
# Fib
################################################################################

def test_Fib_repr_1():
    assert repr(Fib(5)) == "Fib(5)"

def test_Fib_repr_2():
    assert repr(Fib()) == "Fib()"

def test_Fib_str_1():
    assert str(Fib(5)) == "Fib(5)"

def test_Fib_str_2():
    assert str(Fib()) == "Fib()"

def test_Fib_1():
    assert list(Fib(1)) == fibs(1)

def test_Fib_2():
    assert list(Fib(2)) == fibs(2)

def test_Fib_3():
    assert list(Fib(3)) == fibs(3)

def test_Fib_4():
    assert list(Fib(10)) == fibs(10)

def test_Fib_5():
    assert list(Fib(100)) == fibs(100)

def test_Fib_6():
    for f,i in zip(Fib(),range(100000)):
        assert True

################################################################################
# fib_yield
################################################################################

def test_fib_yield_0():
    assert inspect.isgeneratorfunction(fib_yield)

def test_fib_yield_1():
    assert list(fib_yield(1)) == fibs(1)

def test_fib_yield_2():
    assert list(fib_yield(2)) == fibs(2)

def test_fib_yield_3():
    assert list(fib_yield(3)) == fibs(3)

def test_fib_yield_4():
    assert list(fib_yield(10)) == fibs(10)

def test_fib_yield_5():
    assert list(fib_yield(100)) == fibs(100)

def test_fib_yield_6():
    for f,i in zip(fib_yield(),range(100000)):
        assert True
