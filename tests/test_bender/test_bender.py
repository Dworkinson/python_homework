import pytest
from io import StringIO

from bender.bender import \
    max5, InvalidParameter, factorial_recursion,\
    factorial, factorial2, array_abs,\
    array_sum


def test_max5(monkeypatch):
    user_input = StringIO('1 2 3 4 5\n')
    monkeypatch.setattr('sys.stdin', user_input)
    assert max5() == 5


def test_invalid_parameter_exception(monkeypatch):
    user_input = StringIO('1 2 3 4 5 6\n')
    monkeypatch.setattr('sys.stdin', user_input)

    with pytest.raises(InvalidParameter):
        max5()

    with pytest.raises(InvalidParameter):
        factorial_recursion(-1)

    with pytest.raises(InvalidParameter):
        factorial(-1)

    with pytest.raises(InvalidParameter):
        factorial2(-1)


def test_factorial_recursion():
    assert factorial_recursion(5) == 120


def test_factorial():
    factorial(5)
    assert '120\n'

    factorial(1)
    assert '1\n'


def test_factorial2():
    factorial2(0)
    assert '1\n'

    factorial2(5)
    assert '120\n'


def test_array_abs():
    test_array = 1, 2, -3, -4, -5
    assert array_abs(test_array) == [1, 2, 3, 4, 5]


def test_array_sum():
    test_array = 1, 2, -3, -4, -5
    assert array_sum(test_array) == -9
